# Myanmar Names 

<p>This is the simple repository to convert the names from Myanmar written in <b>Burmese</b> language to English and vice versa.</p>
<p>Currently only the dictionary based conversion method is used. The method is that at first, the name written in Burmese is segmented into <b>syllable</b> level and then these syllable words are converted into equivalent <b>English word</b> by the <b>dictionary</b> built from the <b>dataset</b> for Burmese to English conversion(Check <b>EDA</b> notebook for building dictionary). For <b>English to Burmese</b> syllable conversion, the same method is used.</p>

<p>Currently the dictionary based conversion has several weakness and the result is not satisfactory. The json file needs manual checking for best accuracy. I will do some research and add more methods to get the best result.</p>


## Usage

```Python
from mm_names.convert import mm2en, en2mm

print(mm2en("မင်းခန့်မောင်မောင်")) 
## 'min khant maung maung'

print(en2mm("Min Khant Maung Maung"))
## 'မင်း ခန့် မောင် မောင်'
```

## Acknowledgment

I use the [data](https://github.com/ye-kyaw-thu/myRoman/blob/main/person-name/person-name.ver1.0.txt) from Sayar <b>Ye Kyaw Thu repo</b> and I inspired the work from <b>Ko Htain Linn Shwe's [repo]</b>(https://github.com/saturngod/myanmar_names). I also used Burmese syllable segmentation code from Sayar Ye Kyaw Thu's [code](https://github.com/ye-kyaw-thu/myWord/blob/main/syl_segment.py). 

<p>I just make some EDA and want to do some improvment for name conversion method.</p>

## References

Ko Htain Linn Shwe's repo, https://github.com/saturngod/myanmar_names

The dataset from Sayar Ye Kyaw thu, https://github.com/ye-kyaw-thu/myRoman/blob/main/person-name/person-name.ver1.0.txt

Syllable segmentation, https://github.com/ye-kyaw-thu/myWord/blob/main/syl_segment.py




