import lldb

#used like this
#(lldb) command script import ~/lldb/inGivenFrame.py
#(lldb) br s -l codeline
#(lldb) br comm add --script-type python -o "inGivenFrame.inGivenFrame(frame,bp_loc,'givenfuncname')" 1
#(lldb) br comm add --script-type python -F inGivenFrame.inGivenFrameF 1

def inGivenFrame(frame,location,givenFrameName):
	thread = frame.GetThread()
	process = thread.GetProcess()
	#process.Continue()
	#print location
	bIsInGivenFrame = False
	for upperframe in thread.frames:
		if upperframe.GetFunctionName() == givenFrameName:
			bIsInGivenFrame = True
			break
	if bIsInGivenFrame != True:
		process.Continue()
		
def inGivenFrameF(frame,location,unused):
	framename = '-[UITableView _performWithCachedTraitCollection:]'
	thread = frame.GetThread()
	process = thread.GetProcess()
	bIsInGivenFrame = False
	for upperframe in thread.frames:
		print upperframe.GetFunctionName()
		if upperframe.GetFunctionName() == framename:
			print 'in the given frame'
			bIsInGivenFrame = True
			break
	if bIsInGivenFrame != True:
		process.Continue()

