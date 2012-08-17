# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AcGuid(models.Model):
    scriptid = models.IntegerField(null=True, blank=True)
    guid = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'ac_guid'

class Agentcomputerdata(models.Model):
    computerid = models.IntegerField(primary_key=True, db_column='ComputerID') # Field name made lowercase.
    checks = models.IntegerField(db_column='Checks') # Field name made lowercase.
    fails = models.IntegerField(db_column='Fails') # Field name made lowercase.
    reliablity = models.IntegerField(db_column='Reliablity') # Field name made lowercase.
    master = models.IntegerField(db_column='Master') # Field name made lowercase.
    noalerts = models.IntegerField(db_column='NoAlerts') # Field name made lowercase.
    uptimestart = models.TextField(db_column='UpTimeStart') # Field name made lowercase. This field type is a guess.
    uptimeend = models.TextField(db_column='UpTimeEnd') # Field name made lowercase. This field type is a guess.
    indicator = models.CharField(max_length=3072, db_column='Indicator') # Field name made lowercase.
    class Meta:
        db_table = u'agentcomputerdata'


class Autostartupdefs(models.Model):
    autodefid = models.IntegerField(primary_key=True, db_column='AutoDefID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    ltype = models.IntegerField(db_column='LType') # Field name made lowercase.
    location = models.CharField(max_length=600, db_column='Location') # Field name made lowercase.
    removemethod = models.IntegerField(db_column='RemoveMethod') # Field name made lowercase.
    class Meta:
        db_table = u'autostartupdefs'

class Availableapps(models.Model):
    appid = models.IntegerField(primary_key=True, db_column='AppID') # Field name made lowercase.
    name = models.CharField(max_length=60, unique=True, db_column='Name') # Field name made lowercase.
    filename = models.CharField(max_length=300, db_column='Filename') # Field name made lowercase.
    arguments = models.CharField(max_length=1500, db_column='Arguments') # Field name made lowercase.
    postinstall = models.CharField(max_length=4500)
    addreg = models.TextField(db_column='AddReg') # Field name made lowercase.
    uninstall = models.CharField(max_length=4500, db_column='Uninstall') # Field name made lowercase.
    description = models.CharField(max_length=600, db_column='Description') # Field name made lowercase.
    last_user = models.CharField(max_length=90, db_column='Last_User') # Field name made lowercase.
    last_date = models.DateTimeField(db_column='Last_Date') # Field name made lowercase.
    class Meta:
        db_table = u'availableapps'

class Chattranscript(models.Model):
    chatid = models.IntegerField(primary_key=True, db_column='ChatID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    username = models.CharField(max_length=765, db_column='Username') # Field name made lowercase.
    message = models.TextField(db_column='Message') # Field name made lowercase.
    postdate = models.DateTimeField(db_column='PostDate') # Field name made lowercase.
    console = models.IntegerField(db_column='Console') # Field name made lowercase.
    class Meta:
        db_table = u'chattranscript'

class Datacache(models.Model):
    cacheid = models.IntegerField(primary_key=True, db_column='CacheID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    cachetype = models.IntegerField(db_column='CacheType') # Field name made lowercase.
    data = models.TextField(db_column='DATA', blank=True) # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded') # Field name made lowercase.
    class Meta:
        db_table = u'datacache'

class Datacollectors(models.Model):
    agentid = models.IntegerField(primary_key=True, db_column='AgentID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    valuename = models.CharField(max_length=75, db_column='ValueName') # Field name made lowercase.
    unitname = models.CharField(max_length=60, db_column='UnitName') # Field name made lowercase.
    yvalueid = models.IntegerField(db_column='YValueID') # Field name made lowercase.
    maxvalue = models.IntegerField(db_column='MaxValue') # Field name made lowercase.
    class Meta:
        db_table = u'datacollectors'

class Dataviewfolders(models.Model):
    folderid = models.IntegerField(primary_key=True, db_column='FolderID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'dataviewfolders'

class Defragmentation(models.Model):
    driveid = models.IntegerField(db_column='DriveID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    volumesize = models.BigIntegerField(db_column='Volumesize') # Field name made lowercase.
    clustersize = models.IntegerField(db_column='ClusterSize') # Field name made lowercase.
    usedspace = models.BigIntegerField(db_column='UsedSpace') # Field name made lowercase.
    freespace = models.BigIntegerField(db_column='FreeSpace') # Field name made lowercase.
    freepercent = models.IntegerField(db_column='FreePercent') # Field name made lowercase.
    totalfrag = models.IntegerField(db_column='TotalFrag') # Field name made lowercase.
    filefrag = models.IntegerField(db_column='FileFrag') # Field name made lowercase.
    freefrag = models.IntegerField(db_column='FreeFrag') # Field name made lowercase.
    totalfiles = models.IntegerField(db_column='TotalFiles') # Field name made lowercase.
    avgfilesize = models.IntegerField(db_column='AvgFileSize') # Field name made lowercase.
    totalfragfiles = models.IntegerField(db_column='TotalFragFiles') # Field name made lowercase.
    excessfilefrag = models.IntegerField(db_column='ExcessFileFrag') # Field name made lowercase.
    avgfragfile = models.IntegerField(db_column='AvgFragFile') # Field name made lowercase.
    pagefilesize = models.IntegerField(db_column='PageFileSize') # Field name made lowercase.
    pagefilefrag = models.IntegerField(db_column='PageFileFrag') # Field name made lowercase.
    totalfolders = models.IntegerField(db_column='TotalFolders') # Field name made lowercase.
    fragfolders = models.IntegerField(db_column='FragFolders') # Field name made lowercase.
    excessfolderfrag = models.IntegerField(db_column='ExcessFolderFrag') # Field name made lowercase.
    mftsize = models.IntegerField(db_column='MFTSize') # Field name made lowercase.
    mftrecords = models.IntegerField(db_column='MFTrecords') # Field name made lowercase.
    mftpercent = models.IntegerField(db_column='MFTPercent') # Field name made lowercase.
    mftfrag = models.IntegerField(db_column='MFTFrag') # Field name made lowercase.
    class Meta:
        db_table = u'defragmentation'

class Failedemails(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    to = models.CharField(max_length=765, db_column='To') # Field name made lowercase.
    from_field = models.CharField(max_length=765, db_column='From') # Field name made lowercase. Field renamed because it was a Python reserved word.
    cc = models.CharField(max_length=765, db_column='CC') # Field name made lowercase.
    subject = models.CharField(max_length=765, db_column='Subject') # Field name made lowercase.
    body = models.CharField(max_length=6000, db_column='Body') # Field name made lowercase.
    errormsg = models.CharField(max_length=765, db_column='ErrorMsg') # Field name made lowercase.
    faildate = models.DateTimeField(db_column='FailDate') # Field name made lowercase.
    class Meta:
        db_table = u'failedemails'

class HAgentdatayearly(models.Model):
    agentid = models.IntegerField(primary_key=True, db_column='AgentID') # Field name made lowercase.
    computerid = models.IntegerField(primary_key=True, db_column='ComputerID') # Field name made lowercase.
    value = models.DecimalField(decimal_places=4, max_digits=15, db_column='Value') # Field name made lowercase.
    year = models.IntegerField(primary_key=True, db_column='Year') # Field name made lowercase.
    samples = models.IntegerField(db_column='Samples') # Field name made lowercase.
    class Meta:
        db_table = u'h_agentdatayearly'

class HClientstatsweekly(models.Model):
    clientid = models.IntegerField(primary_key=True, db_column='ClientID') # Field name made lowercase.
    closedtickets = models.IntegerField(db_column='ClosedTickets') # Field name made lowercase.
    newtickets = models.IntegerField(db_column='NewTickets') # Field name made lowercase.
    opentickets = models.IntegerField(db_column='OpenTickets') # Field name made lowercase.
    avgclose = models.IntegerField(db_column='AVGClose') # Field name made lowercase.
    timeenties = models.IntegerField(db_column='TimeEnties') # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TotalTime') # Field name made lowercase.
    week = models.IntegerField(primary_key=True, db_column='Week') # Field name made lowercase.
    year = models.IntegerField(primary_key=True, db_column='Year') # Field name made lowercase.
    class Meta:
        db_table = u'h_clientstatsweekly'

class HCommands(models.Model):
    cmdid = models.IntegerField(primary_key=True, db_column='CmdID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DateExecuted') # Field name made lowercase.
    status = models.IntegerField(db_column='Status') # Field name made lowercase.
    command = models.IntegerField(db_column='Command') # Field name made lowercase.
    output = models.CharField(max_length=600, db_column='OutPut') # Field name made lowercase.
    user = models.CharField(max_length=120, db_column='User') # Field name made lowercase.
    datefinished = models.DateTimeField(db_column='DateFinished') # Field name made lowercase.
    class Meta:
        db_table = u'h_commands'

class HComputerstatsdaily(models.Model):
    computerid = models.IntegerField(primary_key=True, db_column='ComputerID') # Field name made lowercase.
    cpu = models.IntegerField(db_column='CPU') # Field name made lowercase.
    mem = models.IntegerField(db_column='MEM') # Field name made lowercase.
    datain = models.BigIntegerField(db_column='DataIN') # Field name made lowercase.
    dataout = models.BigIntegerField(db_column='DataOut') # Field name made lowercase.
    eventdate = models.DateField(primary_key=True, db_column='EventDate') # Field name made lowercase.
    samples = models.IntegerField(db_column='Samples') # Field name made lowercase.
    class Meta:
        db_table = u'h_computerstatsdaily'

class HComputerstatsmonthly(models.Model):
    computerid = models.IntegerField(primary_key=True, db_column='ComputerID') # Field name made lowercase.
    cpu = models.IntegerField(db_column='CPU') # Field name made lowercase.
    mem = models.IntegerField(db_column='MEM') # Field name made lowercase.
    datain = models.BigIntegerField(db_column='DataIN') # Field name made lowercase.
    dataout = models.BigIntegerField(db_column='DataOut') # Field name made lowercase.
    month = models.IntegerField(primary_key=True, db_column='Month') # Field name made lowercase.
    year = models.IntegerField(primary_key=True, db_column='Year') # Field name made lowercase.
    samples = models.IntegerField(db_column='Samples') # Field name made lowercase.
    class Meta:
        db_table = u'h_computerstatsmonthly'

class HDrivestatsdaily(models.Model):
    driveid = models.IntegerField(primary_key=True, db_column='DriveID') # Field name made lowercase.
    free = models.IntegerField(db_column='Free') # Field name made lowercase.
    frag = models.IntegerField(db_column='Frag') # Field name made lowercase.
    samples = models.IntegerField(db_column='Samples') # Field name made lowercase.
    eventdate = models.DateField(primary_key=True, db_column='EventDate') # Field name made lowercase.
    class Meta:
        db_table = u'h_drivestatsdaily'

class HLocationstats(models.Model):
    locationid = models.IntegerField(unique=True, db_column='LocationID') # Field name made lowercase.
    totalcomputers = models.IntegerField(db_column='TotalComputers') # Field name made lowercase.
    activecomputers = models.IntegerField(db_column='ActiveComputers') # Field name made lowercase.
    locationonline = models.IntegerField(db_column='LocationOnline') # Field name made lowercase.
    totaldevices = models.IntegerField(db_column='TotalDevices') # Field name made lowercase.
    activedevices = models.IntegerField(db_column='ActiveDevices') # Field name made lowercase.
    retiredassets = models.IntegerField(db_column='RetiredAssets') # Field name made lowercase.
    mastercomputers = models.IntegerField(db_column='MasterComputers') # Field name made lowercase.
    probeenabled = models.IntegerField(db_column='ProbeEnabled') # Field name made lowercase.
    servers = models.IntegerField(db_column='Servers') # Field name made lowercase.
    workstations = models.IntegerField(db_column='WorkStations') # Field name made lowercase.
    mobile = models.IntegerField(db_column='Mobile') # Field name made lowercase.
    statdate = models.DateTimeField(unique=True, db_column='StatDate') # Field name made lowercase.
    smartphone = models.IntegerField(db_column='Smartphone') # Field name made lowercase.
    tablet = models.IntegerField(db_column='Tablet') # Field name made lowercase.
    class Meta:
        db_table = u'h_locationstats'

class HProbeinternalDatainterfaces(models.Model):
    deviceid = models.IntegerField(db_column='DeviceId') # Field name made lowercase.
    interfaceindex = models.IntegerField(db_column='InterfaceIndex') # Field name made lowercase.
    ifdescr = models.CharField(max_length=765, db_column='ifDescr', blank=True) # Field name made lowercase.
    iftype = models.IntegerField(null=True, db_column='IfType', blank=True) # Field name made lowercase.
    ifmtu = models.IntegerField(null=True, db_column='ifMtu', blank=True) # Field name made lowercase.
    ifspeed = models.IntegerField(null=True, db_column='ifSpeed', blank=True) # Field name made lowercase.
    ifphysaddress = models.CharField(max_length=150, db_column='ifPhysAddress', blank=True) # Field name made lowercase.
    ifadminstatus = models.IntegerField(null=True, db_column='ifAdminStatus', blank=True) # Field name made lowercase.
    ifoperstatus = models.IntegerField(null=True, db_column='ifOperStatus', blank=True) # Field name made lowercase.
    iflastchange = models.CharField(max_length=765, db_column='ifLastChange', blank=True) # Field name made lowercase.
    ifinoctects = models.IntegerField(null=True, db_column='ifInOctects', blank=True) # Field name made lowercase.
    ifinucastpkts = models.IntegerField(null=True, db_column='ifInUcastPkts', blank=True) # Field name made lowercase.
    ifinnucastpkts = models.IntegerField(null=True, db_column='ifInNucastPkts', blank=True) # Field name made lowercase.
    ifindiscards = models.IntegerField(null=True, db_column='ifInDiscards', blank=True) # Field name made lowercase.
    ifinerrors = models.IntegerField(null=True, db_column='ifInErrors', blank=True) # Field name made lowercase.
    ifunknownprotos = models.IntegerField(null=True, db_column='ifUnknownProtos', blank=True) # Field name made lowercase.
    ifoutoctects = models.IntegerField(null=True, db_column='ifOutOctects', blank=True) # Field name made lowercase.
    ifoutucastpkts = models.IntegerField(null=True, db_column='ifOutUcastPkts', blank=True) # Field name made lowercase.
    ifoutnucastpkts = models.IntegerField(null=True, db_column='ifOutNUCastPkts', blank=True) # Field name made lowercase.
    ifoutdiscards = models.IntegerField(null=True, db_column='ifOutDiscards', blank=True) # Field name made lowercase.
    ifouterrors = models.IntegerField(null=True, db_column='ifOutErrors', blank=True) # Field name made lowercase.
    ifoutqlen = models.IntegerField(null=True, db_column='ifOutQLen', blank=True) # Field name made lowercase.
    ifspecific = models.CharField(max_length=765, db_column='ifSpecific', blank=True) # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate') # Field name made lowercase.
    class Meta:
        db_table = u'h_probeinternal_datainterfaces'

class Hotfixgroups(models.Model):
    groupid = models.IntegerField(primary_key=True, db_column='GroupID') # Field name made lowercase.
    hotfixid = models.CharField(max_length=120, primary_key=True, db_column='HotFixID') # Field name made lowercase.
    approved = models.IntegerField(db_column='Approved') # Field name made lowercase.
    class Meta:
        db_table = u'hotfixgroups'

class Hotfixscripts(models.Model):
    hotfixid = models.CharField(max_length=120, primary_key=True, db_column='HotFixID') # Field name made lowercase.
    scriptguid = models.CharField(max_length=120, db_column='ScriptGUID') # Field name made lowercase.
    class Meta:
        db_table = u'hotfixscripts'

class Hvhconfig(models.Model):
    hvhid = models.IntegerField(primary_key=True, db_column='HVHID') # Field name made lowercase.
    hvhname = models.CharField(max_length=135, db_column='HVHName', blank=True) # Field name made lowercase.
    hvhversion = models.CharField(max_length=135, db_column='HVHVersion', blank=True) # Field name made lowercase.
    hvhnetmgmt = models.CharField(max_length=135, db_column='HVHNetMgmt', blank=True) # Field name made lowercase.
    hvsysteminfoid = models.IntegerField(null=True, db_column='HVSystemInfoID', blank=True) # Field name made lowercase.
    hvhusername = models.CharField(max_length=135, db_column='HVHUserName', blank=True) # Field name made lowercase.
    hvhpassword = models.CharField(max_length=135, db_column='HVHPassword', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hvhconfig'

class Hvsysinfo(models.Model):
    hvhid = models.IntegerField(primary_key=True, db_column='HVHID') # Field name made lowercase.
    hvsysbios = models.CharField(max_length=135, db_column='HVSysBios', blank=True) # Field name made lowercase.
    hvbiosvendor = models.CharField(max_length=135, db_column='HVBiosVendor', blank=True) # Field name made lowercase.
    hvsysdescription = models.CharField(max_length=135, db_column='HVSysDescription', blank=True) # Field name made lowercase.
    hvsysvendor = models.CharField(max_length=135, db_column='HVSysVendor', blank=True) # Field name made lowercase.
    hvsysmodel = models.CharField(max_length=135, db_column='HVSysModel', blank=True) # Field name made lowercase.
    hvserial = models.IntegerField(null=True, db_column='HVSerial', blank=True) # Field name made lowercase.
    hvasset = models.CharField(max_length=135, db_column='HVAsset', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hvsysinfo'


class LMobileandroidperms(models.Model):
    permissionname = models.CharField(max_length=762, db_column='PermissionName') # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'l_mobileandroidperms'

class Ltantiviruspolicy(models.Model):
    primaryid = models.IntegerField(null=True, db_column='PrimaryID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=450, db_column='Name', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=450, db_column='Description', blank=True) # Field name made lowercase.
    defaultpolicy = models.IntegerField(null=True, db_column='DefaultPolicy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ltantiviruspolicy'

class Ltantivirusthreats(models.Model):
    threatid = models.BigIntegerField(db_column='ThreatID') # Field name made lowercase.
    clientid = models.IntegerField(null=True, db_column='ClientID', blank=True) # Field name made lowercase.
    clientname = models.CharField(max_length=450, db_column='ClientName', blank=True) # Field name made lowercase.
    locationid = models.IntegerField(null=True, db_column='LocationID', blank=True) # Field name made lowercase.
    locationname = models.CharField(max_length=450, db_column='LocationName', blank=True) # Field name made lowercase.
    compid = models.IntegerField(null=True, db_column='CompID', blank=True) # Field name made lowercase.
    compname = models.CharField(max_length=450, db_column='CompName', blank=True) # Field name made lowercase.
    mac = models.CharField(max_length=450, db_column='MAC', blank=True) # Field name made lowercase.
    datereceived = models.DateTimeField(null=True, db_column='DateReceived', blank=True) # Field name made lowercase.
    dateoccurred = models.DateTimeField(null=True, db_column='DateOccurred', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=450, db_column='UserName', blank=True) # Field name made lowercase.
    scannerreportedname = models.CharField(max_length=450, db_column='ScannerReportedName', blank=True) # Field name made lowercase.
    level = models.CharField(max_length=450, db_column='Level', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=450, db_column='Name', blank=True) # Field name made lowercase.
    object = models.CharField(max_length=450, db_column='Object', blank=True) # Field name made lowercase.
    virus = models.CharField(max_length=450, db_column='Virus', blank=True) # Field name made lowercase.
    action = models.CharField(max_length=450, db_column='Action', blank=True) # Field name made lowercase.
    info = models.CharField(max_length=450, db_column='Info', blank=True) # Field name made lowercase.
    ack = models.IntegerField(null=True, db_column='Ack', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ltantivirusthreats'

class Maintenancemode(models.Model):
    computerid = models.IntegerField(primary_key=True, db_column='ComputerID') # Field name made lowercase.
    timestart = models.DateTimeField(db_column='TimeStart') # Field name made lowercase.
    durration = models.IntegerField(db_column='Durration') # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    class Meta:
        db_table = u'maintenancemode'

class Mobileiosinstalledprofiles(models.Model):
    profileid = models.IntegerField(primary_key=True, db_column='ProfileID') # Field name made lowercase.
    mobileid = models.IntegerField(db_column='MobileID') # Field name made lowercase.
    entered = models.DateTimeField(db_column='Entered') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    identifier = models.CharField(max_length=765, db_column='Identifier') # Field name made lowercase.
    organization = models.CharField(max_length=765, db_column='Organization') # Field name made lowercase.
    description = models.CharField(max_length=765, db_column='Description') # Field name made lowercase.
    encryption = models.IntegerField(db_column='Encryption') # Field name made lowercase.
    removal = models.IntegerField(db_column='Removal') # Field name made lowercase.
    passcode = models.IntegerField(db_column='Passcode') # Field name made lowercase.
    uuid = models.CharField(max_length=108, db_column='UUID') # Field name made lowercase.
    version = models.IntegerField(db_column='Version') # Field name made lowercase.
    class Meta:
        db_table = u'mobileiosinstalledprofiles'

class Mobileiosprovisioningprofiles(models.Model):
    provprofid = models.IntegerField(primary_key=True, db_column='ProvProfID') # Field name made lowercase.
    mobileid = models.IntegerField(db_column='MobileID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    uuid = models.TextField(db_column='UUID') # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate') # Field name made lowercase.
    class Meta:
        db_table = u'mobileiosprovisioningprofiles'

class Mobilepermissions(models.Model):
    permid = models.IntegerField(primary_key=True, db_column='PermID') # Field name made lowercase.
    classid = models.IntegerField(primary_key=True, db_column='ClassID') # Field name made lowercase.
    permission = models.IntegerField(db_column='Permission') # Field name made lowercase.
    class Meta:
        db_table = u'mobilepermissions'

class Mobileschedules(models.Model):
    scheduleid = models.IntegerField(primary_key=True, db_column='ScheduleID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    updateconfigdow = models.IntegerField(db_column='UpdateConfigDow') # Field name made lowercase.
    updateconfigtod = models.IntegerField(db_column='UpdateConfigTod') # Field name made lowercase.
    updateconfiginterval = models.IntegerField(db_column='UpdateConfigInterval') # Field name made lowercase.
    systeminvdow = models.IntegerField(db_column='SystemInvDow') # Field name made lowercase.
    systeminvtod = models.IntegerField(db_column='SystemInvTod') # Field name made lowercase.
    systeminvinterval = models.IntegerField(db_column='SystemInvInterval') # Field name made lowercase.
    processscandow = models.IntegerField(db_column='ProcessScanDow') # Field name made lowercase.
    processscantod = models.IntegerField(db_column='ProcessScanTod') # Field name made lowercase.
    processscaninterval = models.IntegerField(db_column='ProcessScanInterval') # Field name made lowercase.
    softwareinvdow = models.IntegerField(db_column='SoftwareInvDow') # Field name made lowercase.
    softwareinvtod = models.IntegerField(db_column='SoftwareInvTod') # Field name made lowercase.
    softwareinvinterval = models.IntegerField(db_column='SoftwareInvInterval') # Field name made lowercase.
    hardwareinvdow = models.IntegerField(db_column='HardwareInvDow') # Field name made lowercase.
    hardwareinvtod = models.IntegerField(db_column='HardwareInvTod') # Field name made lowercase.
    hardwareinvinterval = models.IntegerField(db_column='HardwareInvInterval') # Field name made lowercase.
    class Meta:
        db_table = u'mobileschedules'

class Monitortemplates(models.Model):
    monitorid = models.IntegerField(primary_key=True, db_column='MonitorID') # Field name made lowercase.
    monitortemplateid = models.IntegerField(db_column='MonitorTemplateID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    checkaction = models.IntegerField(db_column='CheckAction') # Field name made lowercase.
    alertactionid = models.IntegerField(db_column='AlertActionID') # Field name made lowercase.
    alertmessage = models.TextField(db_column='AlertMessage') # Field name made lowercase.
    interval = models.IntegerField()
    where = models.CharField(max_length=765, db_column='Where') # Field name made lowercase.
    what = models.CharField(max_length=765, db_column='What') # Field name made lowercase.
    dataout = models.TextField(db_column='DataOut') # Field name made lowercase.
    comparor = models.IntegerField(db_column='Comparor') # Field name made lowercase.
    datain = models.CharField(max_length=600, db_column='DataIn') # Field name made lowercase.
    idfield = models.CharField(max_length=1500, db_column='IDField') # Field name made lowercase.
    alertstyle = models.IntegerField(db_column='AlertStyle') # Field name made lowercase.
    datacollector = models.CharField(max_length=300, db_column='DataCollector') # Field name made lowercase.
    category = models.IntegerField(db_column='Category') # Field name made lowercase.
    class Meta:
        db_table = u'monitortemplates'

class MsgQuestions(models.Model):
    questionid = models.IntegerField(primary_key=True, db_column='QuestionID') # Field name made lowercase.
    messageid = models.IntegerField(db_column='MessageID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    type = models.IntegerField(db_column='Type') # Field name made lowercase.
    body = models.CharField(max_length=1536, db_column='Body') # Field name made lowercase.
    typedata = models.TextField(db_column='TypeData') # Field name made lowercase.
    imageurl = models.CharField(max_length=765, db_column='ImageUrl') # Field name made lowercase.
    class Meta:
        db_table = u'msg_questions'

class MsgResponses(models.Model):
    responseid = models.IntegerField(primary_key=True, db_column='ResponseID') # Field name made lowercase.
    messageid = models.IntegerField(db_column='MessageID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    timesent = models.DateTimeField(db_column='TimeSent') # Field name made lowercase.
    timereceived = models.DateTimeField(db_column='TimeReceived') # Field name made lowercase.
    answer1 = models.CharField(max_length=765, db_column='Answer1') # Field name made lowercase.
    answer2 = models.CharField(max_length=765, db_column='Answer2') # Field name made lowercase.
    answer3 = models.CharField(max_length=765, db_column='Answer3') # Field name made lowercase.
    answer4 = models.CharField(max_length=765, db_column='Answer4') # Field name made lowercase.
    answer5 = models.CharField(max_length=765, db_column='Answer5') # Field name made lowercase.
    question1 = models.IntegerField(db_column='Question1') # Field name made lowercase.
    question2 = models.IntegerField(db_column='Question2') # Field name made lowercase.
    question3 = models.IntegerField(db_column='Question3') # Field name made lowercase.
    question4 = models.IntegerField(db_column='Question4') # Field name made lowercase.
    question5 = models.IntegerField(db_column='Question5') # Field name made lowercase.
    timescriptqueued = models.DateTimeField(db_column='TimeScriptQueued') # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted') # Field name made lowercase.
    username = models.CharField(max_length=300, db_column='UserName') # Field name made lowercase.
    console = models.IntegerField(db_column='Console') # Field name made lowercase.
    extraparams = models.CharField(max_length=765, db_column='ExtraParams') # Field name made lowercase.
    class Meta:
        db_table = u'msg_responses'

class Networkdrives(models.Model):
    driveid = models.IntegerField(primary_key=True, db_column='DriveID') # Field name made lowercase.
    computerid = models.IntegerField(unique=True, db_column='ComputerID') # Field name made lowercase.
    letter = models.CharField(max_length=6, unique=True, db_column='Letter') # Field name made lowercase.
    model = models.CharField(max_length=105, db_column='Model') # Field name made lowercase.
    user = models.CharField(max_length=90, db_column='User') # Field name made lowercase.
    class Meta:
        db_table = u'networkdrives'

class Orderparts(models.Model):
    orderpartid = models.IntegerField(db_column='OrderPartID') # Field name made lowercase.
    orderno = models.CharField(max_length=150, db_column='OrderNo') # Field name made lowercase.
    trackingno = models.CharField(max_length=600, db_column='TrackingNo') # Field name made lowercase.
    status = models.IntegerField(db_column='Status') # Field name made lowercase.
    distributor = models.CharField(max_length=150, db_column='Distributor') # Field name made lowercase.
    notes = models.CharField(max_length=600, db_column='Notes') # Field name made lowercase.
    class Meta:
        db_table = u'orderparts'

class Plugins(models.Model):
    pluginid = models.IntegerField(primary_key=True, db_column='PluginID') # Field name made lowercase.
    guid = models.CharField(max_length=108, unique=True, db_column='GUID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    version = models.CharField(max_length=150, db_column='Version') # Field name made lowercase.
    author = models.CharField(max_length=765, db_column='Author') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    icon = models.CharField(max_length=765, db_column='Icon') # Field name made lowercase.
    md5 = models.CharField(max_length=765, db_column='MD5') # Field name made lowercase.
    source = models.TextField(db_column='Source') # Field name made lowercase.
    filename = models.CharField(max_length=765, db_column='Filename') # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='ReleaseDate') # Field name made lowercase.
    enable = models.IntegerField(db_column='Enable') # Field name made lowercase.
    iisloaded = models.IntegerField(db_column='IISLoaded') # Field name made lowercase.
    agentloaded = models.IntegerField(db_column='AgentLoaded') # Field name made lowercase.
    exclusive = models.IntegerField(db_column='Exclusive') # Field name made lowercase.
    remoteagent = models.IntegerField(db_column='RemoteAgent') # Field name made lowercase.
    class Meta:
        db_table = u'plugins'


class ProbeEvents(models.Model):
    probeid = models.IntegerField(db_column='ProbeId') # Field name made lowercase.
    eventlevel = models.IntegerField(db_column='EventLevel') # Field name made lowercase.
    eventmessage = models.TextField(db_column='EventMessage') # Field name made lowercase.
    eventtime = models.DateTimeField(db_column='EventTime') # Field name made lowercase.
    class Meta:
        db_table = u'probe_events'

class Probealerts(models.Model):
    probealertid = models.IntegerField(primary_key=True, db_column='ProbeAlertID') # Field name made lowercase.
    probeid = models.IntegerField(db_column='ProbeID') # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID') # Field name made lowercase.
    failed = models.IntegerField(db_column='Failed') # Field name made lowercase.
    data = models.CharField(max_length=600, db_column='Data') # Field name made lowercase.
    failcount = models.IntegerField(db_column='FailCount') # Field name made lowercase.
    alertdate = models.DateTimeField(db_column='AlertDate') # Field name made lowercase.
    trapid = models.IntegerField(db_column='TrapID') # Field name made lowercase.
    syslogid = models.IntegerField(db_column='SyslogID') # Field name made lowercase.
    class Meta:
        db_table = u'probealerts'

class Probecommands(models.Model):
    cmdid = models.IntegerField(primary_key=True, db_column='CmdId') # Field name made lowercase.
    probeid = models.IntegerField(db_column='ProbeId') # Field name made lowercase.
    command = models.IntegerField(db_column='Command') # Field name made lowercase.
    parameters = models.TextField(db_column='Parameters') # Field name made lowercase.
    status = models.IntegerField(db_column='Status') # Field name made lowercase.
    output = models.TextField(db_column='Output') # Field name made lowercase.
    fasttalk = models.IntegerField(db_column='FastTalk') # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated') # Field name made lowercase.
    class Meta:
        db_table = u'probecommands'

class Probedetectionrules(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    rulenumber = models.IntegerField(primary_key=True, db_column='RuleNumber') # Field name made lowercase.
    rulename = models.CharField(max_length=765, db_column='RuleName', blank=True) # Field name made lowercase.
    rulecode = models.IntegerField(null=True, db_column='RuleCode', blank=True) # Field name made lowercase.
    arg1 = models.CharField(max_length=765, db_column='Arg1', blank=True) # Field name made lowercase.
    arg2 = models.CharField(max_length=765, db_column='Arg2', blank=True) # Field name made lowercase.
    arg3 = models.CharField(max_length=765, db_column='Arg3', blank=True) # Field name made lowercase.
    arg4 = models.CharField(max_length=765, db_column='Arg4', blank=True) # Field name made lowercase.
    isactive = models.IntegerField(null=True, db_column='IsActive', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'probedetectionrules'

class ProbeinternalStorageareas(models.Model):
    deviceid = models.IntegerField(primary_key=True, db_column='DeviceId') # Field name made lowercase.
    hrstorageindex = models.IntegerField(primary_key=True, db_column='hrStorageIndex') # Field name made lowercase.
    hrstoragetype = models.CharField(max_length=765, db_column='hrStorageType', blank=True) # Field name made lowercase.
    hrstoragedescr = models.CharField(max_length=765, db_column='hrStorageDescr', blank=True) # Field name made lowercase.
    hrstorageallocationunits = models.IntegerField(null=True, db_column='hrStorageAllocationUnits', blank=True) # Field name made lowercase.
    hrstoragesize = models.IntegerField(null=True, db_column='hrStorageSize', blank=True) # Field name made lowercase.
    hrstorageused = models.IntegerField(null=True, db_column='hrStorageUsed', blank=True) # Field name made lowercase.
    hrstorageallocationfailures = models.IntegerField(null=True, db_column='hrStorageAllocationFailures', blank=True) # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate') # Field name made lowercase.
    class Meta:
        db_table = u'probeinternal_storageareas'

class ProbeinternalSysteminfo(models.Model):
    deviceid = models.IntegerField(primary_key=True, db_column='DeviceId') # Field name made lowercase.
    sysdescr = models.CharField(max_length=765, db_column='SysDescr', blank=True) # Field name made lowercase.
    sysobjectid = models.CharField(max_length=765, db_column='SysObjectId', blank=True) # Field name made lowercase.
    sysuptime = models.CharField(max_length=765, db_column='SysUpTime', blank=True) # Field name made lowercase.
    syscontact = models.CharField(max_length=765, db_column='SysContact', blank=True) # Field name made lowercase.
    sysname = models.CharField(max_length=765, db_column='SysName', blank=True) # Field name made lowercase.
    syslocation = models.CharField(max_length=765, db_column='SysLocation', blank=True) # Field name made lowercase.
    sysservices = models.CharField(max_length=765, db_column='SysServices', blank=True) # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate') # Field name made lowercase.
    class Meta:
        db_table = u'probeinternal_systeminfo'

class Processes(models.Model):
    processid = models.BigIntegerField(primary_key=True, db_column='ProcessID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    name = models.CharField(max_length=60, db_column='Name') # Field name made lowercase.
    procid = models.IntegerField(db_column='ProcID') # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority') # Field name made lowercase.
    creationdate = models.CharField(max_length=90, db_column='CreationDate') # Field name made lowercase.
    procpath = models.CharField(max_length=300, db_column='ProcPath') # Field name made lowercase.
    cputime = models.IntegerField(db_column='CPUTime') # Field name made lowercase.
    memsize = models.BigIntegerField(db_column='MemSize') # Field name made lowercase.
    args = models.CharField(max_length=90, db_column='Args') # Field name made lowercase.
    modules = models.CharField(max_length=6000, db_column='Modules') # Field name made lowercase.
    last_date = models.DateTimeField(db_column='Last_date') # Field name made lowercase.
    class Meta:
        db_table = u'processes'


class Quickconnect(models.Model):
    fromid = models.CharField(max_length=3000, db_column='FromID') # Field name made lowercase.
    toid = models.CharField(max_length=3000, db_column='ToID') # Field name made lowercase.
    name = models.CharField(max_length=45, db_column='Name') # Field name made lowercase.
    message = models.CharField(max_length=765, db_column='Message') # Field name made lowercase.
    status = models.IntegerField(db_column='Status') # Field name made lowercase.
    ip = models.CharField(max_length=90, db_column='IP') # Field name made lowercase.
    port = models.CharField(max_length=30, db_column='Port') # Field name made lowercase.
    pass_field = models.CharField(max_length=9, db_column='Pass') # Field name made lowercase. Field renamed because it was a Python reserved word.
    requestdate = models.DateTimeField(db_column='RequestDate') # Field name made lowercase.
    class Meta:
        db_table = u'quickconnect'

class Reportcategory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=762, db_column='Name') # Field name made lowercase.
    icon = models.TextField(db_column='Icon') # Field name made lowercase.
    titletext = models.CharField(max_length=762, db_column='TitleText') # Field name made lowercase.
    class Meta:
        db_table = u'reportcategory'


class Statusitems(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    title = models.CharField(max_length=765, db_column='Title') # Field name made lowercase.
    basesql = models.CharField(max_length=3072, db_column='BaseSQL') # Field name made lowercase.
    computercolumn = models.CharField(max_length=765, db_column='ComputerColumn') # Field name made lowercase.
    dataviewid = models.CharField(max_length=765, db_column='DataViewID') # Field name made lowercase.
    class Meta:
        db_table = u'statusitems'

class Ticketpriority(models.Model):
    priority = models.IntegerField(primary_key=True, db_column='Priority') # Field name made lowercase.
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'ticketpriority'

class Tickets(models.Model):
    ticketid = models.IntegerField(primary_key=True, db_column='TicketID') # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID') # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectID') # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID') # Field name made lowercase.
    status = models.IntegerField(db_column='Status') # Field name made lowercase.
    subject = models.CharField(max_length=765, db_column='Subject') # Field name made lowercase.
    time = models.IntegerField(db_column='Time') # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    duedate = models.DateTimeField(null=True, db_column='DueDate', blank=True) # Field name made lowercase.
    starteddate = models.DateTimeField(db_column='StartedDate') # Field name made lowercase.
    contactdate = models.DateTimeField(db_column='ContactDate') # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate') # Field name made lowercase.
    requestoremail = models.CharField(max_length=300, db_column='RequestorEmail') # Field name made lowercase.
    ccemail = models.CharField(max_length=765, db_column='CCEmail') # Field name made lowercase.
    level = models.IntegerField(db_column='Level') # Field name made lowercase.
    category = models.IntegerField(db_column='Category') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID') # Field name made lowercase.
    externalid = models.IntegerField(db_column='ExternalID') # Field name made lowercase.
    guid = models.CharField(max_length=300, db_column='GUID') # Field name made lowercase.
    class Meta:
        db_table = u'tickets'

class Ticketstatus(models.Model):
    ticketstatusid = models.IntegerField(primary_key=True, db_column='TicketStatusID') # Field name made lowercase.
    ticketstatus = models.CharField(max_length=75, db_column='TicketStatus') # Field name made lowercase.
    class Meta:
        db_table = u'ticketstatus'

class VExtradataclients(models.Model):
    clientid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    additional_server_checks = models.TextField(db_column='Additional Server Checks') # Field renamed to remove spaces. Field name made lowercase.
    av_expiration_date = models.TextField(db_column='AV Expiration Date') # Field renamed to remove spaces. Field name made lowercase.
    av_license_key = models.TextField(db_column='AV License Key') # Field renamed to remove spaces. Field name made lowercase.
    av_password = models.TextField(db_column='AV Password') # Field renamed to remove spaces. Field name made lowercase.
    av_server_fqdn = models.TextField(db_column='AV Server FQDN') # Field renamed to remove spaces. Field name made lowercase.
    av_username = models.TextField(db_column='AV Username') # Field renamed to remove spaces. Field name made lowercase.
    cluster1___day_of_month = models.TextField(db_column='Cluster1 - Day of Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster1___day_of_week = models.TextField(db_column='Cluster1 - Day of Week') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster1___last_day_of_the_month = models.TextField(db_column='Cluster1 - Last Day of the Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster1___schedule_active = models.TextField(db_column='Cluster1 - Schedule Active') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster1___week_of_month = models.TextField(db_column='Cluster1 - Week of Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster1_to_patch = models.TextField(db_column='Cluster1 to Patch') # Field renamed to remove spaces. Field name made lowercase.
    cluster2___day_of_month = models.TextField(db_column='Cluster2 - Day of Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster2___day_of_week = models.TextField(db_column='Cluster2 - Day of Week') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster2___last_day_of_the_month = models.TextField(db_column='Cluster2 - Last Day of the Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster2___schedule_active = models.TextField(db_column='Cluster2 - Schedule Active') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster2___week_of_month = models.TextField(db_column='Cluster2 - Week of Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster2_to_patch = models.TextField(db_column='Cluster2 to Patch') # Field renamed to remove spaces. Field name made lowercase.
    cluster3___day_of_month = models.TextField(db_column='Cluster3 - Day of Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster3___day_of_week = models.TextField(db_column='Cluster3 - Day of Week') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster3___last_day_of_the_month = models.TextField(db_column='Cluster3 - Last Day of the Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster3___schedule_active = models.TextField(db_column='Cluster3 - Schedule Active') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster3___week_of_month = models.TextField(db_column='Cluster3 - Week of Month') # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    cluster3_to_patch = models.TextField(db_column='Cluster3 to Patch') # Field renamed to remove spaces. Field name made lowercase.
    daily_health_report = models.TextField(db_column='Daily Health Report') # Field renamed to remove spaces. Field name made lowercase.
    daily_report_email = models.TextField(db_column='Daily Report Email') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_client_name = models.TextField(db_column='Doyenz Client Name') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_high_band_limit = models.TextField(db_column='Doyenz High Band Limit') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_high_band_start_time = models.TextField(db_column='Doyenz High Band Start Time') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_low_band_limit = models.TextField(db_column='Doyenz Low Band Limit') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_low_band_start_time = models.TextField(db_column='Doyenz Low Band Start Time') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_backup_directory = models.TextField(db_column='Doyenz SP Backup Directory') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_backup_domain = models.TextField(db_column='Doyenz SP Backup Domain') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_backup_password = models.TextField(db_column='Doyenz SP Backup Password') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_backup_user = models.TextField(db_column='Doyenz SP Backup User') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_install_domain = models.TextField(db_column='Doyenz SP Install Domain') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_password = models.TextField(db_column='Doyenz SP Password') # Field renamed to remove spaces. Field name made lowercase.
    doyenz_sp_user = models.TextField(db_column='Doyenz SP User') # Field renamed to remove spaces. Field name made lowercase.
    enable_patching = models.TextField(db_column='Enable Patching') # Field renamed to remove spaces. Field name made lowercase.
    enable_windows_patching = models.TextField(db_column='Enable Windows Patching') # Field renamed to remove spaces. Field name made lowercase.
    gateway_ip_address = models.TextField(db_column='Gateway IP Address') # Field renamed to remove spaces. Field name made lowercase.
    hot_fix_window = models.TextField(db_column='Hot Fix Window') # Field renamed to remove spaces. Field name made lowercase.
    ip_range = models.TextField(db_column='IP Range') # Field renamed to remove spaces. Field name made lowercase.
    isp_dns_servers = models.TextField(db_column='ISP DNS Servers') # Field renamed to remove spaces. Field name made lowercase.
    lt_backup_server_key = models.TextField(db_column='LT Backup Server Key') # Field renamed to remove spaces. Field name made lowercase.
    lt_backup_workstation_key = models.TextField(db_column='LT Backup Workstation Key') # Field renamed to remove spaces. Field name made lowercase.
    monitoring_dns_name = models.TextField(db_column='Monitoring DNS Name') # Field renamed to remove spaces. Field name made lowercase.
    monthly_health_report = models.TextField(db_column='Monthly Health Report') # Field renamed to remove spaces. Field name made lowercase.
    monthly_report_email = models.TextField(db_column='Monthly Report Email') # Field renamed to remove spaces. Field name made lowercase.
    nod32_config_file = models.TextField(db_column='NOD32 Config File') # Field renamed to remove spaces. Field name made lowercase.
    server_failed_action = models.TextField(db_column='Server Failed Action') # Field renamed to remove spaces. Field name made lowercase.
    servers_under_contract = models.TextField(db_column='Servers Under Contract') # Field renamed to remove spaces. Field name made lowercase.
    skip_missing_virus_scanner = models.TextField(db_column='Skip Missing Virus Scanner') # Field renamed to remove spaces. Field name made lowercase.
    smart_host = models.TextField(db_column='Smart Host') # Field renamed to remove spaces. Field name made lowercase.
    subnet_mask = models.TextField(db_column='Subnet Mask') # Field renamed to remove spaces. Field name made lowercase.
    vpro_pass = models.TextField(db_column='vPro Pass') # Field renamed to remove spaces. Field name made lowercase.
    website_address = models.TextField(db_column='WebSite Address') # Field renamed to remove spaces. Field name made lowercase.
    weekly_health_report = models.TextField(db_column='Weekly Health Report') # Field renamed to remove spaces. Field name made lowercase.
    weekly_report_email = models.TextField(db_column='Weekly Report Email') # Field renamed to remove spaces. Field name made lowercase.
    workstations_failed_action = models.TextField(db_column='Workstations Failed Action') # Field renamed to remove spaces. Field name made lowercase.
    workstations_under_contract = models.TextField(db_column='Workstations Under Contract') # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'v_extradataclients'

