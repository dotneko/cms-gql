# Generated by Django 3.1 on 2020-08-23 00:48

import cmssys.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('alias', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('description_chinese', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Advisory list',
                'db_table': 'advisory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=1)),
                ('cash_amount', models.FloatField()),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('settle_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('supplierdn', models.CharField(blank=True, max_length=255, null=True)),
                ('total_cost', models.FloatField()),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_note_no', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Deliveries',
                'db_table': 'delivery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Depletion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=1)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('move_to', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('depletion_type', models.CharField(choices=[('Stock Move', 'Stock Move'), ('Stock Take', 'Stock Take')], db_column='type', max_length=255)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'depletion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepletionItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.FloatField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('update_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'depletion_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('alias', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_chinese', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'instruction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('avg_cost', models.FloatField(default=0)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('clinic_drug_no', models.CharField(blank=True, max_length=255, null=True)),
                ('dangerous_sign', cmssys.models.TextBooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('discontinue', cmssys.models.TextBooleanField()),
                ('dosage', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('expected_qty', models.FloatField(default=1000)),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('frequency', models.CharField(blank=True, max_length=255, null=True)),
                ('generic_name', models.CharField(blank=True, max_length=255, null=True)),
                ('generic_name_chinese', models.CharField(blank=True, max_length=255, null=True)),
                ('ingredient', models.TextField(blank=True, null=True)),
                ('inventory_type', models.CharField(blank=True, max_length=255, null=True)),
                ('is_clinic_drug_list', cmssys.models.TextBooleanField()),
                ('is_master_drug_list', cmssys.models.TextBooleanField()),
                ('label_name', models.CharField(blank=True, max_length=255, null=True)),
                ('label_name_chinese', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('mini_dispensary_unit', models.FloatField(default=0)),
                ('mini_dosage_unit', models.FloatField(default=0)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_name_chinese', models.CharField(blank=True, max_length=255, null=True)),
                ('registration_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('reorder_level', models.FloatField(default=100)),
                ('reorder_status', models.CharField(blank=True, max_length=255, null=True)),
                ('standard_cost', models.FloatField(default=0)),
                ('stock_qty', models.FloatField(default=0)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_price', models.FloatField(default=0)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.FloatField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'inventory_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryItemType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'inventory_item_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryMovementLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('lot_no', models.CharField(blank=True, max_length=255, null=True)),
                ('move_item', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.FloatField()),
                ('reference_no', models.CharField(blank=True, max_length=255, null=True)),
                ('movement_type', models.CharField(blank=True, choices=[('Delivery', 'Delivery'), ('Dispensary', 'Dispensary'), ('Reconciliation', 'Reconciliation'), ('Stock Initialization', 'Stock Initialization')], db_column='type', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'inventory_movement_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReceivedItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('arrive_date', models.DateField(auto_now_add=True, null=True)),
                ('cost', models.FloatField()),
                ('dangerous_sign', models.BooleanField(default=False)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('lot_no', models.CharField(max_length=255)),
                ('manufacturer_id', models.BigIntegerField(blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('supplier_id', models.BigIntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('use_up', models.BooleanField(default=False)),
                ('received_items_idx', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'received_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=1)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('settle_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=255, null=True)),
                ('total_cost', models.FloatField()),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RequestItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=1)),
                ('expected_qty', models.FloatField()),
                ('quantity', models.FloatField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('stock_qty', models.FloatField()),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('request_items_idx', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'request_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('tel_home', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_office', models.CharField(blank=True, max_length=255, null=True)),
                ('supp_type', models.CharField(blank=True, choices=[('Certificate Holder', 'Certificate Holder'), ('Supplier', 'Supplier'), ('Manufacturer', 'Manufacturer')], db_column='type', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'supplier_manufacturer',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryItemSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliers_idx', models.IntegerField(blank=True, default=0, null=True)),
                ('inventory_item', models.ForeignKey(db_column='inventory_item_suppliers_id', on_delete=django.db.models.deletion.PROTECT, to='cmsinv.inventoryitem')),
                ('supplier', models.ForeignKey(db_column='supplier_manufacturer_id', on_delete=django.db.models.deletion.PROTECT, to='cmsinv.supplier')),
            ],
            options={
                'db_table': 'inventory_item_supplier_manufacturer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DepletionDepletionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_idx', models.IntegerField(blank=True, null=True)),
                ('depletion', models.ForeignKey(db_column='depletion_items_id', on_delete=django.db.models.deletion.CASCADE, to='cmsinv.depletion')),
                ('depletion_item', models.ForeignKey(db_column='depletion_item_id', on_delete=django.db.models.deletion.CASCADE, to='cmsinv.depletionitem')),
            ],
            options={
                'db_table': 'depletion_depletion_item',
                'managed': True,
            },
        ),
    ]