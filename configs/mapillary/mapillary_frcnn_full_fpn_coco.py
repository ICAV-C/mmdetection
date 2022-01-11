# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
"""import json
with open('data/mapillary_sample/temp_class_map.json', 'r') as file:
    class_dict = json.load(file)"""

classes = ['warning--traffic-merges-right--g1', 'warning--added-lane-right--g1', 'warning--playground--g1', 'information--lodging--g1', 'regulatory--no-stopping--g15', 'regulatory--priority-road--g4', 'information--parking--g1', 'complementary--turn-right--g2', 'warning--pedestrian-stumble-train--g1', 'regulatory--maximum-speed-limit-45--g3', 'regulatory--stop--g1', 'warning--railroad-crossing--g1', 'information--end-of-built-up-area--g1', 'regulatory--pedestrians-only--g1', 'regulatory--no-entry--g1', 'regulatory--one-way-straight--g1', 'complementary--maximum-speed-limit-15--g1', 'regulatory--keep-right--g4', 'regulatory--yield--g1', 'warning--pedestrians-crossing--g10', 'regulatory--reversible-lanes--g2', 'regulatory--turn-left--g2', 'regulatory--no-parking--g2', 'regulatory--one-way-right--g1', 'regulatory--one-way-left--g1', 'warning--divided-highway-ends--g1', 'regulatory--maximum-speed-limit-55--g2', 'information--pedestrians-crossing--g1', 'regulatory--no-right-turn--g1', 'information--tram-bus-stop--g2', 'regulatory--turn-right-ahead--g1', 'regulatory--no-overtaking--g1', 'regulatory--height-limit--g1', 'warning--domestic-animals--g3', 'warning--traffic-merges-left--g1', 'regulatory--maximum-speed-limit-35--g2', 'regulatory--keep-right--g1', 'complementary--priority-route-at-intersection--g1', 'warning--texts--g1', 'complementary--maximum-speed-limit-20--g1', 'information--disabled-persons--g1', 'warning--crossroads--g1', 'regulatory--no-parking--g1', 'warning--roadworks--g1', 'complementary--turn-left--g2', 'warning--double-curve-first-right--g1', 'regulatory--turn-left-ahead--g1', 'regulatory--no-heavy-goods-vehicles--g1', 'regulatory--no-motor-vehicles-except-motorcycles--g1', 'regulatory--maximum-speed-limit-30--g1', 'regulatory--no-motorcycles--g1', 'complementary--chevron-left--g2', 'complementary--chevron-left--g3', 'complementary--chevron-right--g3', 'information--end-of-motorway--g1', 'regulatory--maximum-speed-limit-50--g1', 'warning--texts--g3', 'warning--junction-with-a-side-road-acute-left--g1', 'regulatory--no-heavy-goods-vehicles--g2', 'regulatory--maximum-speed-limit-10--g1', 'regulatory--roundabout--g1', 'warning--texts--g2', 'warning--pedestrians-crossing--g4', 'complementary--keep-left--g1', 'warning--slippery-road-surface--g1', 'warning--double-curve-first-right--g2', 'regulatory--no-parking--g5', 'complementary--obstacle-delineator--g2', 'regulatory--keep-left--g1', 'warning--railroad-crossing-without-barriers--g4', 'complementary--chevron-left--g1', 'regulatory--end-of-prohibition--g1', 'warning--junction-with-a-side-road-perpendicular-right--g1', 'warning--roundabout--g1', 'complementary--obstacle-delineator--g1', 'regulatory--maximum-speed-limit-45--g1', 'regulatory--weight-limit--g1', 'warning--slippery-road-surface--g2', 'complementary--distance--g3', 'warning--junction-with-a-side-road-perpendicular-left--g3', 'regulatory--go-straight--g1', 'information--road-bump--g1', 'warning--children--g1', 'regulatory--maximum-speed-limit-40--g1', 'warning--other-danger--g1', 'regulatory--no-buses--g3', 'regulatory--no-heavy-goods-vehicles--g4', 'complementary--chevron-right-unsure--g6', 'complementary--chevron-right--g5', 'complementary--chevron-right--g1', 'information--stairs--g1', 'warning--curve-right--g1', 'complementary--pass-right--g1', 'complementary--chevron-right--g4', 'warning--t-roads--g1', 'regulatory--no-u-turn--g2', 'warning--junction-with-a-side-road-perpendicular-right--g3', 'warning--horizontal-alignment-right--g1', 'warning--pedestrians-crossing--g1', 'regulatory--keep-left--g2', 'warning--wombat-crossing--g1', 'regulatory--no-hawkers--g1', 'warning--railroad-crossing-with-barriers--g1', 'warning--uneven-road--g2', 'complementary--extent-of-prohibition-area-both-direction--g1', 'warning--t-roads--g2', 'regulatory--turn-left--g1', 'regulatory--turn-left--g3', 'information--parking--g3', 'regulatory--turn-right--g2', 'regulatory--no-motor-vehicles--g4', 'regulatory--shared-path-pedestrians-and-bicycles--g1', 'regulatory--no-overtaking--g5', 'regulatory--maximum-speed-limit-5--g1', 'complementary--go-left--g1', 'warning--double-curve-first-left--g1', 'regulatory--go-straight-or-turn-left--g2', 'regulatory--turn-right--g3', 'information--interstate-route--g1', 'regulatory--lane-control--g1', 'warning--road-bump--g2', 'warning--roadworks--g3', 'regulatory--one-way-left--g3', 'warning--narrow-bridge--g1', 'complementary--maximum-speed-limit-50--g1', 'warning--curve-left--g2', 'regulatory--maximum-speed-limit-60--g1', 'regulatory--maximum-speed-limit-100--g1', 'regulatory--maximum-speed-limit-120--g1', 'information--dead-end--g1', 'complementary--maximum-speed-limit-55--g1', 'warning--junction-with-a-side-road-acute-right--g1', 'regulatory--maximum-speed-limit-70--g1', 'regulatory--no-u-turn--g3', 'regulatory--no-right-turn--g2', 'regulatory--no-stopping--g5', 'warning--roadworks--g2', 'complementary--go-right--g1', 'warning--wild-animals--g4', 'information--bike-route--g1', 'information--food--g2', 'regulatory--go-straight-or-turn-left--g3', 'regulatory--turn-right-ahead--g2', 'regulatory--no-stopping--g2', 'regulatory--give-way-to-oncoming-traffic--g1', 'warning--children--g2', 'complementary--maximum-speed-limit-35--g1', 'warning--road-bump--g1', 'regulatory--no-u-turn--g1', 'warning--pass-left-or-right--g2', 'regulatory--no-overtaking--g2', 'regulatory--turn-right--g1', 'warning--curve-right--g2', 'regulatory--no-turns--g1', 'regulatory--no-turn-on-red--g3', 'regulatory--no-parking-or-no-stopping--g2', 'regulatory--stop-here-on-red-or-flashing-light--g2', 'regulatory--maximum-speed-limit-25--g2', 'warning--junction-with-a-side-road-perpendicular-left--g1', 'warning--winding-road-first-right--g1', 'warning--accidental-area-unsure--g2', 'regulatory--no-overtaking--g4', 'warning--school-zone--g2', 'regulatory--wrong-way--g1', 'regulatory--road-closed--g2', 'regulatory--no-stopping--g8', 'complementary--distance--g1', 'warning--emergency-vehicles--g1', 'warning--kangaloo-crossing--g1', 'complementary--maximum-speed-limit-30--g1', 'warning--turn-right--g1', 'regulatory--truck-speed-limit-60--g1', 'regulatory--priority-over-oncoming-vehicles--g1', 'information--pedestrians-crossing--g2', 'information--parking--g5', 'information--children--g1', 'regulatory--passing-lane-ahead--g1', 'information--airport--g1', 'information--limited-access-road--g1', 'regulatory--no-motor-vehicles-except-motorcycles--g2', 'information--safety-area--g2', 'warning--roundabout--g25', 'regulatory--no-left-turn--g1', 'warning--roadworks--g4', 'complementary--trucks--g1', 'regulatory--go-straight--g3', 'warning--steep-ascent--g7', 'warning--divided-highway-ends--g2', 'information--parking--g45', 'regulatory--buses-only--g1', 'regulatory--one-way-right--g3', 'regulatory--maximum-speed-limit-20--g1', 'warning--road-narrows--g1', 'warning--road-narrows-left--g1', 'complementary--accident-area--g3', 'regulatory--one-way-left--g2', 'warning--road-narrows-left--g2', 'warning--trucks-crossing--g1', 'regulatory--bicycles-only--g1', 'complementary--maximum-speed-limit-70--g1', 'warning--curve-left--g1', 'warning--domestic-animals--g1', 'regulatory--maximum-speed-limit-30--g3', 'warning--road-narrows-right--g2', 'regulatory--keep-right--g6', 'information--living-street--g1', 'complementary--tow-away-zone--g1', 'regulatory--triple-lanes-turn-left-center-lane--g1', 'regulatory--maximum-speed-limit-90--g1', 'complementary--both-directions--g1', 'complementary--maximum-speed-limit-45--g1', 'warning--turn-left--g1', 'regulatory--maximum-speed-limit-80--g1', 'complementary--maximum-speed-limit-75--g1', 'regulatory--dual-lanes-go-straight-on-right--g1', 'regulatory--do-not-block-intersection--g1', 'regulatory--radar-enforced--g1', 'warning--traffic-merges-right--g2', 'regulatory--stop--g10', 'regulatory--go-straight-or-turn-left--g1', 'regulatory--no-straight-through--g2', 'regulatory--end-of-maximum-speed-limit-70--g2', 'regulatory--minimum-safe-distance--g1', 'regulatory--no-turn-on-red--g1', 'regulatory--stop-signals--g1', 'information--gas-station--g1', 'regulatory--end-of-speed-limit-zone--g1', 'warning--two-way-traffic--g1', 'warning--railroad-crossing-without-barriers--g3', 'information--hospital--g1', 'warning--stop-ahead--g9', 'warning--railroad-crossing--g3', 'information--motorway--g1', 'information--emergency-facility--g2', 'warning--road-widens--g1', 'regulatory--road-closed-to-vehicles--g3', 'information--highway-exit--g1', 'regulatory--no-turn-on-red--g2', 'regulatory--no-pedestrians--g2', 'regulatory--width-limit--g1', 'warning--hairpin-curve-right--g1', 'complementary--keep-right--g1', 'warning--junction-with-a-side-road-perpendicular-left--g4', 'warning--flaggers-in-road--g1', 'warning--wild-animals--g1', 'warning--traffic-signals--g4', 'warning--crossroads--g3', 'warning--two-way-traffic--g2', 'warning--traffic-signals--g2', 'regulatory--one-way-right--g2', 'regulatory--no-overtaking-by-heavy-goods-vehicles--g1', 'complementary--distance--g2', 'warning--double-reverse-curve-right--g1', 'warning--double-curve-first-left--g2', 'complementary--except-bicycles--g1', 'warning--traffic-signals--g1', 'complementary--chevron-left--g5', 'warning--road-widens-right--g1', 'regulatory--maximum-speed-limit-40--g6', 'warning--horizontal-alignment-left--g1', 'regulatory--no-bicycles--g1', 'regulatory--maximum-speed-limit-15--g1', 'regulatory--no-straight-through--g1', 'regulatory--parking-restrictions--g2', 'regulatory--no-parking-or-no-stopping--g1', 'warning--uneven-road--g6', 'complementary--go-right--g2', 'warning--railroad-intersection--g3', 'warning--railroad-crossing--g4', 'information--airport--g2', 'complementary--trucks-turn-right--g1', 'regulatory--end-of-bicycles-only--g1', 'warning--road-narrows--g2', 'warning--narrow-bridge--g3', 'warning--pedestrians-crossing--g5', 'regulatory--maximum-speed-limit-led-60--g1', 'regulatory--no-parking-or-no-stopping--g3', 'regulatory--pedestrians-only--g2', 'warning--slippery-motorcycles--g1', 'regulatory--pass-on-either-side--g2', 'complementary--one-direction-right--g1', 'warning--pedestrians-crossing--g9', 'regulatory--go-straight-or-turn-right--g1', 'information--end-of-living-street--g1', 'information--bus-stop--g1', 'warning--winding-road-first-left--g1', 'warning--bus-stop-ahead--g3', 'warning--double-turn-first-right--g1', 'warning--winding-road-first-right--g3', 'warning--railroad-crossing-with-barriers--g2', 'warning--railroad-intersection--g4', 'regulatory--keep-right--g2', 'warning--bicycles-crossing--g2', 'regulatory--bicycles-only--g2', 'regulatory--maximum-speed-limit-led-80--g1', 'warning--height-restriction--g2', 'regulatory--maximum-speed-limit-50--g6', 'warning--hairpin-curve-right--g4', 'warning--traffic-signals--g3', 'regulatory--mopeds-and-bicycles-only--g1', 'regulatory--no-left-turn--g2', 'regulatory--end-of-no-parking--g1', 'regulatory--end-of-priority-road--g1', 'regulatory--no-heavy-goods-vehicles-or-buses--g1', 'warning--uneven-roads-ahead--g1', 'regulatory--road-closed-to-vehicles--g1', 'warning--hairpin-curve-left--g1', 'information--trailer-camping--g1', 'regulatory--no-stopping--g4', 'regulatory--no-pedestrians-or-bicycles--g1', 'regulatory--no-heavy-goods-vehicles--g5', 'warning--other-danger--g3', 'warning--falling-rocks-or-debris-right--g1', 'regulatory--dual-lanes-go-straight-on-left--g1', 'regulatory--u-turn--g1', 'complementary--maximum-speed-limit-40--g1', 'regulatory--stop-here-on-red-or-flashing-light--g1', 'information--parking--g6', 'regulatory--no-motor-vehicle-trailers--g1', 'regulatory--no-pedestrians--g1', 'regulatory--no-pedestrians--g3', 'warning--traffic-merges-left--g2', 'regulatory--text-four-lines--g1', 'regulatory--dual-path-bicycles-and-pedestrians--g1', 'regulatory--maximum-speed-limit-40--g3', 'information--parking--g2', 'warning--bicycles-crossing--g3', 'regulatory--pass-on-either-side--g1', 'regulatory--no-bicycles--g3', 'warning--pass-left-or-right--g1', 'complementary--chevron-left--g4', 'warning--falling-rocks-or-debris-right--g2', 'regulatory--maximum-speed-limit-led-100--g1', 'warning--pedestrians-crossing--g12', 'complementary--buses--g1', 'warning--road-narrows-right--g1', 'information--highway-interstate-route--g2', 'warning--y-roads--g1', 'warning--railroad-crossing-without-barriers--g1', 'information--telephone--g2', 'regulatory--maximum-speed-limit-110--g1', 'regulatory--no-right-turn--g3', 'regulatory--stop--g2', 'regulatory--left-turn-yield-on-green--g1', 'warning--dual-lanes-right-turn-or-go-straight--g1', 'regulatory--dual-path-pedestrians-and-bicycles--g1', 'regulatory--maximum-speed-limit-100--g3', 'complementary--one-direction-left--g1', 'regulatory--no-left-turn--g3', 'regulatory--go-straight-or-turn-right--g3', 'warning--dip--g2', 'warning--bicycles-crossing--g1', 'regulatory--no-motorcycles--g2', 'regulatory--road-closed--g1', 'warning--winding-road-first-left--g2', 'regulatory--end-of-maximum-speed-limit-30--g2', 'warning--loop-270-degree--g1', 'complementary--maximum-speed-limit-25--g1', 'warning--falling-rocks-or-debris-right--g4', 'regulatory--maximum-speed-limit-65--g2', 'warning--trail-crossing--g2', 'regulatory--no-vehicles-carrying-dangerous-goods--g1', 'information--end-of-limited-access-road--g1', 'information--telephone--g1', 'information--central-lane--g1', 'warning--offset-roads--g3', 'regulatory--roundabout--g2', 'warning--roadworks--g6', 'warning--crossroads-with-priority-to-the-right--g1', 'information--no-parking--g3', 'information--gas-station--g3', 'regulatory--dual-lanes-turn-right-or-straight--g1', 'regulatory--maximum-speed-limit-25--g1', 'regulatory--no-bicycles--g2', 'regulatory--dual-lanes-turn-left-or-straight--g1', 'regulatory--no-mopeds-or-bicycles--g1', 'warning--horizontal-alignment-right--g3', 'information--camp--g1', 'warning--pedestrians-crossing--g11', 'regulatory--no-motor-vehicles--g1', 'warning--shared-lane-motorcycles-bicycles--g1', 'information--minimum-speed-40--g1', 'information--dead-end-except-bicycles--g1', 'regulatory--do-not-stop-on-tracks--g1', 'warning--turn-right--g2', 'warning--trams-crossing--g1', 'warning--railroad-crossing-with-barriers--g4', 'warning--restricted-zone--g1', 'regulatory--end-of-maximum-speed-limit-70--g1', 'regulatory--turning-vehicles-yield-to-pedestrians--g1', 'warning--playground--g3', 'regulatory--bicycles-only--g3', 'warning--hairpin-curve-left--g3', 'regulatory--end-of-buses-only--g1', 'regulatory--dual-lanes-turn-left-no-u-turn--g1', 'regulatory--shared-path-bicycles-and-pedestrians--g1', 'warning--equestrians-crossing--g2', 'regulatory--weight-limit-with-trucks--g1', 'regulatory--detour-left--g1', 'information--end-of-pedestrians-only--g2']
#classes = ['warning--pedestrians-crossing--g10','regulatory--one-way-straight--g1','information--road-bump--g1','information--parking--g45','regulatory--no-parking--g2','regulatory--one-way-left--g3','regulatory--one-way-right--g3','information--highway-exit--g1','complementary--keep-left--g1','complementary--keep-right--g1','regulatory--maximum-speed-limit-led-60--g1','warning--roadworks--g6','warning--pedestrians-crossing--g12','warning--pedestrians-crossing--g9','complementary--maximum-speed-limit-40--g1','complementary--maximum-speed-limit-50--g1','warning--railroad-crossing-with-barriers--g2','regulatory--maximum-speed-limit-90--g1','warning--bus-stop-ahead--g3','information--airport--g2','complementary--maximum-speed-limit-70--g1','complementary--chevron-left--g5','complementary--chevron-right--g6','warning--traffic-signals--g4','regulatory--roundabout--g2','regulatory--yield--g1','warning--kangaloo-crossing--g1']
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
