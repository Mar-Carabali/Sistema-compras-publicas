from django.db import models
from django.contrib.auth.models import User
from django.core.validators import DecimalValidator


class Csv(models.Model):
    file_name = models.FileField(upload_to="csvs")
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

class Premios(models.Model):
    ocid = models.CharField(max_length=600, null=True)
    release_id = models.CharField(max_length=600, null=True)
    id = models.CharField(primary_key=True, max_length=600 )
    title = models.CharField(max_length=600, null=True)
    description = models.CharField(max_length=600, null=True)
    status = models.CharField(max_length=600, null=True)
    date = models.CharField(max_length=600, null=True)
    amount = models.FloatField(null=True)
    currency = models.CharField(max_length=20, null=True)
    correctedValue_amount = models.CharField(max_length=20, null=True)
    correctedValue_currency = models.CharField(max_length=20, null=True)
    enteredValue_amount = models.CharField(max_length=20, null=True)
    enteredValue_currency =  models.CharField(max_length=20, null=True)
    contractPeriod_startDate =models.CharField(max_length=600, null=True, blank=True)
    contractPeriod_endDate = models.CharField(max_length=600,null=True, blank=True)
    contractPeriod_maxExtentDate = models.CharField(max_length=600,null=True)
    contractPeriod_durationInDays = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.ocid}"


class Contratos(models.Model):
    ocid = models.CharField(max_length=600, null=True)
    release_id = models.CharField(max_length=600, null=True)
    id = models.CharField(primary_key=True, max_length=600 )
    awardID = models.CharField(max_length=600, null=True)
    title = models.CharField(max_length=600, null=True)
    description = models.CharField(max_length=600, null=True)
    status = models.CharField(max_length=60, null=True)
    contractPeriod_startDate = models.CharField(max_length=100, null=True)
    contractPeriod_endDate = models.CharField(max_length=600,null=True)
    contractPeriod_maxExtentDate = models.IntegerField(null=True)
    contractPeriod_durationInDays = models.IntegerField(null=True)
    amount = models.FloatField(null=True)
    currency = models.CharField(max_length=60, null=True)
    dateSigned = models.CharField(max_length= 100, null=True)
    def __str__(self):
        return f"{self.ocid}"
    
    

class Planificacion(models.Model):
    ocid = models.CharField(max_length=600, null=True)
    id = models.CharField(primary_key=True, max_length=600 )
    rationale = models.CharField(max_length=600, null=True)
    budget_id = models.CharField(max_length=800, null=True)
    budget_description = models.CharField(max_length=600, null=True)
    budget_amount = models.FloatField(max_length=600, null=True)
    budget_currency = models.CharField(max_length=600, null=True)
    def __str__(self):
        return f"{self.ocid}"
    
class Lanzamiento(models.Model):
    ocid = models.CharField(max_length=600, null=True)
    id = models.CharField(primary_key=True, max_length=600 )
    initiationType = models.CharField(max_length=600, null=True)
    buyer_id = models.CharField(max_length=600, null=True)
    buyer_name = models.CharField(max_length=800, null=True)
    language = models.CharField(max_length=600, null=True)
    date = models.CharField(max_length=600, null=True)
    tag = models.CharField(max_length=600, null=True)
    def __str__(self):
        return f"{self.ocid}"


class Provedores(models.Model):
    ocid = models.CharField(max_length=600, null=True)
    release_id = models.CharField(max_length=600, null=True)
    award_id = models.CharField(max_length=600, null=True)
    id = models.CharField(primary_key=True, max_length=600)
    name = models.CharField(max_length=600, null=True)
    def __str__(self):
        return f"{self.id}"

class Licitacion(models.Model):
    ocid = models.CharField(max_length=600, null=True)
    release_id = models.CharField(max_length=600, null=True)
    id = models.CharField(primary_key=True, max_length=600 )
    title = models.CharField(max_length=600, null=True)
    description = models.CharField(max_length=600, null=True)
    status = models.CharField(max_length=600, null=True)
    procuringEntity_id = models.CharField(max_length=600, null=True)
    procuringEntity_name = models.CharField(max_length=600, null=True)
    value_amount = models.FloatField(max_length=600, null=True)
    value_currency = models.CharField(max_length=20, null=True)
    procurementMethod = models.CharField(max_length=60, null=True)
    procurementMethodDetails = models.CharField(max_length=60, null=True)
    mainProcurementCategory = models.CharField(max_length=60, null=True)
    awardCriteria = models.CharField(max_length=60, null=True)
    tenderPeriod_startDate = models.CharField(max_length=600,null=True)
    tenderPeriod_endDate = models.CharField(max_length=600,null=True)
    tenderPeriod_maxExtentDate = models.CharField(max_length=600,null=True)
    tenderPeriod_durationInDays = models.IntegerField(null=True)
    enquiryPeriod_startDate = models.CharField(max_length=600,null=True)
    enquiryPeriod_endDate = models.CharField(max_length=600,null=True)
    enquiryPeriod_maxExtentDate = models.CharField(max_length=600,null=True)
    enquiryPeriod_durationInDays= models.IntegerField(null=True)
    hasEnquiries =  models.CharField(max_length=20, null=True)
    eligibilityCriteria =models.CharField(max_length=600, null=True)
    awardPeriod_startDate = models.CharField(max_length=600,null=True)
    awardPeriod_endDate = models.CharField(max_length=600,null=True)
    awardPeriod_maxExtentDate = models.CharField(max_length=600,null=True)
    awardPeriod_durationInDays = models.IntegerField(null=True)
    numberOfTenderers = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.ocid}"

   



