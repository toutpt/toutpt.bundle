from setuptools import setup, find_packages
import os

version = '1.0dev'

install_requires=[
  'setuptools',
  'gdata',
  'python-memcached',
  'suds',

#deps, setup related
  'collective.googleloader',
  'collective.monkeypatcher',
  'plone.app.caching',
  'plone.app.theming',
  'five.grok',
  'Products.CMFPlacefulWorkflow',
  'Products.contentmigration',
  'Products.MemcachedManager',
  'z3c.unconfigure',

#forms
  'Products.PloneFormGen',
  'collective.z3cform.norobots',
  'plone.formwidget.autocomplete',
  'plone.formwidget.captcha',
  'archetypes.referencebrowserwidget',
  'archetypes.uploadreferencewidget',

#email features
  'collective.contentrules.mail',

#media (photo, audio, video, google maps)
  'collective.dewplayer',
  'collective.carousel',
  'collective.gallery',
#  'collective.googlemaps',
  'collective.picnik',
  'nmd.plonelinkasvideoembed',

#some extra portlets
  'collective.portlet.actions',
  'qi.portlet.TagClouds',

#social network, RSS,...
  'collective.portlet.feedmixer',
  'collective.sharerizer',
  'collective.disqus',

#others 
  'collective.portlet.contact',
  'collective.sugarcrm',

]
setup(name='toutpt.bundle',
      version=version,
      description="A bundle of add-ons",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/toutpt.bundle',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require = {'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
