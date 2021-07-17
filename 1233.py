# 1233	Remove Sub-Folders from the Filesystem

class Solution:
  # v2
  def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        folders_filtered = [folder[0]]
        prev_folder = folder[0] + '/'
        for f in folder[1:]:
            if not f.startswith(prev_folder):
                folders_filtered.append(f)
                prev_folder = f + '/'
            
        return folders_filtered
  
  # v1
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders_filtered = set()
        folder = sorted(folder, key = lambda x : x.count('/'))
        
        for f in folder:
            flist = f.split('/')
            higher_folder = [flist[0]]
            subfolder = False
            for i in range(1, len(flist)):
                if '/'.join(higher_folder) in folders_filtered:
                    subfolder = True
                    break
                else:
                    higher_folder.append(flist[i])
            if subfolder == False:
                folders_filtered.add('/'.join(higher_folder))
            
        return folders_filtered
