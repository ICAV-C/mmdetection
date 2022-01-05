# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
"""import json
with open('data/mapillary_sample/temp_class_map.json', 'r') as file:
    class_dict = json.load(file)"""
classes = ["other-sign", "regulatory--keep-right--g1", "regulatory--priority-over-oncoming-vehicles--g1", "regulatory--height-limit--g1", "regulatory--maximum-speed-limit-35--g2"]
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=len(classes))))

# Modify dataset related settings
dataset_type = 'COCODataset'
data = dict(
    train=dict(
        img_prefix='data/mapillary_sample/train/',
        classes=classes,
        ann_file='data/mapillary_sample/temp_coco_train.json'),
    val=dict(
        img_prefix='data/mapillary_sample/train/',
        classes=classes,
        ann_file='data/mapillary_sample/temp_coco_train.json'),
    test=dict(
        img_prefix='data/mapillary_sample/train/',
        classes=classes,
        ann_file='data/mapillary_sample/temp_coco_train.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
#load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
