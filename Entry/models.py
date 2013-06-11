from django.db import models

# Create your models here.
class WorkColor(models.Model):
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()
    intvalue = models.IntegerField(unique=True, db_index=True)
    hexvalue = models.CharField(max_length=8)

    def natural_key(self):
        return {'red': self.red, 'green': self.green, 'blue': self.blue, 'hex': self.hexvalue}

class Work(models.Model):
    accessionNumber = models.CharField("accession number", max_length=255, db_index=True)
    artist = models.TextField(db_index=True)
    catalogueEntry = models.TextField("catalogue entry")
    catalogueRaisonne = models.TextField("catalogue raisonne")
    classification = models.CharField(max_length=255)
    creditLine = models.TextField("credit line")
    culture = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField()
    designer = models.CharField(max_length=255)
    dimensions = models.TextField()

    # Relationships
    dominantcolor = models.ManyToManyField(WorkColor, verbose_name="dominant color", related_name="work_dominant_colors")
    mostsaturated = models.ManyToManyField(WorkColor, verbose_name="most saturated color", related_name="work_mostsaturated_colors")
    palette = models.ManyToManyField(WorkColor, related_name="work_palette_colors")
    searchbycolors = models.ManyToManyField(WorkColor, verbose_name="search by colors", related_name="work_searchby_colors")

    dynasty = models.CharField(max_length=255)
    galleryLabel = models.TextField("gallery label")
    geography = models.CharField(max_length=255)
    imageUrl = models.URLField("image url")
    imgfilename = models.CharField("image filename", max_length=255)
    markings = models.TextField()
    medium = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    provenance = models.TextField()
    reign = models.CharField(max_length=255)
    rightsReproduction = models.TextField("rights reproduction")
    title = models.TextField(blank=False)
    workid = models.IntegerField(blank=False, unique=True)
    workurl = models.URLField("work url", blank=False, unique=True)

    def get_dominant_color(self):
        return self.dominantcolor.get()

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