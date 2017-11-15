#!/usr/bin/python
import tools as tools


Natom = 3
# Newton X filename
filename = 'final_output' 
workfile = tools.readfile(filename)
xyzs = tools.geoms(workfile,Natom)
tools.writer_geoms(xyzs)

# Model input name
template_inpname = 'molinp.input'
foldername = 'geoms'
tools.write_molcasinp(template_inpname,foldername)


