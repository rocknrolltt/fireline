
import urllib
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
urllist=["http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001231.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001231.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001233.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001233.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001320.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001320.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001321.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001321.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001322.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001322.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001323.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001323.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001330.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001330.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001332.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2001332.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003011.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003011.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003013.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003013.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003031.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003031.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003033.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003033.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003100.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003100.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003101.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003101.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003102.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003102.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003103.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003103.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003110.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003110.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003112.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003112.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003120.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003120.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003121.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003121.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003122.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003122.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003123.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003123.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003130.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003130.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003132.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003132.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003211.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003211.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003213.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003213.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003231.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003231.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003233.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003233.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003300.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003300.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003301.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003301.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003302.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003302.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003303.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003303.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003310.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003310.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003312.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003312.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003320.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003320.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003321.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003321.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003322.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003322.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003323.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003323.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003330.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003330.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003332.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2003332.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021011.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021011.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021013.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021013.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021031.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021031.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021033.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021033.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021100.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021100.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021101.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021101.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021102.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021102.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021103.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021103.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021110.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021110.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021112.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021112.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021120.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021120.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021121.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021121.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021122.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021122.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021123.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021123.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021130.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021130.tif.ovr" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021132.tif" ,
"http://opendata.digitalglobe.com/carr-fire/post-event/2018-07-24/1030010080C1DE00/2021132.tif.ovr" ]
                          


for list in urllist:
	file_name=list.split('/')[-1]
	urllib.urlretrieve (list,file_name)