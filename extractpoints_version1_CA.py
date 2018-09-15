from osgeo import gdal
from osgeo.gdalconst import *
from osgeo import osr
import time
import numpy



#AZcountylist=["cno","apa","cuz","gee","ghm","gla","moh","mrc","nav","paz","pin","pma","yav","yma","coc"]
# COcountylist=["ads","alm","ara","arc","bac","bld","bmf","bnt","cek",
# 			"cha","chy","cnj","cos","cus","cwl","den","det","dol","dug",
# 			"eag","elb","fem","gaf","glp","gra","gun","hin","hue","jak",
# 			"jfe","kit","kiw","laa","lap","lar","lgn","lke","lnk",
# 			"mes","mff","min","mor","mot","mtz","ote","our","pas","php",
# 			"pky","prw","ptk","pub","rib","rig","rtt","saj","sam",
# 			"sau","sed","smm","tll","uma","wel","wtn"]
#IDcountylist=["ada","adm","ban","ber","bnw","bin","bla","bos","bon","bov","bou","btt","cam","can","cbo","cas","clk","clr","cst","elm","frk","fmt",
			  #"gem","god","idh","jfs","jer","koo","lat","lem","lis","lin","mdi","mid","nez","one","owy","pay","pow","sho","tet","tnf","vll","whg"]
# MTcountylist=["bvr","bhr","bne","bwt","cbn","crt","csd","cho","csr","dan","dws","drl","fal","frg","flh","gal","grf","glc","gdv","grt","hli","jrs","jdb","lae","lac","lbr","lic","mcc","man","mea","mnl","mis",
# 			  "mus","par","pet","phl","pon","pwr","pwl","prr","rav","rcl","roo","rbd","snd","srd","svb","slw","swg","ttn","tol","tre","vly","wtl","wib","yel"]
#NMcountylist=["brn","cat","chv","cib","cox","cur","deb","doa","edd","grn","gua","hrd","hid","lea","lcn","lam","lun","mck","mra","otr","qua","rio","ros","sdv","sju","smg","sfe","ser","sor","tao","trr","uno","val"]
#OKcountylist=["adi","alf","ato","bev","bec","bli","bry","cad","cnd","cre","che","ctw","cim","clv","coa","cmc","cot","cra","cee","cer","dlw","dew","els","gfi","gvn","grd","gan","gre","hmn","hrp","has","hug","jcs","jsn","joh","kay","kfs","kio","lti"
	#,"lef","lcl","log","lve","maj","msh","may","mcn","mcu","mci","mur","msk","nob","now","okf","okl","okm","osa","ott","paw","pyn","pit","pnt","pot","pus","rog","rgr","sem","seq","sph","tex","tmn","tsa","wag","win","wit","woo","wdw"]
