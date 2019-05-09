class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        folderName = ''
        lastChar = ''
        path += '/'
        for i in range(len(path)):
            if path[i] == '/':
                if lastChar == '/' or lastChar == '':
                    pass
                else:
                    if len(folderName) > 0: 
                        if folderName == '.':
                            pass
                        elif folderName == '..':
                            if len(dirs) > 0: dirs.pop()
                        else:
                            dirs.append(folderName)
                    folderName = ''
            else:
                folderName += path[i]
            lastChar = path[i]
        
        pathStr = ''
        for i in range(len(dirs)):
            pathStr += '/' + dirs[i]
        
        return pathStr if pathStr != '' else '/'