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
	'NBC',
	'ABC',
	'CBS',
	'NBC Golf',
	'NBC Sports',
	'NBA',
	'Bloomberg TV',
	'MNB 1',
	'MNB 2',
	'UBS',
	'NTV',
	'ETV',
	'Eh Oron',
	'TV5',
	'TV9',
	'25',
	'EDU',
	'Eagle',
	'SBN',
	'Royal',
	'Parliament'
]
urls = [
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mongolhd.smil/playlist.m3u8',
	'http://cp.dmbshare.net:8000/live/aaron/aaron/4578.ts',
	'http://cp.dmbshare.net:8000/live/aaron/aaron/4601.ts',
	'http://cp.dmbshare.net:8000/live/aaron/aaron/4576.ts',
	'http://cp.dmbshare.net:8000/live/aaron/aaron/4586.ts',
	'http://cp.dmbshare.net:8000/live/aaron/aaron/4587.ts',
	'http://cp.dmbshare.net:8000/live/aaron/aaron/4577.ts',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:bloomberg.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mnb.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mnb_2.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:ubs.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:ntv.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:etv.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:ehoron.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:tv5.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:tv9.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:mn25.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:edu.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:eagle.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:sbn.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:royal.smil/playlist.m3u8',
	'http://202.70.45.36/hls/_definst_/tv_mid/smil:parliament.smil/playlist.m3u8'
]
icons=[
	'mongol-tv.png',
	'mongol-tv.png',
	'mongol-tv.png',
	'mongol-tv.png',
	'mongol-tv.png',
	'mongol-tv.png',
	'bloomberg.png',
	'mnb_512x512.png',
	'mn2_512x512.png',
	'ubs_512x512.png',
	'ntv_512x512.png',
	'etv_512x512.png',
	'ehoron_512x512.png',
	'tv5_512x512.png',
	'tv9_512x512.png',
	'royalhd_512x512.png',
	'edu_512x512.png',
	'eagle_512x512.png',
	'sbn_512x512.png',
	'royalhd_512x512.png',
	'royalhd_512x512.png',
]

for name,url,icon in zip(names,urls,icons):
	li = xbmcgui.ListItem(label=name, path=url)
	li.setThumbnailImage(os.path.join(image_dir,icon))
	li.setIconImage(os.path.join(image_dir,icon))
	li.setInfo(type='Video', infoLabels={ "Title": name })
	li.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
