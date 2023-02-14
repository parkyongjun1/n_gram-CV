# Simple-NGram
Analysis of 2020 Accepted Papers(ACCV,CVPR, ECCV, WACV) using N-Gram

## Usage
```python
NGram(paper_2020_list).ngram(2).gram_freq_sorted[:10]
```
```[('machine translation', 83),
 ('object detection', 59),
 ('image classification', 59),
 ```
```python
NGram(paper_2020_list,2).showTitles('object detection')[:3]
```
```
['EfficientDet: Scalable and Efficient Object Detection']
```
 
## License
whitepurple, MIT License
