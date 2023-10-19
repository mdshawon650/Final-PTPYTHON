from django.http import HttpResponse
from django.shortcuts import render

blog_post = [
    {
        'title': "ভালো শুরুর পরও বাংলাদেশ ২৫৬",
        'content': "ঊরুর চোটের কারণে ম্যাচটা খেলছেন না সাকিব আল হাসান। তাতে বিশ্বকাপের মঞ্চে বাংলাদেশ দলকে নেতৃত্ব দেওয়ার সুযোগ আসে নাজমুল হোসেনের। পুনের ব্যাটিং স্বর্গে টস ভাগ্য গেছে তাঁর পক্ষেই।",
        'author': "লিটন",
        'post_create_date': " ১৯ অক্টোবর ২০২৩"
    },
    {
        'title': "রবি শাস্ত্রীর মন্তব্য কি তাতাবে আফ্রিদিকে",
        'content': "এবারের বিশ্বকাপটা মোটেও ভালো যাচ্ছে না শাহিন শাহ আফ্রিদির। এমনকি গত মাসে শ্রীলঙ্কা আর পাকিস্তানে অনুষ্ঠিত এশিয়া কাপেও তিনি খুব একটা ভালো করতে পারেননি। চোটের কারণে দীর্ঘ বিরতিটা কি তাঁর বোলিংয়ে মরচে ধরিয়ে দিল! এমন প্রশ্ন উঠছে।",
        'author': "শাহিন শাহ আফ্রিদি",
        'post_create_date': " ১৯ অক্টোবর ২০২৩"
    }
]


def home(request):
    return render(request, 'blog/home.html', {'blog_post': blog_post})


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})