#ORcountylist=["bak","btn","kam","cla","cou","coo","cok","crr","des","dgl","gil","gat","har","hoo","jac","jff","jos","kla","lka","lne","lil","lnn","mal","mao","mrr","mlt","pok","she","til","umt","uni","wao","was","wat","wee","yhl"]
# TXcountylist=["and","adw","ang","arn","ach","arm","ata","aus","bly","bdr","bst","byl","bee","bll","bex","bln","brd","bsq","bwi","bza","bzs","brw","brs","brk","bwn",
# 			  "brl","brt","cld","clh","cll","cmr","cmp","crs","css","ctr","chm","chk","chl","cly","cch","cke","com","cln","clg","crd","cml","cmn","cnc","coe","cry",
# 			  "ctt","crn","cck","crb","clb","dll","dls","daw","dfs","dlt","dnt","dwt","dck","dmm","dnl","dvl","est","ect","edw","ell","elp","ert","fll","fnn","fyt",
# 			  "fsh","fly","foa","ftb","fnk","fst","fri","gns","glv","grz","gll","gls","gld","gnz","gry","grs","grg","grm","gdl","hal","hll","ham","han","hrm","hrn",
# 			  "hrr","hrs","hrt","hsk","hay","hmp","hnd","hdg","hil","hck","hod","hpk","hst","how","hud","hnt","htc","iri","jck","jks","jsp","jfd","jfr","jmh","jmw",
# 			  "jhn","jns","kar","kfm","ken","knd","knt","krr","kmb","kig","knn","klb","knx","lmr","lmb","lmp","lsl","lvc","lee","leo","lib","lim","lip","lvo","lln","lov",
# 			  "lbb","lyn","mcl","mln","mml","mds","mrn","mrt","msn","mtg","mav","mdn","mnr","ndl","mlm","mll","mtl","mng","mgm","mre","mrs","mty","ncg","nvr","nwt","nln","nue"
# 			  ,"pch","old","orn","plp","pnl","prk","prm","pcs","plk","ptt","prs","rns","rnd","rea","rel","rrv","ree","ref","rob","rbs","rck","rnn","rsk","sab","sag","sjc","spt",
# 			  "ssb","sch","scr","shk","shl","shr","smi","som","str","stp","stg","stw","stt","sws","tar","tay","trl","try","thr","tts","tgr","trv","trt","tty","ups","upt","uva","vvr",
# 			  "vzn","vic","wlk","wll","wrd","wsh","wbb","wrt","wlr","wch","wlb","wlc","wlm","wls","wnk","wse","wod","yok","yng","zap","zav"]

#UTcountylist=["bea","box","cac","car","dag","dav","dch","emr","gfd","gnd","iro","jua","kne","mld","mgn","piu","ric","stl","sun","san","sev","sum","too","unt","uta","waa","war","way","web"]
#WAcountylist=["ams","aso","ben","che","clm","cak","clu","cow","dog","fer","fra","gar","gnt","grh","isl","jef","kin","ksp","ktt","kli","lew","lkn","mas","oka","pac","peo","prc","sjn","ska","skm","sno","spk","ste","thu","wkk","wal","whc","whm","yak"]
#WYcountylist=["alb","bgh","cpb","cao","cvr","cro","fmo","gos","hot","jon","lrm","lco","nat","nio","pak","plt","srn","sbl","swe","ton","uin","wsk","wst"]
#NVcountylist=["chc","crk","dou","elk","esm","eur","hum","lan","lnc","lyo","mrl","nye","per","sto","who","wte","cct"]
CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			  "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			  "sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]


