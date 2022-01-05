import os.path as osp


def load_annotation(root, image_key):
    with open(os.path.join(root, 'annotations', '{:s}.json'.format(image_key)), 'r') as fid:
        anno = json.load(fid)
    return anno

def convert_mapillary_to_coco(root_dir, keys_file, outfile):
    split = keys_file.split('')
    with open(keys_file) as file:
        keys = file.readlines()
        keys = [key.rstrip() for key in keys]

        for idx, key in enumerate(keys):
            file_name = key
            
            with Image.open(os.path.join(root, 'train/images', '{:s}.jpg'.format(image_key))) as img:
            ann = load_annotation(root_dir, key)
            for obj in ann['objects']:


def convert_balloon_to_coco(ann_file, out_file, image_prefix):
    data_infos = mmcv.load(ann_file)

    annotations = []
    images = []
    obj_count = 0
    for idx, v in enumerate(mmcv.track_iter_progress(data_infos.values())):
        filename = v['filename']
        img_path = osp.join(image_prefix, filename)
        height, width = mmcv.imread(img_path).shape[:2]

        images.append(dict(
            id=idx,
            file_name=filename,
            height=height,
            width=width))

        bboxes = []
        labels = []
        masks = []
        for _, obj in v['regions'].items():
            assert not obj['region_attributes']
            obj = obj['shape_attributes']
            px = obj['all_points_x']
            py = obj['all_points_y']
            poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
            poly = [p for x in poly for p in x]

            x_min, y_min, x_max, y_max = (
                min(px), min(py), max(px), max(py))


            data_anno = dict(
                image_id=idx,
                id=obj_count,
                category_id=0,
                bbox=[x_min, y_min, x_max - x_min, y_max - y_min],
                area=(x_max - x_min) * (y_max - y_min),
                segmentation=[poly],
                iscrowd=0)
            annotations.append(data_anno)
            obj_count += 1

    coco_format_json = dict(
        images=images,
        annotations=annotations,
        categories=[{'id':0, 'name': 'balloon'}])
    mmcv.dump(coco_format_json, out_file)
