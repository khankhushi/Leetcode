class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        
        fdirs = path.split('/')
        for fd in fdirs:
            if fd:
                if fd == "..":
                    if path_stack:
                        path_stack.pop()
                elif fd == ".":
                    continue
                else:
                    path_stack.append(fd)
        
        ans = "/"
        if path_stack:
            ans += "/".join(path_stack)
            
        return ans
    
        