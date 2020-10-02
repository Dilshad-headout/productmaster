from django.db import models
from django.contrib.auth.models import User

list_type = (
    ('null', '---'),
    ('Existing EC Update', 'Existing EC Update'),
    ('New EC Launch', 'New EC Launch'),
    ('Category Revamp', 'Category Revamp'),
)
urgency_type = (
    ('null', '---'),
    ('Urgent', 'Urgent (Within 1 working day)'),
    ('High', 'High (Within 2 working days)'),
    ('Medium', 'Medium (Within 4 working days)'),
    ('Low', 'Low (Within 6 working days)'),
)

listing_issues_types = (
    ('null', '---'),
    ('SP On-boarding Pending', 'SP On-boarding Pending'),
    ('SP Automation Pending', 'SP Automation Pending'),
    ('Product Link not working', 'Product Link not working'),
)
listing_status_types = (
    ('null', '---'),
    ('Live and Audited', 'Live and Audited'),
    ('In Progress', 'In Progress'),
    ('Blocked', 'Blocked')
)
class ListingMember(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    def no_of_listing(self):
        listings = Product.objects.filter(listing_poc=self)
        return len(listings)

class Product(models.Model):
    city = models.CharField("City", max_length=20, blank=False, null=False)
    category_name = models.CharField("Category Name", max_length=255, blank=False, null=False)
    tgid = models.IntegerField( blank=False, null=False)
    product_name = models.CharField("Product Name", max_length=255, blank=False, null=False)
    tid = models.IntegerField(blank=False, null=False)
    variant_name = models.CharField("Variant Name", max_length=20, blank=False, null=False)
    listing_type = models.CharField(max_length=25, choices=list_type, default='null')
    frame_work_url = models.URLField("Frame Work Sheet URL", max_length=100, blank=False, null=False)
    trello_link = models.URLField("Trello Link", max_length=100, blank=False, null=False)
    urgency = models.CharField(max_length=50, choices=urgency_type, default='null')
    #one to many
    # listing_poc = models.CharField(max_length=25, choices=listing_members, default='null')
    listing_poc = models.ForeignKey(ListingMember,on_delete=models.PROTECT,related_name='listing_members')

    listing_issue = models.CharField(max_length=25, choices=listing_issues_types, default='null')
    listing_status = models.CharField(max_length=25, choices=listing_status_types, default='null')
    Comments = models.TextField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    # user = models.ForeignKey(User)
    def __str__(self):
        return self.product_name

class BusinessOwner(models.Model):
    business_owner = models.CharField("Business Owner", max_length=255, blank=False, null=False)
    # one to one
    product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.PROTECT)