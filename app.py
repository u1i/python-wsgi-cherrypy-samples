#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cherrypy


class App:

  @cherrypy.expose
  def index(self):
    '''Make some traffic'''  
    return ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean quis laoreet urna. '
      'Integer vitae volutpat neque, et tempor quam. Sed eu massa non libero pretium tempus. '
      'Quisque volutpat aliquam lacinia. Class aptent taciti sociosqu ad litora torquent per '
      'conubia nostra, per inceptos himenaeos. Quisque scelerisque pellentesque purus id '
      'vulputate. Suspendisse potenti. Vestibulum rutrum vehicula magna et varius. Sed in leo'
      ' sit amet massa fringilla aliquet in vitae enim. Donec justo dolor, vestibulum vitae '
      'rhoncus vel, dictum eu neque. Fusce ac ultrices nibh. Mauris accumsan augue vitae justo '
      'tempor, non ullamcorper tortor semper. ')


cherrypy.tree.mount(App(), '/')
