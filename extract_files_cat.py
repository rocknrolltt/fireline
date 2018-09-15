file_map={}
for year in range(2003,2015):
    year_str=str(year)
    file_map[year_str]=open("output_nc"+year_str+".csv","w")
f=open("c:/ting/wind/claims_table_for_AER.txt","r")
line=f.readline()
line=line.replace("|", ",")
for value in file_map.values():
    value.write(line)
while line != "":
    line=f.readline()
    field_list=line.split("|")
    claim_field1=field_list[6]
    print claim_field1
        #claim_field2=field_list[27]
    if claim_field1=="WIND": #and claim_field2=="N":
            new_str=",".join(field_list)
            year_field=field_list[3]
            year_str1=year_field[-4:]
            fw=file_map[year_str1]
            fw.write(new_str)
           
for value in file_map.values():
    value.close()
f.close()
