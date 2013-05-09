from django.db import models

# Create your models here.
class WorkColor(models.Model):
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()
    intvalue = models.IntegerField(unique=True, db_index=True)
    hexvalue = models.CharField(max_length=8)

class Work(models.Model):
    accessionNumber = models.CharField("accession number", max_length=255, db_index=True)
    artist = models.CharField(max_length=255, db_index=True)
    catalogueEntry = models.CharField("catalogue entry", max_length=255)
    catalogueRaisonne = models.CharField("catalogue raisonne", max_length=255)
    classification = models.CharField(max_length=255)
    creditLine = models.CharField("credit line", max_length=255)
    culture = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    designer = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)

    # Relationships
    dominantcolor = models.ManyToManyField(WorkColor, verbose_name="dominant color", related_name="work_dominant_colors")
    mostsaturated = models.ManyToManyField(WorkColor, verbose_name="most saturated color", related_name="work_mostsaturated_colors")
    palette = models.ManyToManyField(WorkColor, related_name="work_palette_colors")
    searchbycolors = models.ManyToManyField(WorkColor, verbose_name="search by colors", related_name="work_searchby_colors")

    dynasty = models.CharField(max_length=255)
    galleryLabel = models.CharField("gallery label", max_length=255)
    geography = models.CharField(max_length=255)
    imageUrl = models.URLField("image url")
    imgfilename = models.CharField("image filename", max_length=255)
    markings = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    provenance = models.CharField(max_length=255)
    reign = models.CharField(max_length=255)
    rightsReproduction = models.CharField("rights reproduction", max_length=255)
    title = models.CharField(max_length=255,  blank=False)
    workid = models.IntegerField(blank=False, unique=True)
    workurl = models.URLField("work url", blank=False, unique=True)

#could these 3 models be thought of a polymorphic?
class ExhibitionHistory(models.Model):
    entry = models.TextField()
    work = models.ForeignKey(Work)

class Notes(models.Model):
    entry = models.TextField()
    work = models.ForeignKey(Work)

class References(models.Model):
    entry = models.TextField()
    work = models.ForeignKey(Work)