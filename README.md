# Augmentor

对代码进行了修改, 修改原因如下:

1. 该工具对原始图像进行随机抽取, 可能会有部分原始图像数据被遗漏

   [augmentor_images = [random.choice(self.augmentor_images) for _ in range(n)]](https://github.com/mdbloice/Augmentor/blob/e41755431e725dd88155de1fa7ee356ac0a9583c/Augmentor/Pipeline.py#L358)

2. 对每个图像后没有保留相应的处理方式, 且与原始图像不能一一对应

   [file_name = str(uuid.uuid4())](https://github.com/mdbloice/Augmentor/blob/e41755431e725dd88155de1fa7ee356ac0a9583c/Augmentor/Pipeline.py#L239)



增加了接口:

```python
p = Augmentor.Pipeline(source_directory, output_directory)
p.random_distortion(1.0, 5, 15, 3) # 更改了接口
p.increase(5) # 增加了接口, 将数据增加5倍
```

