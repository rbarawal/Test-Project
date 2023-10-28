# Generated by Django 3.2.4 on 2023-10-27 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Influencerquestions',
            fields=[
                ('influencerquestionsid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField(blank=True, null=True)),
                ('subheading', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('influencerid', models.ForeignKey(blank=True, db_column='influencerid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.influencerprofile', to_field='influencer_userid')),
                ('serviceid', models.ForeignKey(blank=True, db_column='serviceid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.services')),
            ],
        ),
        migrations.CreateModel(
            name='Orderrequirementquestions',
            fields=[
                ('orderrequirementquestionsid', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('orderid', models.ForeignKey(db_column='orderid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.orders')),
                ('question', models.ForeignKey(db_column='question', on_delete=django.db.models.deletion.DO_NOTHING, to='Client.influencerquestions')),
            ],
        ),
        migrations.CreateModel(
            name='Orderdefaultquestions',
            fields=[
                ('defualtquestionid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField(blank=True, null=True)),
                ('subheading', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('serviceid', models.ForeignKey(blank=True, db_column='serviceid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.services')),
            ],
        ),
        migrations.CreateModel(
            name='Defaultreviews',
            fields=[
                ('defaultreviewsid', models.AutoField(primary_key=True, serialize=False)),
                ('reviews', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('serviceid', models.ForeignKey(blank=True, db_column='serviceid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.services')),
            ],
        ),
    ]
