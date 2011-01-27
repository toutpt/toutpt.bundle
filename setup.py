from setuptools import setup, find_packages
import os

version = '1.0dev'

install_requires=[
  'setuptools',
  'gdata',
  'python-memcached',
  'suds',

#deps, setup related
  'collective.autopermission',
  'collective.googleloader',
  'collective.monkeypatcher',
  'plone.app.caching',
  'plone.app.theming',
  'five.grok',
  'Products.CMFPlacefulWorkflow',
  'Products.contentmigration',
  'Products.MemcachedManager',
  'Products.TextIndexNG3',
  'z3c.unconfigure',

#form
  'Products.PloneFormGen',
  'collective.z3cform.norobots',
  'plone.formwidget.autocomplete',
  'plone.formwidget.captcha',
  'archetypes.referencebrowserwidget',
  'archetypes.uploadreferencewidget',
  'Products.CompoundField',

#email features
  'collective.contentrules.mail',
  'Products.EasyNewsletter',
  #'collective.dancing', #collective.singing, five.intid, cssutils, BeautifulSoup, zope.sendmail, zope.keyreference>=3.6.2, zope.app.keyreference==3.6.1',zope.app.catalog', zope.app.i18n', zc.queue', zc.lockfile', plone.z3cform>=0.5.1'

#media (photo, audio, video, google maps)
  'collective.dewplayer',
  'collective.gallery',
  'collective.picnik',
  'p4a.videoembed',
  'Products.Maps',


#menu
  'collective.portlet.actions',
  'qi.portlet.TagClouds',

#social network, RSS,...
  'collective.portlet.feedmixer',
  'collective.sharerizer',

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
      keywords='',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
