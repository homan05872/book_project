from urllib import response
from django.test import TestCase
from book.models import Book,Review,Profiel,User
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve 
from .. import views
from django.shortcuts import render, redirect
from book import forms


class Form_test(TestCase):
    def test_BookForm_form(self):
        """BookFormテスト"""
        test_book = {"bookname": 'testbook', "subtitle": "testtitle","text": "testtext", "category": "ビジネス" }
        form = views.BookForm(test_book)
        self.assertTrue(form.is_valid())
        
    def test_Review_form(self):
        """ReviewFormテスト"""
        test_review = {"text": 'testtext', "rate": 1 }
        form = views.ReviewForm(test_review)
        self.assertTrue(form.is_valid())
        
    def test_emp_form(self):
        """BookNameSearchテスト"""
        test_book = {"bookname": 'testbook'}
        form = views.BookNameSearch(test_book)
        self.assertTrue(form.is_valid())
        
    def test_emp_form(self):
        """SubtitleSearchテスト"""
        test_book = {"subtitle": "testtitle"}
        form = views.SubtitleSearch(test_book)
        self.assertTrue(form.is_valid())