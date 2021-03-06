import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import os

addon_handle = int(sys.argv[1])
base_url = sys.argv[0]

__settings__ = xbmcaddon.Addon(id='plugin.video.mongolian-live-tv')
rootDir = xbmc.translatePath(__settings__.getAddonInfo('path')).decode('utf-8')
image_dir = os.path.join(rootDir, 'resources', 'media')

print image_dir

xbmcplugin.setContent(addon_handle, 'videos')

names = [
	'Mongol TV',
	'Bloomberg TV',
	'MNB 1',
	'MNB 2',
	'UBS',
	'Edu TV',
	'NTV',
	'TV5',
	'Eagle News',
	'SBN',
	'TV9',
	'ETV',
	'Royal HD',
	'Ekh Oron',
	'25',
	'Parliament'
]
urls = [
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mongolhd.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:bloomberg.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mnb.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mnb_2.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:ubs.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:edu.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:ntv.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:tv5.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:eagle.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:sbn.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:tv9.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:etv.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:royal.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:ehoron.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mn25.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:parliament.smil/playlist.m3u8'
]
icons=[
	'mongol-tv.png',
	'bloomberg.png',
	'mnb_512x512.png',
	'mn2_512x512.png',
	'ubs_512x512.png',
	'edu_512x512.png',
	'ntv_512x512.png',
	'tv5_512x512.png',
	'eagle_512x512.png',
	'sbn_512x512.png',
	'tv9_512x512.png',
	'etv_512x512.png',
	'royalhd_512x512.png',
	'ehoron_512x512.png',
	'molor_512x512.png',
	'sch_512x512.png'
]

for name,url,icon in zip(names,urls,icons):
	li = xbmcgui.ListItem(label=name, path=url)
	li.setThumbnailImage(os.path.join(image_dir,icon))
	li.setIconImage(os.path.join(image_dir,icon))
	li.setInfo(type='Video', infoLabels={ "Title": name })
	li.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
