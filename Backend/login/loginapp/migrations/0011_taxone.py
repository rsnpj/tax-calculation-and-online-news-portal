# Generated by Django 3.2 on 2021-05-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0010_auto_20210513_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annual_gross_salary', models.FloatField(null=True)),
                ('tax_slab_percentage', models.FloatField(null=True)),
                ('taxable_income', models.FloatField(null=True)),
                ('net_payable_tax', models.FloatField(null=True)),
            ],
        ),
    ]