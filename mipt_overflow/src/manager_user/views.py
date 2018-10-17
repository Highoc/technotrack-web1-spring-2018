# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import base64, hashlib, json

from jsonrpc import jsonrpc_method
from manager_user.models import User, File
from django.http.response import HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, HttpResponse

def user_index(request):
    return render(request, 'manager_user/index.html')

def user_info(request):
    return render(request, 'manager_user/info.html')



@jsonrpc_method( 'api.upload_photo' )
def upload_photo( request, user_pk, content_base64 ):
    file_content = base64.b64decode( content_base64 ).decode('utf-8')

    user = User.objects.filter(id=user_pk).first()
    key = generate_key(user.username)

    user.photo.save( '{}/{}'.format(user.id, key), ContentFile(file_content.encode('utf-8')))

    return key


@jsonrpc_method( 'api.upload_file' )
def upload_file( request, user_pk, file_json ):
    file = json.loads(file_json)

    content = base64.b64decode( file['content'] ).decode('utf-8')
    key = generate_key( file['filename'] )
    owner = User.objects.filter( id=user_pk ).first()

    new_file = File.objects.filter(key=key, owners=owner).first()
    if not new_file is None:
        new_file.content.save('{}/{}'.format(user_pk, key), ContentFile(content.encode('utf-8')))
        new_file.save()
    else:
        new_file = File()
        new_file.key = key
        new_file.name = file['filename']
        new_file.mime = file['mime_type']
        new_file.content.save('{}/{}'.format(user_pk, key), ContentFile(content.encode('utf-8')))
        new_file.save()
        new_file.owners.add(owner)

    return key


@jsonrpc_method( 'api.get_file' )
def get_file(request, filename):
    key = generate_key(filename)

    file = File.objects.filter(key=key, owners=request.user).first()

    if file is None:
        return HttpResponseNotFound('404')
        # return HttpResponseForbidden('403')

    else:
        responce = HttpResponse()
        responce['X-Accel-Redirect'] = '/protected/{}/'.format(key)
        return responce


def generate_key(filename):
    h = hashlib.new('md5')
    h.update(filename.encode('utf-8'))
    return h.hexdigest()

