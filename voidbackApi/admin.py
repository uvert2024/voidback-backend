from django.contrib import admin
from .models import (
    Account,
    OneTimePassword,
    Post,
    PostImage,
    PostImpression,
    PostMetadata,
    Symbol,
    Hashtag,
    ForYou,
    Follow,
    SearchQuery,
    Report,
    InboxMessage,
    ResearchPaper,
    ResearchPaperImpression,
    Notification,
    PlatformMessage,
    PlatformMessageImpression
)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin


admin.site.unregister(Group)



@admin.register(Account)
class UserAdmin(ModelAdmin):
    search_fields = ['username', 'full_name', 'id']


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass




@admin.register(Post)
class PostAdmin(ModelAdmin):
    search_fields = ['id']
    sortable_by = ['id']



@admin.register(PostImage)
class PostImageAdmin(ModelAdmin):
    pass


@admin.register(PostImpression)
class PostImpressionAdmin(ModelAdmin):
    search_fields = ['post__id', "account__username"]


@admin.register(PostMetadata)
class PostMetadataAdmin(ModelAdmin):
    search_fields = ['post__id']


@admin.register(Symbol)
class SymbolAdmin(ModelAdmin):
    search_fields = ['symbol']


@admin.register(Hashtag)
class HashtagAdmin(ModelAdmin):
    search_fields = ['hashtag']


@admin.register(ForYou)
class ForYouAdmin(ModelAdmin):
    search_fields = ['account__username']


@admin.register(Follow)
class FollowAdmin(ModelAdmin):
    search_fields = ['follower__username', 'following__username']


@admin.register(SearchQuery)
class SearchQueryAdmin(ModelAdmin):
    search_fields = ['query']


@admin.register(Report)
class ReportAdmin(ModelAdmin):
    search_fields = ['object_type', 'resolved_by__username']
    ordering = ['resolved', '-priority', '-disturbance']




@admin.register(ResearchPaper)
class ResearchPaperAdmin(ModelAdmin):
    search_fields = ['title', 'author__username']



@admin.register(ResearchPaperImpression)
class ResearchPaperImpressionAdmin(ModelAdmin):
    search_fields = ['paper__title', 'impression', 'account__username']



@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    search_fields = ['account__username']



@admin.register(PlatformMessage)
class PlatformMessageAdmin(ModelAdmin):
    search_fields = ['title']


@admin.register(PlatformMessageImpression)
class PlatformMessageImpressionAdmin(ModelAdmin):
    search_fields = ['message__title', 'account__username']





