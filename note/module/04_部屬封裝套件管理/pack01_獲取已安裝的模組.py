import pkg_resources

def test1():
    installed_packages = pkg_resources.working_set
    # installed_packages_list = sorted([f'{i.key} {i.version}' for i in installed_packages])
    # print(installed_packages_list)

    installed_packages_list = sorted([e.key for e in installed_packages])
    print(installed_packages_list)
    
if __name__ == '__main__':
    test1()