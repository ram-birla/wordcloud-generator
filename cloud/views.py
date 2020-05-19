from django.shortcuts import render,redirect
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from django.contrib import messages
import io
import sys
from . models import Wrdcloud,Simple
from os import path, getcwd
import datetime
# Create your views here.
def homePage(req):
    return render(req,'home.html')

def maker(req):
    return render(req,'maker.html')

def creator(req):
    return render(req,'creator.html')

def make(req):
    try:
        if req.method == 'POST' and req.FILES['shape'] and req.FILES['txt']:
            try:
                color = req.POST.get('color')
                wdth = req.POST.get('width')
                hight = req.POST.get('height')
                shpe = req.FILES['shape']
                text = req.FILES['txt']
                txt = text.read().decode("utf-8")
                print(color, hight,wdth, shpe, text,txt )
                
                fname = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                file_name = fname+"."+text.name.split(".")[1]
                img_name = fname+"."+shpe.name.split(".")[1]
                if text and shpe is not None:
                    wrd = Wrdcloud(text=text,image=shpe)
                    wrd.image.name = img_name
                    wrd.text.name = file_name
                    print(wrd.image)
                    wrd.save()
                
                punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

                non_punctuation_text=""
                for char in txt:
                    if char not in punctuations:
                        non_punctuation_text=non_punctuation_text+char
                # for i in text:
                print(non_punctuation_text)
                #     print(i)
                stopwords = set(STOPWORDS)
                stopwords.update(["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
                "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
                "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
                "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","after"])
                print("-1")
                d = getcwd()
                print("-0.75")
                b = "./media/cloud/image/"+ img_name
                print(b)
                # a = Wrdcloud.objects.all()
                # for i in a:
                #     print(i.text,i.image)
                mask = np.array(Image.open(path.join(d, b)))
                wordcloud = WordCloud(stopwords= STOPWORDS,max_font_size=150, width=int(wdth), height=int(hight),max_words=1000, mask=mask, background_color=color).generate(non_punctuation_text)
                
                # print(a)
                image_colors = ImageColorGenerator(mask)
                plt.figure(figsize = [20,10])
                
                a = plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
                
                plt.axis("off")
                plt.savefig('./media/cloud/result/'+img_name)
                # wordcloud.to_file('./m/im/graph.png')
                # path="/m/im/graph.png"
                # wrd = Wrdcloud(text=)
                p = img_name
                ww = Wrdcloud.objects.get(image__endswith=img_name)
                ww.cloud = '/media/cloud/result/'+img_name
                ww.save()
                return render(req,'wordcloud.html',{'plot':p,'h':hight,'w':wdth})
            except:
                a = Wrdcloud.objects.get(image__endswith=img_name)
                a.delete()
                msg = "Something went wrong. Some Tips: Check Color name, use Color Code For Appropriate background colors. Check your files, upload right files at right place. If Your Wordcloud id not appropriate with masked ,try another images/Shape. Try again!!"
                
                messages.info(req,msg)
                return redirect('/maker')
        else:
            messages.info(req,'Fill Out the form Properly')
            return redirect('/maker')

    except:
        messages.info(req,'Fill Out the form Properly')
        return redirect('/maker')


def simple(req):
    try:
        if req.method == 'POST' and req.FILES['txt']:
            try:
                color = req.POST.get('color')
                wdth = req.POST.get('width')
                hight = req.POST.get('height')
                max_size = req.POST.get('max')
                text = req.FILES['txt']
                txt = text.read().decode("utf-8")
                print(color, hight, wdth, text,txt )
                
                fname = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                file_name = fname+"."+text.name.split(".")[1]
                smp = Simple(text=text)
                if text is not None:
                    smp.text.name = file_name
                    smp.save()
                punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                

                non_punctuation_text=""
                for char in txt:
                    if char not in punctuations:
                        non_punctuation_text=non_punctuation_text+char
                # for i in text:
                print(non_punctuation_text)
                #     print(i)
                stopwords = set(STOPWORDS)
                stopwords.update(["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
                "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
                "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
                "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","after"])
                print("-1")
                # d = getcwd()
                print("-0.75")
                # b = "./media/cloud/image/"+ img_name
                # print(b)
                # a = Wrdcloud.objects.all()
                # for i in a:
                #     print(i.text,i.image)
                # mask = np.array(Image.open(path.join(d, b)))
                wordcloud = WordCloud(stopwords= STOPWORDS,max_font_size=int(max_size),width=int(wdth),height=int(hight), max_words=1000, background_color=color).generate(non_punctuation_text)
                
                # print(a)
                # image_colors = ImageColorGenerator(mask)
                plt.figure(figsize = [20,10])
                
                plt.imshow(wordcloud, interpolation="bilinear")
                
                plt.axis("off")
                img_name = fname+".png"
                
                plt.savefig('./media/cloud/result/'+img_name)
                # wordcloud.to_file('./m/im/graph.png')
                # path="/m/im/graph.png"
                # wrd = Wrdcloud(text=)
                p = img_name
                ss = Simple.objects.get(text__endswith=file_name)
                ss.cloud = '/media/cloud/result/'+img_name
                ss.save()
                return render(req,'wordcloud.html',{'plot':p,'h':hight,'w':wdth})
            except:
                a = Simple.objects.get(text__endswith=file_name)
                a.delete()
                msg = "Something went wrong. Some Tips: Check Color name, use Color Code For Appropriate background colors. Check your files, upload right files at right place. If Your Wordcloud id not appropriate with masked ,try another images/Shape. Try again!!"
                
                messages.info(req,msg)
                return redirect('/maker')
        else:
            messages.info(req,'Fill Out the form Properly')
            return redirect('/maker')

    except:
        messages.info(req,'Fill Out the form Properly')
        return redirect('/maker')


def gallery(req):
    mask = Wrdcloud.objects.all()
    simple = Simple.objects.all()
    return render(req,'gallery.html',{'mask':mask,'simple':simple})

