import os
import shutil
import filecmp
import warnings

import paste.script.command

here_cross = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

def paster(cmd):
    print "paster %s" % cmd
    from paste.script import command
    args = cmd.split()
    options, args = command.parser.parse_args(args)
    options.base_parser = command.parser
    command.system_plugins.extend(options.plugins or [])
    commands = command.get_commands()
    command_name = args[0]
    if command_name not in commands:
        command = command.NotFoundCommand
    else:
        command = commands[command_name].load()
    runner = command(command_name)
    runner.run(args[1:])

def listdir(path):
    """Like os.listdir with '.svn' filter"""

    return [f for f in os.listdir(path) if f not in (('.svn',))]

def isFolderContentEqual(a, b):
    len_a = len(a)
    for root, dirs, files in os.walk(a):
        folder_part = root[len_a:].strip(os.path.sep)
        
        if not os.path.exists(os.path.join(b, folder_part)):
            warnings.warn("%s not exists" % (os.path.join(b, folder_part)))
            return False

        # Compare files and directory
        if listdir(root) != listdir(os.path.join(b, folder_part)):
            warnings.warn("%s != %s" % (listdir(root), listdir(os.path.join(b, folder_part))))
            return False
        
        # Compare files contents
        for f in files:
            if not filecmp.cmp(
                os.path.join(b, folder_part, f),
                os.path.join(root, f)
            ):
                warnings.warn("%s != %s" % (os.path.join(b, folder_part, f), os.path.join(root, f)))
                return False

    return True

def createPackage(package_name, buildout):
    tmp = here_cross(('tmp',))

    if os.path.isdir(tmp):
        shutil.rmtree(tmp)

    cmd = 'create -t advanced_package %s package=%s version= description= long_description= keywords= author= author_email= url= license_name= zip_safe= buildout=%s -o %s' % (package_name, package_name, buildout, tmp)
    paster(cmd)


    assert isFolderContentEqual(
        os.path.join(tmp, package_name),
        here_cross((package_name, ))
    )

    if os.path.isdir(tmp):
        shutil.rmtree(tmp)

def testMyNameSpace():
    createPackage(package_name = "my.name.space", buildout = "")

def testSimpleWithBuildout():
    createPackage(package_name = "simple_with_buildout", buildout = "True")