AZscorefinal=[]
text = numpy.genfromtxt("D:/twu/wildfire/CA.txt",delimiter='\t',dtype=None,skiprows=1)
for county in CAcountylist:
	aflist="D:/twu/FRoldSHIA2014/CA/%s/%sfroshia.img"%(county,county)
	fuelslopelist="D:/twu/Mosaic2014/CA/%s/%smosaic.img"%(county,county)
	accesslist="D:/twu/Hazard/GRID/CA/%s/%shazg/w001001.adf" %(county,county)
	time0=time.time()
	#reading areafuel image"
	print aflist
	ds1 = gdal.Open(aflist)
	band2=ds1.GetRasterBand(1)
	gt1 = ds1.GetGeoTransform()
	srs1 = osr.SpatialReference()
	srs1.ImportFromWkt(ds1.GetProjection())
	srslatlong1 = srs1.CloneGeogCS()
	ct1 = osr.CoordinateTransformation(srslatlong1,srs1)
	ras1 = band2.ReadAsArray()


	print fuelslopelist
	ds=gdal.Open(fuelslopelist)
	band1=ds.GetRasterBand(1)
	gt = ds.GetGeoTransform()
	srs = osr.SpatialReference()
	srs.ImportFromWkt(ds.GetProjection())
	srslatlong = srs.CloneGeogCS()
	ct = osr.CoordinateTransformation(srslatlong,srs)
	ras2 = band1.ReadAsArray()

	print accesslist
	ds2=gdal.Open(accesslist)
	band3=ds2.GetRasterBand(1)
	gt2=ds2.GetGeoTransform()
	srs2=osr.SpatialReference()
	srs2.ImportFromWkt(ds2.GetProjection())
	srslatlong2 = srs2.CloneGeogCS()
	ct2 = osr.CoordinateTransformation(srslatlong2,srs2)
	ras3 = band3.ReadAsArray()

	def areafuel(latlonpairs):


		point = latlonpairs
		(point[1],point[0],holder) = ct1.TransformPoint(point[1],point[0])
		x = (point[1] - gt1[0])/gt1[1]
		y = (point[0] - gt1[3])/gt1[5]
		if x>0 and y>0:
			try:

				value1 = ras1[int(y),int(x)]

				if (value1>=0 and value1<110):

					value4=(value1)%100
					if (value1/100!=0):

						SHIA="Y"
					else:
						SHIA="N"
				else:
					SHIA=999
					value4=999
			except:
				value4=999
				SHIA=999
		else:
			value4=999
			SHIA=999
		ds1=None
		return value4,SHIA


	def fuelslope(latlonpairs):
		#reading fuel and slope image"


		point = latlonpairs
		(point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
		x = (point[1] - gt[0])/gt[1]
		y = (point[0] - gt[3])/gt[5]

		if x>0 and y>0:
			try:
				value2 = ras2[int(y),int(x)]

				if value2>0 & value2<60:
					slope=value2/10
					Fuel=value2%10
					if slope==4:
						slope=5
					if value2%10==4:
						Fuel="NF"
					elif value2%10==6:
						Fuel="WA"
					elif value2%10==5 or value2%10 ==0:
						Fuel="F0"
					elif value2%10==2:
						Fuel="F3"
					elif value2%10==3:
						Fuel="F5"
					else:
						Fuel="F1"

				else:
					slope=999
					Fuel=999


			except:
				slope=999
				Fuel=999
		else:
			slope=999
			Fuel=999

		ds=None
		return slope, Fuel


	def accessore(latlonpairs):
		#reading access image"


		point = latlonpairs
		(point[1],point[0],holder) = ct2.TransformPoint(point[1],point[0])
		x = (point[1] - gt2[0])/gt2[1]
		y = (point[0] - gt2[3])/gt2[5]
		if x>0 and y>0:
			try:
				value3 = ras3[int(y),int(x)]
				if value3>0 and value3<=46:
					value3="0"
				elif value3>=61 and value3<=96:
					value3="1"
				elif value3>=111 and value3<=146:
					value3="3"
				elif value3>=161 and value3<=194:
					value3="5"
				else:
					value3=999

			except:
				value3=999
		else:
			value3=999
		ds2=None
		return value3



	count=0
	for row in text:

		count+=1
		lat=row[3]
		lon=row[2]
		#Shia=row[2]
		#print lat,lon

		value4,SHIA=areafuel([lat,lon])
		slope,Fuel=fuelslope([lat,lon])
		value3=accessore([lat,lon])
		WFHS=int(value4)*int(slope)+int(value3)

		AZscorefinal.append([row[0],row[1],lon,lat,value4,slope,Fuel,value3,WFHS,SHIA])

	print count

	del ras1
	del ras2
	del ras3
	time1=time.time()
	looptime=time1-time0
	print looptime


numpy.savetxt('D:/twu/wildfire/CAscore.txt',AZscorefinal,delimiter="\t",fmt='%s')
df=numpy.genfromtxt("D:/twu/wildfire/CAscore.txt",delimiter='\t',dtype=None,skiprows=0)

df=numpy.unique(df)
# print df[1]

# unique_keys, indices = numpy.unique(df[:,0], return_index=True)
# df=df[indices]



newlist=[]
for row in df:
	if (row[4]=='999' or row[4]==999 or row[4]==255 or row[4]=='255')or (row[5] =='999' or row[5]==999 or row[5]==255 or row[5]=='255') or (row[6]=='999'or row[6]==999 or row[6]==255 or row[6]=='255')or (row[7]=='999' or row[7]==999 or row[7]==255 or row[7]=='255'):
		continue

	else:
		newlist.append(row)

numpy.savetxt('D:/twu/wildfire/CAscoreunique.txt',newlist,delimiter="\t",fmt='%s')

