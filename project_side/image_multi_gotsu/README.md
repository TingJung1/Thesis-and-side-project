## Archived this repo
This repo has too much raw data, takes forever to clone

Migrate to [image_multi_thresholds](https://github.com/ComputationalAgronomy/image_multi_thresholds)


## Issues with BFG

Errors after BFG clean up raw data here.
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

```bash
$ git push -f
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ComputationalAgronomy/image_analyze.git
 ! [remote rejected] refs/pull/1/head -> refs/pull/1/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/10/head -> refs/pull/10/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/19/head -> refs/pull/19/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/2/head -> refs/pull/2/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/20/head -> refs/pull/20/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/23/head -> refs/pull/23/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/3/head -> refs/pull/3/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/4/head -> refs/pull/4/head (deny updating a hidden ref)
 ! [remote rejected] refs/pull/5/head -> refs/pull/5/head (deny updating a hidden ref)
branch 'main' set up to track 'origin/main'.
error: failed to push some refs to 'https://github.com/ComputationalAgronomy/image_analyze.git'

```


```python
##alg_apr_多核使用方法
#選擇cpu數目
cpus = 8
#載入套件
import multiprocessing as mp
import logging
from datetime import datetime
import os
import pickle

def setup_logger():
    now = datetime.now().strftime("%y%m%d%H%M%S")
    logger = logging.getLogger("download_logging")
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s\t[%(levelname)s]\t%(message)s",
                                "%Y-%m-%d %H:%M:%S")
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = logging.FileHandler(os.path.join(os.path.dirname(__file__), f"logging_{now}.txt"), mode="a")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

#選擇需要的版本GOTSU_版本
#放入路徑位置image1
#選擇雜訊量 雜訊值
#選擇otsu計算範圍
#輸出otsu與gotsu得到的閾值
def job_1(i):
    g= GOTSU_GV_w()
    g.read_folder(image1)
    g.datasets = Clean_data.add_single_photo_noise(g.datasets,20000,116,i,1)
    g.otsu_instance()
    g.global_objective_scanning(100,130)
    start_list = heristic_algorithm.store_the_otsu_information(g.datasets,g.G_all)   
    b107o.append(start_list)  
    abc = start_list.copy()
    result = heristic_algorithm.heristic_model_otsu_random_start(g,g.datasets,abc)
    b107.append(result)   
    logger.info(f"{i} is completed")   
    return {"b107": result, "b107o": start_list}


logger = setup_logger()
if __name__ == "__main__":
    logger.info("Start running jobs")
    with mp.Pool(cpus) as pool:
        results = pool.map(job_1, range(25))
    summary = []
    summary1 = [] 
    for idx, result in enumerate(results):
        summary.append(result["b107"][idx])
        summary1.append(result["b107o"][idx])    

    print(summary)
    print(summary1)      
    
#alg用法
#建立路經
record = []    
record1 = []
image1 = "C:/Users/user/Desktop/middle_term_mean"
#選擇GOTSU
g= GOTSU_GV()
#photos 迴圈 重複進行幾次
#選擇雜訊量 雜訊值
#選擇otsu計算範圍
#輸出otsu與gotsu得到的閾值
for i in range(photos):
    g= GOTSU_GV_w()
    g.read_folder(image1)
    g.datasets = Clean_data.add_single_photo_noise(g.datasets,20000,106,i,1)
    g.otsu_instance()
    g.global_objective_scanning(100,130)
    list = heristic_algorithm.store_the_otsu_information(g.datasets,g.G_all)
    result = heristic_algorithm.heristic_model_otsu_random_start(g,g.datasets,list)
    record.append(result)
    
    
##有設定pytest 測試是否有演算法計算錯誤
```
