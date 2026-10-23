# Codex conversation

## User

假设ObjectConceptLearning/data/from_web已准备完善。为了满足ObjectConceptLearning/Test.md中的要求，接下来我该怎么做？我将把程序和数据上传到服务器上。

## Assistant

我先查看 `Test.md` 以及项目当前目录结构，确认服务器部署前需要准备的程序、数据、环境和运行命令。

## Activity

    $ pwd && rg --files -g 'Test.md' -g '!*.pyc' -g '!__pycache__/**' | sort && printf '\n--- top-level ---\n' && find . -maxdepth 2 -type f | sort | sed -n '1,160p'
    /home/linfu/src/Test/ObjectConceptLearning/data
    
    --- top-level ---
    ./download_web_images.py
    ./from_web.tgz
    ./from_web.tgz:Zone.Identifier
    ./from_web/test_0001.jpg
    ./from_web/test_0003.jpg
    ./from_web/test_0005.jpg
    ./from_web/test_0006.jpg
    ./from_web/test_0007.jpg
    ./from_web/test_0009.jpg
    ./from_web/test_0010.jpeg
    ./from_web/test_0011.jpg
    ./from_web/test_0012.jpg
    ./from_web/test_0013.jpg
    ./from_web/test_0015.jpg
    ./from_web/test_0016.jpg
    ./from_web/test_0017.jpeg
    ./from_web/test_0018.jpg
    ./from_web/test_0019.jpg
    ./from_web/test_0020.jpeg
    ./from_web/test_0021.jpg
    ./from_web/test_0022.jpg
    ./from_web/test_0024.jpg
    ./from_web/test_0025.jpg
    ./from_web/test_0026.jpg
    ./from_web/test_0027.jpg
    ./from_web/test_0029.jpg
    ./from_web/test_0030.jpg
    ./from_web/test_0031.jpg
    ./from_web/test_0032.jpg
    ./from_web/test_0033.jpg
    ./from_web/test_0034.jpeg
    ./from_web/test_0035.jpg
    ./from_web/test_0036.jpg
    ./from_web/test_0037.jpg
    ./from_web/test_0038.jpg
    ./from_web/test_0039.jpg
    ./from_web/test_0040.jpg
    ./from_web/test_0041.jpg
    ./from_web/test_0044.jpg
    ./from_web/test_0045.jpg
    ./from_web/test_0046.jpg
    ./from_web/test_0047.jpg
    ./from_web/test_0048.jpg
    ./from_web/test_0049.jpg
    ./from_web/test_0050.jpg
    ./from_web/test_0052.jpg
    ./from_web/test_0053.jpg
    ./from_web/test_0054.jpg
    ./from_web/test_0055.jpg
    ./from_web/test_0056.jpeg
    ./from_web/test_0057.jpg
    ./from_web/test_0058.jpg
    ./from_web/test_0059.jpg
    ./from_web/test_0060.jpg
    ./from_web/test_0061.jpg
    ./from_web/test_0062.jpg
    ./from_web/test_0063.jpg
    ./from_web/test_0064.jpg
    ./from_web/test_0065.jpeg
    ./from_web/test_0068.jpg
    ./from_web/test_0070.jpg
    ./from_web/test_0072.jpg
    ./from_web/test_0074.png
    ./from_web/test_0075.jpg
    ./from_web/test_0076.jpg
    ./from_web/test_0077.jpg
    ./from_web/test_0078.jpg
    ./from_web/test_0079.jpg
    ./from_web/test_0080.jpg
    ./from_web/test_0081.jpg
    ./from_web/test_0082.jpg
    ./from_web/test_0083.jpg
    ./from_web/test_0084.jpg
    ./from_web/test_0085.jpg
    ./from_web/test_0086.jpg
    ./from_web/test_0087.jpg
    ./from_web/test_0088.jpg
    ./from_web/test_0090.jpg
    ./from_web/test_0091.jpg
    ./from_web/test_0092.jpg
    ./from_web/test_0093.jpeg
    ./from_web/test_0095.jpg
    ./from_web/test_0096.jpg
    ./from_web/test_0097.jpg
    ./from_web/test_0099.jpg
    ./from_web/test_0100.png
    ./from_web/test_0101.jpg
    ./from_web/test_0102.jpeg
    ./from_web/test_0103.jpg
    ./from_web/test_0107.jpg
    ./from_web/test_0108.jpeg
    ./from_web/test_0109.jpeg
    ./from_web/test_0110.jpg
    ./from_web/test_0112.jpg
    ./from_web/test_0113.jpg
    ./from_web/test_0115.jpeg
    ./from_web/test_0117.png
    ./from_web/test_0118.jpg
    ./from_web/test_0119.jpg
    ./from_web/test_0120.jpeg
    ./from_web/test_0121.jpg
    ./from_web/test_0122.jpeg
    ./from_web/test_0123.jpg
    ./from_web/test_0124.jpg
    ./from_web/test_0125.jpg
    ./from_web/test_0126.jpg
    ./from_web/test_0127.jpg
    ./from_web/test_0128.jpg
    ./from_web/test_0129.jpg
    ./from_web/test_0130.jpg
    ./from_web/test_0131.jpg
    ./from_web/test_0133.jpeg
    ./from_web/test_0134.png
    ./from_web/test_0135.jpg
    ./from_web/test_0136.jpg
    ./from_web/test_0137.jpg
    ./from_web/test_0138.jpg
    ./from_web/test_0139.jpeg
    ./from_web/test_0140.jpg
    ./from_web/test_0141.jpg
    ./from_web/test_0142.jpg
    ./from_web/test_0143.jpg
    ./from_web/test_0144.jpg
    ./from_web/test_0146.jpg
    ./from_web/test_0147.jpg
    ./from_web/test_0148.png
    ./from_web/test_0149.jpg
    ./from_web/test_0150.jpg
    ./from_web/test_0151.jpg
    ./from_web/test_0152.jpg
    ./from_web/test_0153.jpg
    ./from_web/test_0154.jpeg
    ./from_web/test_0156.jpeg
    ./from_web/test_0157.jpg
    ./from_web/test_0158.jpg
    ./from_web/test_0160.jpg
    ./from_web/test_0161.jpg
    ./from_web/test_0162.jpg
    ./from_web/test_0163.jpg
    ./from_web/test_0165.jpg
    ./from_web/test_0166.jpg
    ./from_web/test_0167.jpg
    ./from_web/test_0168.jpg
    ./from_web/test_0169.jpg
    ./from_web/test_0170.jpg
    ./from_web/test_0172.jpg
    ./from_web/test_0173.jpg
    ./from_web/test_0174.jpg
    ./from_web/test_0175.jpg
    ./from_web/test_0176.jpg
    ./from_web/test_0177.jpg
    ./from_web/test_0178.jpeg
    ./from_web/test_0179.jpg
    ./from_web/test_0180.jpg
    ./from_web/test_0181.jpg
    ./from_web/test_0182.jpg
    ./from_web/test_0183.png
    ./from_web/test_0184.jpg
    ./from_web/test_0185.jpg
    ./from_web/test_0186.jpg
    ✓ • 298ms

## User

请从环境准备，数据准备，代码完备3个角度分析并给我step-by-step的指南

## Assistant

我会按“环境准备、数据准备、代码完备”三个角度核对，并把结果整理成服务器上可依次执行的步骤，标明哪些已经具备、哪些还需要补齐。

## Activity

    $ pwd
    /home/linfu/src/Test/ObjectConceptLearning
    ✓ • 0ms

## Activity

    $ cat Test.md
    # OCL
    
    Implement an OCL-based object category classification inference experiment.
    
    Set up your own Python environment by downloading and installing **Miniforge / uv / Python**, and then begin the experiment.
    
    ## References
    
    1. OCL paper: **Beyond Object Recognition: A New Benchmark towards Object Concept Learning**
    
    2. **OCL dataset preparation**
    
       - The official data preparation scripts are provided in the OCL GitHub repository: [https://github.com/silicx/ObjectConceptLearning/tree/main/data](https://github.com/silicx/ObjectConceptLearning/tree/main/data)
       - Please read and understand the provided scripts and dataset structure before implementing the DataLoader.
       - In particular, the repository provides `prepare_data.sh`, `download_web_images.py`, and the `resources` directory for dataset preparation.
       - After downloading the dataset, inspect the image data and annotation files carefully and understand how **category**, **attribute**, and **affordance** annotations are represented.
    
    3. Download and prepare the required test data using the scripts provided in the official OCL GitHub repository.
    
    4. CLIP paper/repository: **Contrastive Language-Image Pre-Training**
    
       [https://github.com/openai/CLIP](https://github.com/openai/CLIP)
    
    ## Step 1: Prepare the DataLoader
    
    1. Implement a custom dataset class by inheriting from PyTorch's native `Dataset`:
    
       - Load the dataset and corresponding annotations;
       - Filter the data by sorting category labels according to the number of samples, and keep only the **10 categories with the largest number of samples**;
       - Perform image preprocessing and text tokenization.
    
    2. Create a test data loader using PyTorch's native `DataLoader`:
    
       - Set `batch_size = 4`.
    
    ## Step 2: Prepare the CLIP Model
    
    1. Load a pretrained CLIP model using the available API.
    
    ## Step 3: Inference and Evaluation
    
    1. Instantiate the dataset and model, and move the model to GPU, including:
    
       - `load_dataset`
       - `load_model`
       - `model.to(device)`
    
    2. Set the model to inference mode and freeze all model parameters:
    
       - Iterate over all model parameters and set gradient computation to `False`.
    
    3. Iterate over the test set and perform inference:
    
       - Each image may contain multiple objects.
       - Compute the cosine similarity between each object and the candidate **category** labels.
       - Use the cosine similarity scores for ranking.
       - Compute the model's **Top-k accuracy**.
       - Perform forward inference batch by batch and report the average accuracy over the entire test set.
    
    4. Evaluate the prediction performance for **attribute** and **affordance** labels using the **mAP (mean Average Precision)** metric.
    ✓ • 0ms

## Activity

    $ git status --short
     M .gitignore
     M README.md
     M data/download_web_images.py
     M data/prepare_data.sh
    ?? Test.md
    ?? aPY/
    ?? clip_dataset.py
    ?? clip_inference.py
    ?? data/from_web.tgz
    ?? data/from_web.tgz:Zone.Identifier
    ?? data/resources/OCL_annot_test.pkl
    ?? data/resources/OCL_annot_train.pkl
    ?? data/resources/OCL_annot_val.pkl
    ?? docs/clip_inference.md
    ?? requirements-clip.txt
    ?? setup_clip_gpu.sh
    ?? tests/
    ✓ • 0ms

## Activity

    $ rg --files -g AGENTS.md -g '!data/from_web/**' -g '!data/*.tgz' /home/linfu/src/Test /home/linfu/.codex 2>/dev/null
    ✗ (1) • 125ms

## Activity

    $ rg --files -g '!data/from_web/**' -g '!data/*.tgz' -g '!*.pyc' -g '!**/__pycache__/**' -g '!**/.git/**'
    setup_clip_gpu.sh
    docs/clip_inference.md
    docs/task.png
    README.md
    requirements-clip.txt
    config/OCRN_stage2.yaml
    config/OCRN_stage1.yaml
    config/Faster50Feature.yaml
    config/OCRN_stage3.yaml
    config/BaseConfig.yaml
    LICENSE
    test_tde.py
    utils/__init__.py
    clip_dataset.py
    utils/dataset/__init__.py
    clip_inference.py
    run_ocl.py
    requirements.txt
    utils/dataset/data_utils.py
    utils/dataset/OCL_dataset.py
    utils/evaluator.py
    utils/utils.py
    calc_dataset_prior.py
    extract_feature.py
    tests/test_download_web_images.py
    models/__init__.py
    tests/test_clip_category_selection.py
    Test.md
    data/from_web.tgz:Zone.Identifier
    data/prepare_data.sh
    models/feature.py
    models/base_models.py
    models/OCRN_intervention.py
    test_ocl.py
    aPY/ayahoo_test_images.tar.gz
    aPY/VOCtrainval_14-Jul-2008.tar
    data/resources/OCL_annot_val.pkl
    data/resources/OCL_class_object.json
    data/resources/OCL_annot_test.pkl
    data/resources/OCL_annot.tgz
    data/resources/category_aff_matrix.json
    data/resources/OCL_annot_train.pkl
    data/resources/causal_many_shot300.json
    data/resources/OCL_category_annot.json
    data/resources/OCL_class_affordance.json
    data/resources/OCL_class_attribute.json
    data/resources/OCL_weight.json
    data/resources/url_to_filename.json
    data/SUN/images/e/excavation/sun_azfhopjzrcrakowb.jpg
    data/SUN/images/e/excavation/sun_bqklycsnizxqadyi.jpg
    data/SUN/images/e/excavation/sun_brblkcriwevpompg.jpg
    data/SUN/images/e/excavation/sun_bczyhtycrunqjqvk.jpg
    data/SUN/images/e/excavation/sun_bbepytfbwzaursez.jpg
    data/SUN/images/e/excavation/sun_bdwnrzbgbairyofe.jpg
    data/SUN/images/e/excavation/sun_bhkwccjejnymafel.jpg
    data/SUN/images/e/excavation/sun_bpxjswtenkfzpllj.jpg
    data/SUN/images/e/excavation/sun_aqlqigrtvsekvebg.jpg
    data/SUN/images/e/excavation/sun_bqptezoddaurwyqh.jpg
    data/SUN/images/e/excavation/sun_bmivqtdizhntlwvl.jpg
    data/SUN/images/e/excavation/sun_auolpexyapurugmc.jpg
    data/SUN/images/e/excavation/sun_azkkwrjfndakvxxk.jpg
    data/SUN/images/e/excavation/sun_bmixwwyahvceqgmc.jpg
    data/SUN/images/e/excavation/sun_aknncljcrmtysrge.jpg
    data/SUN/images/e/excavation/sun_bmxnoyalfwrshdqo.jpg
    data/SUN/images/e/excavation/sun_afonyfevemledovi.jpg
    data/SUN/images/e/excavation/sun_ajctgesrsttsabke.jpg
    data/SUN/images/e/excavation/sun_brjrsqfytymzaaig.jpg
    data/SUN/images/e/excavation/sun_anoyvyykrcsbjsdn.jpg
    data/SUN/images/e/excavation/sun_bnxamdrdmtnpmfdp.jpg
    data/SUN/images/e/elevator_shaft/sun_afxxlyvgmhxzkxjs.jpg
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_003777.png
    data/SUN/images/e/elevator_shaft/sun_aefcbrgrtkkhfznu.jpg
    data/SUN/images/e/elevator_shaft/sun_aeyjnybbygaaonmh.jpg
    data/SUN/images/e/elevator_shaft/sun_alpkhxvjuxlgysvh.jpg
    data/SUN/images/e/elevator_shaft/sun_amatwvgcfyzuynms.jpg
    data/SUN/images/e/elevator_shaft/sun_afcagahirnkxvaja.jpg
    data/SUN/images/e/elevator_shaft/sun_akhwozmuqyvaayfl.jpg
    data/SUN/images/e/elevator_shaft/sun_abbqsmpgzwrfmjxg.jpg
    data/SUN/images/e/elevator_shaft/sun_agoxuyhyugwuuekn.jpg
    data/SUN/images/e/elevator_shaft/sun_apnagbvvtlhmnidd.jpg
    data/SUN/images/e/elevator_shaft/sun_aqhbnjejdmwfpifm.jpg
    data/SUN/images/e/elevator_shaft/sun_akfqcrrqpbzjsqob.jpg
    data/SUN/images/e/elevator_shaft/sun_akehcuvnzdqbcjtr.jpg
    data/SUN/images/e/elevator_shaft/sun_aqftctjxicgethmn.jpg
    data/SUN/images/e/elevator_shaft/sun_acvovsrkuqmypydj.jpg
    data/SUN/images/e/elevator_shaft/sun_aafmfybkndnlumop.jpg
    data/SUN/images/e/elevator_shaft/sun_agejojvttluyffmk.jpg
    data/SUN/images/e/elevator_shaft/sun_akcycfgptrmdmbik.jpg
    data/SUN/images/e/elevator_shaft/sun_ajruhveolfpfjvvj.jpg
    data/SUN/images/e/elevator_shaft/sun_atisekgpjwviikei.jpg
    data/SUN/images/e/elevator_shaft/sun_aktwjrhpbihxnxhq.jpg
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000529.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001027.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008525.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003841.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003872.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000452.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006434.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001884.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005951.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002904.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000346.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008526.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001154.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005210.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007154.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003621.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005354.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000540.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006530.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003815.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005926.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006327.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002240.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001040.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004866.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008072.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001971.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002387.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005124.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008204.png
    data/SUN/images/e/editing_room/sun_bqjdqtxebniwaukg.jpg
    data/SUN/images/e/editing_room/sun_aledxrcfulsknabk.jpg
    data/SUN/images/e/editing_room/sun_bqvdzhyseilwhslm.jpg
    data/SUN/images/e/editing_room/sun_bmmkxdkouibgvvtk.jpg
    data/SUN/images/e/editing_room/sun_asyicswfrmmzyijp.jpg
    data/SUN/images/e/editing_room/sun_aedzefctxsvpcezr.jpg
    data/SUN/images/e/editing_room/sun_bsonwhdqhbajrxgb.jpg
    data/SUN/images/e/editing_room/sun_bhuhmobsmsycsxjs.jpg
    data/SUN/images/e/editing_room/sun_avtxgxwuxoomybfj.jpg
    data/SUN/images/e/editing_room/sun_bhfniphgmyksqlpm.jpg
    data/SUN/images/e/editing_room/sun_beglihuiydroxxss.jpg
    data/SUN/images/e/editing_room/sun_bzboclmajioqhsgz.jpg
    data/SUN/images/e/editing_room/sun_bldstlalggzleyzq.jpg
    data/SUN/images/e/editing_room/sun_bgsisetzvbqurena.jpg
    data/SUN/images/e/editing_room/sun_aoaypbdlejihulqi.jpg
    data/SUN/images/e/editing_room/sun_bgmludmotlglbyku.jpg
    data/SUN/images/e/editing_room/sun_bjikzaemhafgbqzf.jpg
    data/SUN/images/e/editing_room/sun_buxoxpbhptuiguwd.jpg
    data/SUN/images/e/editing_room/sun_axkhpldvtdflszgg.jpg
    data/SUN/images/e/editing_room/sun_beacpfaowprndckt.jpg
    data/SUN/images/e/editing_room/sun_asubxpjjntvaymca.jpg
    data/SUN/images/e/elevator/door/sun_asenfytsrpomalqd.jpg
    data/SUN/images/e/elevator/door/sun_ajrpxszcjhnqeaiw.jpg
    data/SUN/images/e/elevator/door/sun_agebnbbndqxextmq.jpg
    data/SUN/images/e/elevator/door/sun_aacfxczwjbidyntb.jpg
    data/SUN/images/e/elevator/door/sun_atqcpxguurfkuhnq.jpg
    data/SUN/images/e/elevator/door/sun_agbvztgaxsufwpoi.jpg
    data/SUN/images/e/elevator/door/sun_aazrybiwsixsdees.jpg
    data/SUN/images/e/elevator/door/sun_arwcllogoqkgoopn.jpg
    data/SUN/images/e/elevator/door/sun_aippxmqqwcgoslvn.jpg
    data/SUN/images/e/elevator/door/sun_aopyxsahoqlbzqod.jpg
    data/SUN/images/e/elevator/door/sun_aihgvutljuuztats.jpg
    data/SUN/images/e/elevator/door/sun_aungxakojlstxfiq.jpg
    data/SUN/images/e/elevator/door/sun_aiimgydrhbkpivnz.jpg
    data/SUN/images/e/elevator/door/sun_aebnzscpgoyfbpde.jpg
    data/SUN/images/e/elevator/door/sun_agkepmegcalzsxra.jpg
    data/SUN/images/e/elevator/door/sun_abmwvmkvtlwialrf.jpg
    data/SUN/images/e/elevator/door/sun_akrucpvmadhvozdb.jpg
    data/SUN/images/e/elevator/door/sun_aumqmiplggjdxcis.jpg
    data/SUN/images/e/elevator/door/sun_amvyzgieqllyakod.jpg
    data/SUN/images/e/elevator/door/sun_arbwqqhltujmyynn.jpg
    data/SUN/images/e/elevator/door/sun_agxkotjrrbksldzt.jpg
    data/SUN/images/e/elevator/interior/sun_ageumvenmgoqnpwa.jpg
    data/SUN/images/e/elevator/interior/sun_arraonhlqtewoyph.jpg
    data/SUN/images/e/elevator/interior/sun_apjgxjcrqnoqplzw.jpg
    data/SUN/images/e/elevator/interior/sun_amlmhqphmehxbimr.jpg
    data/SUN/images/e/elevator/interior/sun_arlvrpsoubltdjpf.jpg
    data/SUN/images/e/elevator/interior/sun_amicbywtgzbygxyr.jpg
    data/SUN/images/e/elevator/interior/sun_aethhvoqotahvwvp.jpg
    data/SUN/images/e/elevator/interior/sun_aiiyunbqgurlzmgp.jpg
    data/SUN/images/e/elevator/interior/sun_adoglxpihhzmvarn.jpg
    data/SUN/images/e/elevator/interior/sun_akmqdfrgxxzcigru.jpg
    data/SUN/images/e/elevator/interior/sun_amivdohodflzttam.jpg
    data/SUN/images/e/elevator/interior/sun_aqiqmumxrtcrcmrk.jpg
    data/SUN/images/e/elevator/interior/sun_adghtxezglgfnsml.jpg
    data/SUN/images/e/elevator/interior/sun_aglxtfxcaotvscoh.jpg
    data/SUN/images/e/elevator/interior/sun_ambxhevercuirpnf.jpg
    data/SUN/images/e/elevator/interior/sun_ajcrushbwnlmhotl.jpg
    data/SUN/images/e/elevator/interior/sun_alqbzfrdxdjysqdk.jpg
    data/SUN/images/e/elevator/interior/sun_afcnkbtdoeyylfjx.jpg
    data/SUN/images/e/elevator/interior/sun_ahmiklalbrqxilla.jpg
    data/SUN/images/e/elevator/interior/sun_apjzntryvcmobxdi.jpg
    data/SUN/images/e/elevator/interior/sun_akxeqjniqgizktxt.jpg
    data/aPY/VOCdevkit/VOC2008/ImageSets/Segmentation/val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Segmentation/test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Segmentation/train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Segmentation/trainval.txt
    data/SUN/images/e/elevator/freight_elevator/sun_annndzsubdtfjill.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_avfismvtngmhbdur.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_apvckdyqwhzgxbhd.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_acjghktkrtvlfvms.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_akdogrektdiuohce.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_amxjqaluekdvvwsa.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_atmgeqstzgxyropz.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_aldtfsjgucnsectf.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_aqkhcwtarswwtoeo.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_asblrkgyxgxdijio.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_ajbnyvdpqovxgoku.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_amtrwubfrdemnyvx.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_aqmifisvgpexsjqd.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_astpugmwluyshguo.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_aoujihreqfruwlhx.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_aarfwombgbngvjto.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_alenaudspacoinql.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_aqijpkpcqofbkyhc.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_anyttoqgakxhfnpy.jpg
    data/SUN/images/e/elevator/freight_elevator/sun_abwepcgmicigmpdv.jpg
    data/aPY/VOCdevkit/VOC2008/ImageSets/Layout/val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Layout/test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Layout/train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Layout/trainval.txt
    data/SUN/images/e/embassy/sun_ajibdgwkjnvozavb.jpg
    data/SUN/images/e/embassy/sun_aduiygwsavxnsaxd.jpg
    data/SUN/images/e/embassy/sun_aiqbixwvqsapvjcn.jpg
    data/SUN/images/e/embassy/sun_acnqigkjjmquumlc.jpg
    data/SUN/images/e/embassy/sun_aezlbulzajebwgte.jpg
    data/SUN/images/e/embassy/sun_ajqwplrdvnllgysw.jpg
    data/SUN/images/e/embassy/sun_anlxfulmvnloyjmo.jpg
    data/SUN/images/e/embassy/sun_algwytjodgvvughe.jpg
    data/SUN/images/e/embassy/sun_aawdiwdptxiuuedm.jpg
    data/SUN/images/e/embassy/sun_aliwxafwkthkwuin.jpg
    data/SUN/images/e/embassy/sun_akbqufeozfughoss.jpg
    data/SUN/images/e/embassy/sun_asundkmeckcdyfqp.jpg
    data/SUN/images/e/embassy/sun_abmagwcfedvnlxoi.jpg
    data/SUN/images/e/embassy/sun_acfxhkuchdjbnfiw.jpg
    data/SUN/images/e/embassy/sun_anivcmcvpiljtjew.jpg
    data/SUN/images/e/embassy/sun_aaawvlrqzhhgypvf.jpg
    data/SUN/images/e/embassy/sun_atmbothblhqelqwi.jpg
    data/SUN/images/e/embassy/sun_amowqbkopbemvzgh.jpg
    data/SUN/images/e/embassy/sun_aeejhzqvmmqxbjgn.jpg
    data/SUN/images/e/embassy/sun_asultqbcqrvygqju.jpg
    data/SUN/images/e/earth_fissure/sun_dtnbsmdqhovumuzh.jpg
    data/SUN/images/e/earth_fissure/sun_dgvosrssdhmexurn.jpg
    data/SUN/images/e/earth_fissure/sun_dclzmraaxxbrnxlv.jpg
    data/SUN/images/e/earth_fissure/sun_ddzjpzhthgbasedh.jpg
    data/SUN/images/e/earth_fissure/sun_ddhftslzdbdabuam.jpg
    data/SUN/images/e/earth_fissure/sun_dnolkkkrxymlfwyy.jpg
    data/SUN/images/e/earth_fissure/sun_dfitsrwqskyxkaxs.jpg
    data/SUN/images/e/earth_fissure/sun_dcenigqtsogapzwe.jpg
    data/SUN/images/e/earth_fissure/sun_dxzmgcakgxkidtfy.jpg
    data/SUN/images/e/earth_fissure/sun_dbzffzbfnwwufybx.jpg
    data/SUN/images/e/earth_fissure/sun_dvmhjfqtdbbkyhjh.jpg
    data/SUN/images/e/earth_fissure/sun_dmcmnfbustcxkdlm.jpg
    data/SUN/images/e/earth_fissure/sun_dwupwthndtsdlfay.jpg
    data/SUN/images/e/earth_fissure/sun_dbtrzpblubhwlqwu.jpg
    data/SUN/images/e/earth_fissure/sun_dsgksyvvnizdbyru.jpg
    data/SUN/images/e/earth_fissure/sun_dpvblventqiiolgv.jpg
    data/SUN/images/e/earth_fissure/sun_dgletyhysvxhqnoo.jpg
    data/SUN/images/e/earth_fissure/sun_dkerisxuxnraejsp.jpg
    data/SUN/images/e/earth_fissure/sun_dikybdvxmkxbjcmj.jpg
    data/SUN/images/e/earth_fissure/sun_ddrfmtbmnbtjswpt.jpg
    data/SUN/images/e/estuary/sun_bshjzcbhgxoczqxe.jpg
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/car_train.txt
    data/SUN/images/e/estuary/sun_bgsdtbrjdzjbuuso.jpg
    data/SUN/images/e/estuary/sun_bftkwavhmmzzcxhy.jpg
    data/SUN/images/e/estuary/sun_apdmypavufkiaplw.jpg
    data/SUN/images/e/estuary/sun_bffetjbeuxajcvnq.jpg
    data/SUN/images/e/estuary/sun_bcgwjeujnneykmbd.jpg
    data/SUN/images/e/estuary/sun_bsnhetuyqcediiik.jpg
    data/SUN/images/e/estuary/sun_bfndasonamlaolbl.jpg
    data/SUN/images/e/estuary/sun_bbdxswihrpikrpzd.jpg
    data/SUN/images/e/estuary/sun_bqxoatnezwwbikky.jpg
    data/SUN/images/e/estuary/sun_bpiethrahywlwcyx.jpg
    data/SUN/images/e/estuary/sun_apkpgmhfajbpjphr.jpg
    data/SUN/images/e/estuary/sun_bnclfvlhqfdnongo.jpg
    data/SUN/images/e/estuary/sun_aagwzzjdcglggavf.jpg
    data/SUN/images/e/estuary/sun_bsjlsmtkmppanppf.jpg
    data/SUN/images/e/estuary/sun_bnshvhjphxqatnyx.jpg
    data/SUN/images/e/estuary/sun_bduycgqnxhaukqbx.jpg
    data/SUN/images/e/estuary/sun_aywgdhvkbpimtrve.jpg
    data/SUN/images/e/estuary/sun_bihfquxprjecdigc.jpg
    data/SUN/images/e/estuary/sun_apkeqvuqvhipxuur.jpg
    data/SUN/images/e/estuary/sun_bhdmijsqgtqkecgk.jpg
    data/SUN/images/e/exhibition_hall/sun_aetazaadfpzuwhrb.jpg
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/aeroplane_trainval.txt
    data/SUN/images/e/exhibition_hall/sun_adocxlnykxfmopio.jpg
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001239.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000589.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008571.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002669.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007908.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005358.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003195.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002852.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001586.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004838.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008222.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003525.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009209.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008323.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002972.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007534.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009756.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002258.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006678.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000121.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003207.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002269.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000515.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000567.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001733.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009911.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000853.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007772.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006232.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004405.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005314.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001289.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005637.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000309.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002545.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009245.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006802.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000919.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004121.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007649.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006900.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005460.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001397.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009346.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001308.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007341.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005509.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000243.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007417.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006182.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004510.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009348.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006117.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007818.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005525.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004754.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003451.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009764.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004052.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006445.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002445.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004644.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009807.png
    data/SUN/images/e/exhibition_hall/sun_akjffxrjxjcklpvf.jpg
    data/SUN/images/e/exhibition_hall/sun_airrqvmgydigwjsw.jpg
    data/SUN/images/e/exhibition_hall/sun_aqfjlblftaxrchof.jpg
    data/SUN/images/e/exhibition_hall/sun_akyfnboqdjmdxhnc.jpg
    data/SUN/images/e/exhibition_hall/sun_avbivallhyxkmnly.jpg
    data/SUN/images/e/exhibition_hall/sun_ahpnfzovndzwkwly.jpg
    data/SUN/images/e/exhibition_hall/sun_akqrcnhhzfkpovcv.jpg
    data/SUN/images/e/exhibition_hall/sun_agmbdlbrdqbnyfuk.jpg
    data/SUN/images/e/exhibition_hall/sun_aidwfspdbtpwmrsc.jpg
    data/SUN/images/e/exhibition_hall/sun_afibuetsbqfhhgri.jpg
    data/SUN/images/e/exhibition_hall/sun_aisxnkeolnxujubm.jpg
    data/SUN/images/e/exhibition_hall/sun_awzaseviqbwwesem.jpg
    data/SUN/images/e/exhibition_hall/sun_aqpyplkcanrgadvt.jpg
    data/SUN/images/e/exhibition_hall/sun_agonhldblfnytcjw.jpg
    data/SUN/images/e/exhibition_hall/sun_aizrtehrtafvfrlt.jpg
    data/SUN/images/e/exhibition_hall/sun_ajhxfnrtpoeezabc.jpg
    data/SUN/images/e/exhibition_hall/sun_abtiruceclnbyuvu.jpg
    data/SUN/images/e/exhibition_hall/sun_avsvcrqvfjstvefv.jpg
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006065.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001498.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002368.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/tvmonitor_val.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004769.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009088.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cat_val.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007849.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/motorbike_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/boat_trainval.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006704.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/boat_val.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006408.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006866.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005608.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004607.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005696.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005058.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002895.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000676.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009068.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008575.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007130.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001249.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006339.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007447.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004830.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001487.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002900.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003593.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005248.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008084.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004483.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005544.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004856.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003742.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002914.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003051.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002358.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001399.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008301.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000837.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002426.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002105.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/dog_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/motorbike_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/car_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bird_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bus_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/horse_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sheep_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/pottedplant_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/diningtable_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/person_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/person_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/chair_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bus_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bus_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/train_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bird_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/motorbike_trainval.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001423.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/boat_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/pottedplant_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/tvmonitor_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_007930.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bicycle_val.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000657.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/car_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003373.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/horse_val.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005633.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000700.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001698.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001872.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006134.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000725.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005145.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002160.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005600.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001106.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000170.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000645.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005262.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008670.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000332.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000822.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001408.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005676.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001787.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000392.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004869.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004948.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/aeroplane_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cat_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cow_train.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_003709.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sheep_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/dog_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004241.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/horse_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009687.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bicycle_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009889.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sheep_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/train_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/dog_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/train_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/boat_train.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009562.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bus_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004441.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/person_trainval.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000491.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/tvmonitor_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cat_trainval.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004259.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sofa_val.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002361.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/aeroplane_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/trainval.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009649.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000836.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005114.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008746.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009258.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005844.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000811.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_004627.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001028.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000068.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000182.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008980.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001078.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001231.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000862.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001135.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_003585.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_007497.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003565.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000217.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003541.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002467.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005006.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006028.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000464.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005915.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_006345.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001568.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008476.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004069.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008801.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001857.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_009139.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005130.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000042.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008682.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_003913.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003205.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001208.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001299.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_001225.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002400.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_003885.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003611.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002936.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_004911.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001874.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002132.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_008392.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005878.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_008945.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_005691.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001821.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sofa_test.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_002120.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/diningtable_train.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001640.png
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/car_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bottle_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/pottedplant_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/aeroplane_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bird_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/diningtable_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/person_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/chair_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sheep_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bottle_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/diningtable_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cow_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/dog_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/train_val.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/horse_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sofa_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bird_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bicycle_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/sofa_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bicycle_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/tvmonitor_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cow_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/chair_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/pottedplant_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cat_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bottle_train.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/motorbike_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/bottle_test.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/cow_trainval.txt
    data/aPY/VOCdevkit/VOC2008/ImageSets/Main/chair_trainval.txt
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_002704.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_005547.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_001741.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_003134.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000760.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_006409.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2007_000528.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_003110.png
    data/aPY/VOCdevkit/VOC2008/SegmentationObject/2008_000238.png
    ... command output truncated for persistence ...
    OCO_train2014_000000105863.jpg
    data/train2014/COCO_train2014_000000083382.jpg
    data/train2014/COCO_train2014_000000485187.jpg
    data/train2014/COCO_train2014_000000154343.jpg
    data/train2014/COCO_train2014_000000177550.jpg
    data/train2014/COCO_train2014_000000003579.jpg
    data/train2014/COCO_train2014_000000147976.jpg
    data/train2014/COCO_train2014_000000079552.jpg
    data/train2014/COCO_train2014_000000540110.jpg
    data/train2014/COCO_train2014_000000253419.jpg
    data/train2014/COCO_train2014_000000100599.jpg
    data/train2014/COCO_train2014_000000098989.jpg
    data/train2014/COCO_train2014_000000348573.jpg
    data/train2014/COCO_train2014_000000555088.jpg
    data/train2014/COCO_train2014_000000002369.jpg
    data/train2014/COCO_train2014_000000437318.jpg
    data/train2014/COCO_train2014_000000449201.jpg
    data/train2014/COCO_train2014_000000330614.jpg
    data/train2014/COCO_train2014_000000470647.jpg
    data/train2014/COCO_train2014_000000239752.jpg
    data/train2014/COCO_train2014_000000059556.jpg
    data/train2014/COCO_train2014_000000145311.jpg
    data/train2014/COCO_train2014_000000022012.jpg
    data/train2014/COCO_train2014_000000324107.jpg
    data/train2014/COCO_train2014_000000280596.jpg
    data/train2014/COCO_train2014_000000248355.jpg
    data/train2014/COCO_train2014_000000093971.jpg
    data/train2014/COCO_train2014_000000316471.jpg
    data/train2014/COCO_train2014_000000459147.jpg
    data/train2014/COCO_train2014_000000105339.jpg
    data/train2014/COCO_train2014_000000560384.jpg
    data/train2014/COCO_train2014_000000275709.jpg
    data/train2014/COCO_train2014_000000281910.jpg
    data/train2014/COCO_train2014_000000130666.jpg
    data/train2014/COCO_train2014_000000523484.jpg
    data/train2014/COCO_train2014_000000108034.jpg
    data/train2014/COCO_train2014_000000180827.jpg
    data/train2014/COCO_train2014_000000058929.jpg
    data/train2014/COCO_train2014_000000506231.jpg
    data/train2014/COCO_train2014_000000169945.jpg
    data/train2014/COCO_train2014_000000000560.jpg
    data/train2014/COCO_train2014_000000013754.jpg
    data/train2014/COCO_train2014_000000294421.jpg
    data/train2014/COCO_train2014_000000368871.jpg
    data/train2014/COCO_train2014_000000261885.jpg
    data/train2014/COCO_train2014_000000286138.jpg
    data/train2014/COCO_train2014_000000516481.jpg
    data/train2014/COCO_train2014_000000365003.jpg
    data/train2014/COCO_train2014_000000516726.jpg
    data/train2014/COCO_train2014_000000305170.jpg
    data/train2014/COCO_train2014_000000439402.jpg
    data/train2014/COCO_train2014_000000356257.jpg
    data/train2014/COCO_train2014_000000122419.jpg
    data/train2014/COCO_train2014_000000097563.jpg
    data/train2014/COCO_train2014_000000554992.jpg
    data/train2014/COCO_train2014_000000218784.jpg
    data/train2014/COCO_train2014_000000536054.jpg
    data/train2014/COCO_train2014_000000194459.jpg
    data/train2014/COCO_train2014_000000493742.jpg
    data/train2014/COCO_train2014_000000262308.jpg
    data/train2014/COCO_train2014_000000162767.jpg
    data/train2014/COCO_train2014_000000321127.jpg
    data/train2014/COCO_train2014_000000052626.jpg
    data/train2014/COCO_train2014_000000286619.jpg
    data/train2014/COCO_train2014_000000501718.jpg
    data/train2014/COCO_train2014_000000357859.jpg
    data/train2014/COCO_train2014_000000518509.jpg
    data/train2014/COCO_train2014_000000185087.jpg
    data/train2014/COCO_train2014_000000011775.jpg
    data/train2014/COCO_train2014_000000107705.jpg
    data/train2014/COCO_train2014_000000429233.jpg
    data/train2014/COCO_train2014_000000249611.jpg
    data/train2014/COCO_train2014_000000442872.jpg
    data/train2014/COCO_train2014_000000217216.jpg
    data/train2014/COCO_train2014_000000294236.jpg
    data/train2014/COCO_train2014_000000547131.jpg
    data/train2014/COCO_train2014_000000353056.jpg
    data/train2014/COCO_train2014_000000473706.jpg
    data/train2014/COCO_train2014_000000203818.jpg
    data/train2014/COCO_train2014_000000169249.jpg
    data/train2014/COCO_train2014_000000048824.jpg
    data/train2014/COCO_train2014_000000309364.jpg
    data/train2014/COCO_train2014_000000193454.jpg
    data/train2014/COCO_train2014_000000530945.jpg
    data/train2014/COCO_train2014_000000021462.jpg
    data/train2014/COCO_train2014_000000255044.jpg
    data/train2014/COCO_train2014_000000123038.jpg
    data/train2014/COCO_train2014_000000179550.jpg
    data/train2014/COCO_train2014_000000505626.jpg
    data/train2014/COCO_train2014_000000324708.jpg
    data/train2014/COCO_train2014_000000015107.jpg
    data/train2014/COCO_train2014_000000483138.jpg
    data/train2014/COCO_train2014_000000380665.jpg
    data/train2014/COCO_train2014_000000505687.jpg
    data/train2014/COCO_train2014_000000248023.jpg
    data/train2014/COCO_train2014_000000499142.jpg
    data/train2014/COCO_train2014_000000511580.jpg
    data/train2014/COCO_train2014_000000133912.jpg
    data/train2014/COCO_train2014_000000009231.jpg
    data/train2014/COCO_train2014_000000425691.jpg
    data/train2014/COCO_train2014_000000084383.jpg
    data/train2014/COCO_train2014_000000221621.jpg
    data/train2014/COCO_train2014_000000138807.jpg
    data/train2014/COCO_train2014_000000152514.jpg
    data/train2014/COCO_train2014_000000539335.jpg
    data/train2014/COCO_train2014_000000564050.jpg
    data/train2014/COCO_train2014_000000333634.jpg
    data/train2014/COCO_train2014_000000393396.jpg
    data/train2014/COCO_train2014_000000415288.jpg
    data/train2014/COCO_train2014_000000320008.jpg
    data/train2014/COCO_train2014_000000095081.jpg
    data/train2014/COCO_train2014_000000349164.jpg
    data/train2014/COCO_train2014_000000114978.jpg
    data/train2014/COCO_train2014_000000374598.jpg
    data/train2014/COCO_train2014_000000162641.jpg
    data/train2014/COCO_train2014_000000348951.jpg
    data/train2014/COCO_train2014_000000069314.jpg
    data/train2014/COCO_train2014_000000218985.jpg
    data/train2014/COCO_train2014_000000512731.jpg
    data/train2014/COCO_train2014_000000109568.jpg
    data/train2014/COCO_train2014_000000142098.jpg
    data/train2014/COCO_train2014_000000052192.jpg
    data/train2014/COCO_train2014_000000153067.jpg
    data/train2014/COCO_train2014_000000429448.jpg
    data/train2014/COCO_train2014_000000150867.jpg
    data/train2014/COCO_train2014_000000082495.jpg
    data/train2014/COCO_train2014_000000277916.jpg
    data/train2014/COCO_train2014_000000209386.jpg
    data/train2014/COCO_train2014_000000234352.jpg
    data/train2014/COCO_train2014_000000332915.jpg
    data/train2014/COCO_train2014_000000405288.jpg
    data/train2014/COCO_train2014_000000447278.jpg
    data/train2014/COCO_train2014_000000107357.jpg
    data/train2014/COCO_train2014_000000069302.jpg
    data/train2014/COCO_train2014_000000027089.jpg
    data/train2014/COCO_train2014_000000040938.jpg
    data/train2014/COCO_train2014_000000129888.jpg
    data/train2014/COCO_train2014_000000002083.jpg
    data/train2014/COCO_train2014_000000281034.jpg
    data/train2014/COCO_train2014_000000132959.jpg
    data/train2014/COCO_train2014_000000125193.jpg
    data/train2014/COCO_train2014_000000199011.jpg
    data/train2014/COCO_train2014_000000548175.jpg
    data/train2014/COCO_train2014_000000523151.jpg
    data/train2014/COCO_train2014_000000334872.jpg
    data/train2014/COCO_train2014_000000241161.jpg
    data/train2014/COCO_train2014_000000472405.jpg
    data/train2014/COCO_train2014_000000263450.jpg
    data/train2014/COCO_train2014_000000379612.jpg
    data/train2014/COCO_train2014_000000221937.jpg
    data/train2014/COCO_train2014_000000337297.jpg
    data/train2014/COCO_train2014_000000175781.jpg
    data/train2014/COCO_train2014_000000209232.jpg
    data/train2014/COCO_train2014_000000033517.jpg
    data/train2014/COCO_train2014_000000069054.jpg
    data/train2014/COCO_train2014_000000184843.jpg
    data/train2014/COCO_train2014_000000154895.jpg
    data/train2014/COCO_train2014_000000177245.jpg
    data/train2014/COCO_train2014_000000202447.jpg
    data/train2014/COCO_train2014_000000495677.jpg
    data/train2014/COCO_train2014_000000232161.jpg
    data/train2014/COCO_train2014_000000465740.jpg
    data/train2014/COCO_train2014_000000091989.jpg
    data/train2014/COCO_train2014_000000360575.jpg
    data/train2014/COCO_train2014_000000251045.jpg
    data/train2014/COCO_train2014_000000447297.jpg
    data/train2014/COCO_train2014_000000115126.jpg
    data/train2014/COCO_train2014_000000103250.jpg
    data/train2014/COCO_train2014_000000105582.jpg
    data/train2014/COCO_train2014_000000116827.jpg
    data/train2014/COCO_train2014_000000229940.jpg
    data/train2014/COCO_train2014_000000058834.jpg
    data/train2014/COCO_train2014_000000218854.jpg
    data/train2014/COCO_train2014_000000457720.jpg
    data/train2014/COCO_train2014_000000324689.jpg
    data/train2014/COCO_train2014_000000074601.jpg
    data/train2014/COCO_train2014_000000196108.jpg
    data/train2014/COCO_train2014_000000296978.jpg
    data/train2014/COCO_train2014_000000577207.jpg
    data/train2014/COCO_train2014_000000290774.jpg
    data/train2014/COCO_train2014_000000506316.jpg
    data/train2014/COCO_train2014_000000251016.jpg
    data/train2014/COCO_train2014_000000075230.jpg
    data/train2014/COCO_train2014_000000273650.jpg
    data/train2014/COCO_train2014_000000095079.jpg
    data/train2014/COCO_train2014_000000464257.jpg
    data/train2014/COCO_train2014_000000188100.jpg
    data/train2014/COCO_train2014_000000558278.jpg
    data/train2014/COCO_train2014_000000115862.jpg
    data/train2014/COCO_train2014_000000526793.jpg
    data/train2014/COCO_train2014_000000247320.jpg
    data/train2014/COCO_train2014_000000346678.jpg
    data/train2014/COCO_train2014_000000299931.jpg
    data/train2014/COCO_train2014_000000321711.jpg
    data/train2014/COCO_train2014_000000060980.jpg
    data/train2014/COCO_train2014_000000133540.jpg
    data/train2014/COCO_train2014_000000249791.jpg
    data/train2014/COCO_train2014_000000188113.jpg
    data/train2014/COCO_train2014_000000213780.jpg
    data/train2014/COCO_train2014_000000097914.jpg
    data/train2014/COCO_train2014_000000464240.jpg
    data/train2014/COCO_train2014_000000183350.jpg
    data/train2014/COCO_train2014_000000449291.jpg
    data/train2014/COCO_train2014_000000343432.jpg
    data/train2014/COCO_train2014_000000279697.jpg
    data/train2014/COCO_train2014_000000483272.jpg
    data/train2014/COCO_train2014_000000024372.jpg
    data/train2014/COCO_train2014_000000381684.jpg
    data/train2014/COCO_train2014_000000308350.jpg
    data/train2014/COCO_train2014_000000577759.jpg
    data/train2014/COCO_train2014_000000386715.jpg
    data/train2014/COCO_train2014_000000464322.jpg
    data/train2014/COCO_train2014_000000254228.jpg
    data/train2014/COCO_train2014_000000533258.jpg
    data/train2014/COCO_train2014_000000562876.jpg
    data/train2014/COCO_train2014_000000048270.jpg
    data/train2014/COCO_train2014_000000074794.jpg
    data/train2014/COCO_train2014_000000408016.jpg
    data/train2014/COCO_train2014_000000377213.jpg
    data/train2014/COCO_train2014_000000245517.jpg
    data/train2014/COCO_train2014_000000259811.jpg
    data/train2014/COCO_train2014_000000192816.jpg
    data/train2014/COCO_train2014_000000331331.jpg
    data/train2014/COCO_train2014_000000373679.jpg
    data/train2014/COCO_train2014_000000319905.jpg
    data/train2014/COCO_train2014_000000483692.jpg
    data/train2014/COCO_train2014_000000477555.jpg
    data/train2014/COCO_train2014_000000549962.jpg
    data/train2014/COCO_train2014_000000066586.jpg
    data/train2014/COCO_train2014_000000420300.jpg
    data/train2014/COCO_train2014_000000321338.jpg
    data/train2014/COCO_train2014_000000291280.jpg
    data/train2014/COCO_train2014_000000305056.jpg
    data/train2014/COCO_train2014_000000256155.jpg
    data/train2014/COCO_train2014_000000013160.jpg
    data/train2014/COCO_train2014_000000289344.jpg
    data/train2014/COCO_train2014_000000146128.jpg
    data/train2014/COCO_train2014_000000390840.jpg
    data/train2014/COCO_train2014_000000148859.jpg
    data/train2014/COCO_train2014_000000558765.jpg
    data/train2014/COCO_train2014_000000457656.jpg
    data/train2014/COCO_train2014_000000224272.jpg
    data/train2014/COCO_train2014_000000518754.jpg
    data/train2014/COCO_train2014_000000576727.jpg
    data/train2014/COCO_train2014_000000176671.jpg
    data/train2014/COCO_train2014_000000483453.jpg
    data/train2014/COCO_train2014_000000287303.jpg
    data/train2014/COCO_train2014_000000311796.jpg
    data/train2014/COCO_train2014_000000259288.jpg
    data/train2014/COCO_train2014_000000144796.jpg
    data/train2014/COCO_train2014_000000056109.jpg
    data/train2014/COCO_train2014_000000311066.jpg
    data/train2014/COCO_train2014_000000197584.jpg
    data/train2014/COCO_train2014_000000223203.jpg
    data/train2014/COCO_train2014_000000014083.jpg
    data/train2014/COCO_train2014_000000462712.jpg
    data/train2014/COCO_train2014_000000496619.jpg
    data/train2014/COCO_train2014_000000418115.jpg
    data/train2014/COCO_train2014_000000119267.jpg
    data/train2014/COCO_train2014_000000271469.jpg
    data/train2014/COCO_train2014_000000307240.jpg
    data/train2014/COCO_train2014_000000467358.jpg
    data/train2014/COCO_train2014_000000276770.jpg
    data/train2014/COCO_train2014_000000082901.jpg
    data/train2014/COCO_train2014_000000537316.jpg
    data/train2014/COCO_train2014_000000536278.jpg
    data/train2014/COCO_train2014_000000224182.jpg
    data/train2014/COCO_train2014_000000281160.jpg
    data/train2014/COCO_train2014_000000153845.jpg
    data/train2014/COCO_train2014_000000356071.jpg
    data/train2014/COCO_train2014_000000177763.jpg
    data/train2014/COCO_train2014_000000338766.jpg
    data/train2014/COCO_train2014_000000118918.jpg
    data/train2014/COCO_train2014_000000291841.jpg
    data/train2014/COCO_train2014_000000513541.jpg
    data/train2014/COCO_train2014_000000054427.jpg
    data/train2014/COCO_train2014_000000277726.jpg
    data/train2014/COCO_train2014_000000195725.jpg
    data/train2014/COCO_train2014_000000052484.jpg
    data/train2014/COCO_train2014_000000553441.jpg
    data/train2014/COCO_train2014_000000373252.jpg
    data/train2014/COCO_train2014_000000088929.jpg
    data/train2014/COCO_train2014_000000268192.jpg
    data/train2014/COCO_train2014_000000512572.jpg
    data/train2014/COCO_train2014_000000203794.jpg
    data/train2014/COCO_train2014_000000149726.jpg
    data/train2014/COCO_train2014_000000564599.jpg
    data/train2014/COCO_train2014_000000396030.jpg
    data/train2014/COCO_train2014_000000144951.jpg
    data/train2014/COCO_train2014_000000578103.jpg
    data/train2014/COCO_train2014_000000151499.jpg
    data/train2014/COCO_train2014_000000343953.jpg
    data/train2014/COCO_train2014_000000321852.jpg
    data/train2014/COCO_train2014_000000502730.jpg
    data/train2014/COCO_train2014_000000162213.jpg
    data/train2014/COCO_train2014_000000275412.jpg
    data/train2014/COCO_train2014_000000365320.jpg
    data/train2014/COCO_train2014_000000247925.jpg
    data/train2014/COCO_train2014_000000550019.jpg
    data/train2014/COCO_train2014_000000504191.jpg
    data/train2014/COCO_train2014_000000454814.jpg
    data/train2014/COCO_train2014_000000104273.jpg
    data/train2014/COCO_train2014_000000418173.jpg
    data/train2014/COCO_train2014_000000124812.jpg
    data/train2014/COCO_train2014_000000433568.jpg
    data/train2014/COCO_train2014_000000203768.jpg
    data/train2014/COCO_train2014_000000345863.jpg
    data/train2014/COCO_train2014_000000253219.jpg
    data/train2014/COCO_train2014_000000064799.jpg
    data/train2014/COCO_train2014_000000233587.jpg
    data/train2014/COCO_train2014_000000474668.jpg
    data/train2014/COCO_train2014_000000528657.jpg
    data/train2014/COCO_train2014_000000105386.jpg
    data/train2014/COCO_train2014_000000318496.jpg
    data/train2014/COCO_train2014_000000442078.jpg
    data/train2014/COCO_train2014_000000003935.jpg
    data/train2014/COCO_train2014_000000059118.jpg
    data/train2014/COCO_train2014_000000481974.jpg
    data/train2014/COCO_train2014_000000546447.jpg
    data/train2014/COCO_train2014_000000480391.jpg
    data/train2014/COCO_train2014_000000266680.jpg
    data/train2014/COCO_train2014_000000338704.jpg
    data/train2014/COCO_train2014_000000092975.jpg
    data/train2014/COCO_train2014_000000002055.jpg
    data/train2014/COCO_train2014_000000486013.jpg
    data/train2014/COCO_train2014_000000283809.jpg
    data/train2014/COCO_train2014_000000562849.jpg
    data/train2014/COCO_train2014_000000323478.jpg
    data/train2014/COCO_train2014_000000113501.jpg
    data/train2014/COCO_train2014_000000186315.jpg
    data/train2014/COCO_train2014_000000340688.jpg
    data/train2014/COCO_train2014_000000277524.jpg
    data/train2014/COCO_train2014_000000021475.jpg
    data/train2014/COCO_train2014_000000475932.jpg
    data/train2014/COCO_train2014_000000433723.jpg
    data/train2014/COCO_train2014_000000502232.jpg
    data/train2014/COCO_train2014_000000027215.jpg
    data/train2014/COCO_train2014_000000489302.jpg
    data/train2014/COCO_train2014_000000048226.jpg
    data/train2014/COCO_train2014_000000065588.jpg
    data/train2014/COCO_train2014_000000049603.jpg
    data/train2014/COCO_train2014_000000064202.jpg
    data/train2014/COCO_train2014_000000154637.jpg
    data/train2014/COCO_train2014_000000323424.jpg
    data/train2014/COCO_train2014_000000018542.jpg
    data/train2014/COCO_train2014_000000278938.jpg
    data/train2014/COCO_train2014_000000581055.jpg
    data/train2014/COCO_train2014_000000480451.jpg
    data/train2014/COCO_train2014_000000023812.jpg
    data/train2014/COCO_train2014_000000353607.jpg
    data/train2014/COCO_train2014_000000246713.jpg
    data/train2014/COCO_train2014_000000041658.jpg
    data/train2014/COCO_train2014_000000307280.jpg
    data/train2014/COCO_train2014_000000189353.jpg
    data/train2014/COCO_train2014_000000400313.jpg
    data/train2014/COCO_train2014_000000473912.jpg
    data/train2014/COCO_train2014_000000314681.jpg
    data/train2014/COCO_train2014_000000529665.jpg
    data/train2014/COCO_train2014_000000419714.jpg
    data/train2014/COCO_train2014_000000021595.jpg
    data/train2014/COCO_train2014_000000099892.jpg
    data/train2014/COCO_train2014_000000028868.jpg
    data/train2014/COCO_train2014_000000317730.jpg
    data/train2014/COCO_train2014_000000082874.jpg
    data/train2014/COCO_train2014_000000145116.jpg
    data/train2014/COCO_train2014_000000137288.jpg
    data/train2014/COCO_train2014_000000126921.jpg
    data/train2014/COCO_train2014_000000266083.jpg
    data/train2014/COCO_train2014_000000553894.jpg
    data/train2014/COCO_train2014_000000092674.jpg
    data/train2014/COCO_train2014_000000438762.jpg
    data/train2014/COCO_train2014_000000262897.jpg
    data/train2014/COCO_train2014_000000231164.jpg
    data/train2014/COCO_train2014_000000118227.jpg
    data/train2014/COCO_train2014_000000494733.jpg
    data/train2014/COCO_train2014_000000074887.jpg
    data/train2014/COCO_train2014_000000509620.jpg
    data/train2014/COCO_train2014_000000354309.jpg
    data/train2014/COCO_train2014_000000455482.jpg
    data/train2014/COCO_train2014_000000120782.jpg
    data/train2014/COCO_train2014_000000180307.jpg
    data/train2014/COCO_train2014_000000183788.jpg
    data/train2014/COCO_train2014_000000524500.jpg
    data/train2014/COCO_train2014_000000524338.jpg
    data/train2014/COCO_train2014_000000311644.jpg
    data/train2014/COCO_train2014_000000575497.jpg
    data/train2014/COCO_train2014_000000351002.jpg
    data/train2014/COCO_train2014_000000268617.jpg
    data/train2014/COCO_train2014_000000444952.jpg
    data/train2014/COCO_train2014_000000290265.jpg
    data/train2014/COCO_train2014_000000352877.jpg
    data/train2014/COCO_train2014_000000189306.jpg
    data/train2014/COCO_train2014_000000474721.jpg
    data/train2014/COCO_train2014_000000073823.jpg
    data/train2014/COCO_train2014_000000200263.jpg
    data/train2014/COCO_train2014_000000067849.jpg
    data/train2014/COCO_train2014_000000266058.jpg
    data/train2014/COCO_train2014_000000427886.jpg
    data/train2014/COCO_train2014_000000209701.jpg
    data/train2014/COCO_train2014_000000378203.jpg
    data/train2014/COCO_train2014_000000528006.jpg
    data/train2014/COCO_train2014_000000174440.jpg
    data/train2014/COCO_train2014_000000478410.jpg
    data/train2014/COCO_train2014_000000114880.jpg
    data/train2014/COCO_train2014_000000484405.jpg
    data/train2014/COCO_train2014_000000034551.jpg
    data/train2014/COCO_train2014_000000192954.jpg
    data/train2014/COCO_train2014_000000001200.jpg
    data/train2014/COCO_train2014_000000276332.jpg
    data/train2014/COCO_train2014_000000251754.jpg
    data/train2014/COCO_train2014_000000393721.jpg
    data/train2014/COCO_train2014_000000527229.jpg
    data/train2014/COCO_train2014_000000106799.jpg
    data/train2014/COCO_train2014_000000186099.jpg
    data/train2014/COCO_train2014_000000251626.jpg
    data/train2014/COCO_train2014_000000493829.jpg
    data/train2014/COCO_train2014_000000271873.jpg
    data/train2014/COCO_train2014_000000265161.jpg
    data/train2014/COCO_train2014_000000228572.jpg
    data/train2014/COCO_train2014_000000018233.jpg
    data/train2014/COCO_train2014_000000298315.jpg
    data/train2014/COCO_train2014_000000164772.jpg
    data/train2014/COCO_train2014_000000192221.jpg
    data/train2014/COCO_train2014_000000443525.jpg
    data/train2014/COCO_train2014_000000500228.jpg
    data/train2014/COCO_train2014_000000508634.jpg
    data/train2014/COCO_train2014_000000148129.jpg
    data/train2014/COCO_train2014_000000317040.jpg
    data/train2014/COCO_train2014_000000513299.jpg
    data/train2014/COCO_train2014_000000401044.jpg
    data/train2014/COCO_train2014_000000251663.jpg
    data/train2014/COCO_train2014_000000060018.jpg
    data/train2014/COCO_train2014_000000373109.jpg
    data/train2014/COCO_train2014_000000284835.jpg
    data/train2014/COCO_train2014_000000523894.jpg
    data/train2014/COCO_train2014_000000320979.jpg
    data/train2014/COCO_train2014_000000198993.jpg
    data/train2014/COCO_train2014_000000345145.jpg
    data/train2014/COCO_train2014_000000526966.jpg
    data/train2014/COCO_train2014_000000483534.jpg
    data/train2014/COCO_train2014_000000011010.jpg
    data/train2014/COCO_train2014_000000039859.jpg
    data/train2014/COCO_train2014_000000121525.jpg
    data/train2014/COCO_train2014_000000321402.jpg
    data/train2014/COCO_train2014_000000154652.jpg
    data/train2014/COCO_train2014_000000441172.jpg
    data/train2014/COCO_train2014_000000354036.jpg
    data/train2014/COCO_train2014_000000555861.jpg
    data/train2014/COCO_train2014_000000061463.jpg
    data/train2014/COCO_train2014_000000365582.jpg
    data/train2014/COCO_train2014_000000391568.jpg
    data/train2014/COCO_train2014_000000456705.jpg
    data/train2014/COCO_train2014_000000280338.jpg
    data/train2014/COCO_train2014_000000086248.jpg
    data/train2014/COCO_train2014_000000072556.jpg
    data/train2014/COCO_train2014_000000152701.jpg
    data/train2014/COCO_train2014_000000256057.jpg
    data/train2014/COCO_train2014_000000142711.jpg
    data/train2014/COCO_train2014_000000315813.jpg
    data/train2014/COCO_train2014_000000279648.jpg
    data/train2014/COCO_train2014_000000532175.jpg
    data/train2014/COCO_train2014_000000136962.jpg
    data/train2014/COCO_train2014_000000265139.jpg
    data/train2014/COCO_train2014_000000106107.jpg
    data/train2014/COCO_train2014_000000383368.jpg
    data/train2014/COCO_train2014_000000580257.jpg
    data/train2014/COCO_train2014_000000102987.jpg
    data/train2014/COCO_train2014_000000256037.jpg
    data/train2014/COCO_train2014_000000428595.jpg
    data/train2014/COCO_train2014_000000481354.jpg
    data/train2014/COCO_train2014_000000126737.jpg
    data/train2014/COCO_train2014_000000505402.jpg
    data/train2014/COCO_train2014_000000171099.jpg
    data/train2014/COCO_train2014_000000003897.jpg
    data/train2014/COCO_train2014_000000398285.jpg
    data/train2014/COCO_train2014_000000559877.jpg
    data/train2014/COCO_train2014_000000386161.jpg
    data/train2014/COCO_train2014_000000108110.jpg
    data/train2014/COCO_train2014_000000217221.jpg
    data/train2014/COCO_train2014_000000266386.jpg
    data/train2014/COCO_train2014_000000100319.jpg
    data/train2014/COCO_train2014_000000090006.jpg
    data/train2014/COCO_train2014_000000408854.jpg
    data/train2014/COCO_train2014_000000387480.jpg
    data/train2014/COCO_train2014_000000186799.jpg
    data/train2014/COCO_train2014_000000019906.jpg
    data/train2014/COCO_train2014_000000206584.jpg
    data/train2014/COCO_train2014_000000167994.jpg
    data/train2014/COCO_train2014_000000027742.jpg
    data/train2014/COCO_train2014_000000295578.jpg
    data/train2014/COCO_train2014_000000242620.jpg
    data/train2014/COCO_train2014_000000266569.jpg
    data/train2014/COCO_train2014_000000374955.jpg
    data/train2014/COCO_train2014_000000150195.jpg
    data/train2014/COCO_train2014_000000522755.jpg
    data/train2014/COCO_train2014_000000155138.jpg
    data/train2014/COCO_train2014_000000268592.jpg
    data/train2014/COCO_train2014_000000401681.jpg
    data/train2014/COCO_train2014_000000210684.jpg
    data/train2014/COCO_train2014_000000205150.jpg
    data/train2014/COCO_train2014_000000354569.jpg
    data/train2014/COCO_train2014_000000377488.jpg
    data/train2014/COCO_train2014_000000458617.jpg
    data/train2014/COCO_train2014_000000358396.jpg
    data/train2014/COCO_train2014_000000347697.jpg
    data/train2014/COCO_train2014_000000517869.jpg
    data/train2014/COCO_train2014_000000461211.jpg
    data/train2014/COCO_train2014_000000550660.jpg
    data/train2014/COCO_train2014_000000134712.jpg
    data/train2014/COCO_train2014_000000179964.jpg
    data/train2014/COCO_train2014_000000415500.jpg
    data/train2014/COCO_train2014_000000067414.jpg
    data/train2014/COCO_train2014_000000358029.jpg
    data/train2014/COCO_train2014_000000360020.jpg
    data/train2014/COCO_train2014_000000573967.jpg
    data/train2014/COCO_train2014_000000285400.jpg
    data/train2014/COCO_train2014_000000434092.jpg
    data/train2014/COCO_train2014_000000294954.jpg
    data/train2014/COCO_train2014_000000140946.jpg
    data/train2014/COCO_train2014_000000434141.jpg
    data/train2014/COCO_train2014_000000499267.jpg
    data/train2014/COCO_train2014_000000336804.jpg
    data/train2014/COCO_train2014_000000057138.jpg
    data/train2014/COCO_train2014_000000496210.jpg
    data/train2014/COCO_train2014_000000541109.jpg
    data/train2014/COCO_train2014_000000337883.jpg
    data/train2014/COCO_train2014_000000118920.jpg
    data/train2014/COCO_train2014_000000123824.jpg
    data/train2014/COCO_train2014_000000545209.jpg
    data/train2014/COCO_train2014_000000242709.jpg
    data/train2014/COCO_train2014_000000323311.jpg
    data/train2014/COCO_train2014_000000243028.jpg
    data/train2014/COCO_train2014_000000002093.jpg
    data/train2014/COCO_train2014_000000017651.jpg
    data/train2014/COCO_train2014_000000136088.jpg
    data/train2014/COCO_train2014_000000276006.jpg
    data/train2014/COCO_train2014_000000124477.jpg
    data/train2014/COCO_train2014_000000329543.jpg
    data/train2014/COCO_train2014_000000481868.jpg
    data/train2014/COCO_train2014_000000236015.jpg
    data/train2014/COCO_train2014_000000189469.jpg
    data/train2014/COCO_train2014_000000497821.jpg
    data/train2014/COCO_train2014_000000572536.jpg
    data/train2014/COCO_train2014_000000445007.jpg
    data/train2014/COCO_train2014_000000574538.jpg
    data/train2014/COCO_train2014_000000415475.jpg
    data/train2014/COCO_train2014_000000393442.jpg
    data/train2014/COCO_train2014_000000018418.jpg
    data/train2014/COCO_train2014_000000194043.jpg
    data/train2014/COCO_train2014_000000306791.jpg
    data/train2014/COCO_train2014_000000136338.jpg
    data/train2014/COCO_train2014_000000299496.jpg
    data/train2014/COCO_train2014_000000442443.jpg
    data/train2014/COCO_train2014_000000147568.jpg
    data/train2014/COCO_train2014_000000202891.jpg
    data/train2014/COCO_train2014_000000057491.jpg
    data/train2014/COCO_train2014_000000106293.jpg
    data/train2014/COCO_train2014_000000160653.jpg
    data/train2014/COCO_train2014_000000303735.jpg
    data/train2014/COCO_train2014_000000191918.jpg
    data/train2014/COCO_train2014_000000379743.jpg
    data/train2014/COCO_train2014_000000201508.jpg
    data/train2014/COCO_train2014_000000399774.jpg
    data/train2014/COCO_train2014_000000218603.jpg
    data/train2014/COCO_train2014_000000555654.jpg
    data/train2014/COCO_train2014_000000519929.jpg
    data/train2014/COCO_train2014_000000000194.jpg
    data/train2014/COCO_train2014_000000274319.jpg
    data/train2014/COCO_train2014_000000558221.jpg
    data/train2014/COCO_train2014_000000135796.jpg
    data/train2014/COCO_train2014_000000312877.jpg
    data/train2014/COCO_train2014_000000154023.jpg
    data/train2014/COCO_train2014_000000077899.jpg
    data/train2014/COCO_train2014_000000143629.jpg
    data/train2014/COCO_train2014_000000159972.jpg
    data/train2014/COCO_train2014_000000286166.jpg
    data/train2014/COCO_train2014_000000008553.jpg
    data/train2014/COCO_train2014_000000072549.jpg
    data/train2014/COCO_train2014_000000170313.jpg
    data/train2014/COCO_train2014_000000431169.jpg
    data/train2014/COCO_train2014_000000062257.jpg
    data/train2014/COCO_train2014_000000507824.jpg
    data/train2014/COCO_train2014_000000529823.jpg
    data/train2014/COCO_train2014_000000116398.jpg
    data/train2014/COCO_train2014_000000049491.jpg
    data/train2014/COCO_train2014_000000216324.jpg
    data/train2014/COCO_train2014_000000420713.jpg
    data/train2014/COCO_train2014_000000568208.jpg
    data/train2014/COCO_train2014_000000516782.jpg
    data/train2014/COCO_train2014_000000348047.jpg
    data/train2014/COCO_train2014_000000466964.jpg
    data/train2014/COCO_train2014_000000096339.jpg
    data/train2014/COCO_train2014_000000054903.jpg
    data/train2014/COCO_train2014_000000021750.jpg
    data/train2014/COCO_train2014_000000333571.jpg
    data/train2014/COCO_train2014_000000550536.jpg
    data/train2014/COCO_train2014_000000236769.jpg
    data/train2014/COCO_train2014_000000284684.jpg
    data/train2014/COCO_train2014_000000131044.jpg
    data/train2014/COCO_train2014_000000392964.jpg
    data/train2014/COCO_train2014_000000399294.jpg
    data/train2014/COCO_train2014_000000358674.jpg
    data/train2014/COCO_train2014_000000042166.jpg
    data/train2014/COCO_train2014_000000174406.jpg
    data/train2014/COCO_train2014_000000321030.jpg
    data/train2014/COCO_train2014_000000495750.jpg
    data/train2014/COCO_train2014_000000525944.jpg
    data/train2014/COCO_train2014_000000095774.jpg
    data/train2014/COCO_train2014_000000193051.jpg
    data/train2014/COCO_train2014_000000432417.jpg
    data/train2014/COCO_train2014_000000288712.jpg
    data/train2014/COCO_train2014_000000523114.jpg
    data/train2014/COCO_train2014_000000426762.jpg
    data/train2014/COCO_train2014_000000097519.jpg
    data/train2014/COCO_train2014_000000308915.jpg
    data/train2014/COCO_train2014_000000128093.jpg
    data/train2014/COCO_train2014_000000247110.jpg
    data/train2014/COCO_train2014_000000269934.jpg
    data/train2014/COCO_train2014_000000298160.jpg
    data/train2014/COCO_train2014_000000353622.jpg
    data/train2014/COCO_train2014_000000532509.jpg
    data/train2014/COCO_train2014_000000137202.jpg
    data/train2014/COCO_train2014_000000281091.jpg
    data/train2014/COCO_train2014_000000555318.jpg
    data/train2014/COCO_train2014_000000233193.jpg
    data/train2014/COCO_train2014_000000568023.jpg
    data/train2014/COCO_train2014_000000213535.jpg
    data/train2014/COCO_train2014_000000209752.jpg
    data/train2014/COCO_train2014_000000483187.jpg
    data/train2014/COCO_train2014_000000310633.jpg
    data/train2014/COCO_train2014_000000205362.jpg
    data/train2014/COCO_train2014_000000104349.jpg
    data/train2014/COCO_train2014_000000135016.jpg
    data/train2014/COCO_train2014_000000486413.jpg
    data/train2014/COCO_train2014_000000085081.jpg
    data/train2014/COCO_train2014_000000292146.jpg
    data/train2014/COCO_train2014_000000379518.jpg
    data/train2014/COCO_train2014_000000196524.jpg
    data/train2014/COCO_train2014_000000234713.jpg
    data/train2014/COCO_train2014_000000298468.jpg
    data/train2014/COCO_train2014_000000380325.jpg
    data/train2014/COCO_train2014_000000406208.jpg
    data/train2014/COCO_train2014_000000579374.jpg
    data/train2014/COCO_train2014_000000058684.jpg
    data/train2014/COCO_train2014_000000457478.jpg
    data/train2014/COCO_train2014_000000531444.jpg
    data/train2014/COCO_train2014_000000433013.jpg
    data/train2014/COCO_train2014_000000319903.jpg
    data/train2014/COCO_train2014_000000469181.jpg
    data/train2014/COCO_train2014_000000128299.jpg
    data/train2014/COCO_train2014_000000517140.jpg
    data/train2014/COCO_train2014_000000147459.jpg
    data/train2014/COCO_train2014_000000058627.jpg
    data/train2014/COCO_train2014_000000564708.jpg
    data/train2014/COCO_train2014_000000381602.jpg
    data/train2014/COCO_train2014_000000143501.jpg
    data/train2014/COCO_train2014_000000062481.jpg
    data/train2014/COCO_train2014_000000547192.jpg
    data/train2014/COCO_train2014_000000384836.jpg
    data/train2014/COCO_train2014_000000454452.jpg
    data/train2014/COCO_train2014_000000048825.jpg
    data/train2014/COCO_train2014_000000302052.jpg
    data/train2014/COCO_train2014_000000426355.jpg
    data/train2014/COCO_train2014_000000242081.jpg
    data/train2014/COCO_train2014_000000427972.jpg
    data/train2014/COCO_train2014_000000529842.jpg
    data/train2014/COCO_train2014_000000244933.jpg
    data/train2014/COCO_train2014_000000143258.jpg
    data/train2014/COCO_train2014_000000334742.jpg
    data/train2014/COCO_train2014_000000304999.jpg
    data/train2014/COCO_train2014_000000441095.jpg
    data/train2014/COCO_train2014_000000091708.jpg
    data/train2014/COCO_train2014_000000052494.jpg
    data/train2014/COCO_train2014_000000349561.jpg
    data/train2014/COCO_train2014_000000470911.jpg
    data/train2014/COCO_train2014_000000335039.jpg
    data/train2014/COCO_train2014_000000242537.jpg
    data/train2014/COCO_train2014_000000285618.jpg
    data/train2014/COCO_train2014_000000499771.jpg
    data/train2014/COCO_train2014_000000336333.jpg
    data/train2014/COCO_train2014_000000148385.jpg
    data/train2014/COCO_train2014_000000495832.jpg
    data/train2014/COCO_train2014_000000579394.jpg
    data/train2014/COCO_train2014_000000115692.jpg
    data/train2014/COCO_train2014_000000206198.jpg
    data/train2014/COCO_train2014_000000478076.jpg
    data/train2014/COCO_train2014_000000089128.jpg
    data/train2014/COCO_train2014_000000334432.jpg
    data/train2014/COCO_train2014_000000395480.jpg
    data/train2014/COCO_train2014_000000188826.jpg
    data/train2014/COCO_train2014_000000365027.jpg
    data/train2014/COCO_train2014_000000065161.jpg
    data/train2014/COCO_train2014_000000578226.jpg
    data/train2014/COCO_train2014_000000155741.jpg
    data/train2014/COCO_train2014_000000196611.jpg
    data/train2014/COCO_train2014_000000020168.jpg
    data/train2014/COCO_train2014_000000517047.jpg
    ✓ • 146ms

## Activity

    $ nl -ba clip_dataset.py
         1    """Object crops and candidate-label tokens for the OCL CLIP experiment."""
         2
         3    from __future__ import annotations
         4
         5    import json
         6    import math
         7    import pickle
         8    from collections import Counter
         9    from dataclasses import dataclass
        10    from pathlib import Path
        11    from typing import TYPE_CHECKING
        12
        13    import torch
        14    from PIL import Image
        15    from torch.utils.data import DataLoader, Dataset
        16
        17    if TYPE_CHECKING:
        18        from transformers import CLIPProcessor
        19
        20
        21    NUM_CATEGORIES = 10
        22    BATCH_SIZE = 4
        23
        24
        25    @dataclass(frozen=True)
        26    class ObjectInstance:
        27        image_name: str
        28        object_index: int
        29        category_id: int
        30        box: tuple[float, float, float, float] | None
        31        attribute_ids: tuple[int, ...]
        32        affordance_ids: tuple[int, ...]
        33
        34
        35    class OCLClipDataset(Dataset):
        36        """One sample per annotated object in the ten most frequent categories."""
        37
        38        def __init__(
        39            self,
        40            data_root: str | Path,
        41            processor: CLIPProcessor,
        42        ) -> None:
        43            self.data_root = Path(data_root).expanduser().resolve()
        44            self.image_processor = processor.image_processor
        45            resources = self.data_root / "resources"
        46
        47            def load_classes(name: str) -> list:
        48                with (resources / f"OCL_class_{name}.json").open(encoding="utf-8") as handle:
        49                    return json.load(handle)
        50
        51            object_classes = load_classes("object")
        52            self.attribute_classes = load_classes("attribute")
        53            self.affordance_classes = load_classes("affordance")
        54            annotations = []
        55            # Merge all supplied annotations into one evaluation dataset.
        56            for filename in ("OCL_annot_train.pkl", "OCL_annot_val.pkl", "OCL_annot_test.pkl"):
        57                annotation_path = resources / filename
        58                if not annotation_path.is_file():
        59                    raise FileNotFoundError(
        60                        f"Missing {annotation_path}. Extract data/resources/OCL_annot.tgz first."
        61                    )
        62                with annotation_path.open("rb") as handle:
        63                    annotations.extend(pickle.load(handle))
        64
        65            counts = Counter(obj["obj"] for image in annotations for obj in image["objects"])
        66            unknown = set(counts) - set(object_classes)
        67            if unknown:
        68                raise ValueError(f"Categories missing from OCL_class_object.json: {sorted(unknown)}")
        69            if len(counts) < NUM_CATEGORIES:
        70                raise ValueError(f"Need {NUM_CATEGORIES} categories; found {len(counts)}.")
        71            # Alphabetical tie-breaking makes class IDs independent of annotation order.
        72            ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        73            self.selection_category_counts = dict(ranked[:NUM_CATEGORIES])
        74            self.category_classes = list(self.selection_category_counts)
        75            category_to_id = {name: index for index, name in enumerate(self.category_classes)}
        76
        77            self.instances = [
        78                ObjectInstance(
        79                    image_name=image["name"],
        80                    object_index=object_index,
        81                    category_id=category_to_id[obj["obj"]],
        82                    box=tuple(obj["box"]) if "box" in obj else None,
        83                    attribute_ids=tuple(obj["attr"]),
        84                    affordance_ids=tuple(obj["aff"]),
        85                )
        86                for image in annotations
        87                for object_index, obj in enumerate(image["objects"])
        88                if obj["obj"] in category_to_id
        89            ]
        90            self.num_selected_objects = len(self.instances)
        91            self.excluded_objects = []
        92            valid_instances = []
        93            for instance in self.instances:
        94                box = instance.box
        95                if box is not None and (
        96                    len(box) != 4
        97                    or not all(math.isfinite(value) for value in box)
        98                    or box[2] <= box[0]
        99                    or box[3] <= box[1]
       100                ):
       101                    self.excluded_objects.append(
       102                        {
       103                            "image_name": instance.image_name,
       104                            "object_index": instance.object_index,
       105                            "category": self.category_classes[instance.category_id],
       106                            "box": repr(box),
       107                            "reason": "non-finite, malformed or non-positive-area box",
       108                        }
       109                    )
       110                else:
       111                    valid_instances.append(instance)
       112            self.instances = valid_instances
       113            if not self.instances:
       114                raise ValueError("No usable objects from the selected categories.")
       115            evaluation_counts = Counter(instance.category_id for instance in self.instances)
       116            self.evaluation_category_counts = {
       117                name: evaluation_counts[index] for index, name in enumerate(self.category_classes)
       118            }
       119            self.num_images = len({instance.image_name for instance in self.instances})
       120
       121            self.prompts = {
       122                "category": [f"a photo of a {name}." for name in self.category_classes],
       123                "attribute": [
       124                    f"a photo of an object that is {name}." for name in self.attribute_classes
       125                ],
       126                # Preserve original IDs: several affordances share a verb but differ in meaning.
       127                "affordance": [self._affordance_prompt(label) for label in self.affordance_classes],
       128            }
       129            self.text_inputs = {
       130                name: dict(
       131                    processor.tokenizer(
       132                        prompts,
       133                        padding=True,
       134                        truncation=True,
       135                        max_length=processor.tokenizer.model_max_length,
       136                        return_tensors="pt",
       137                    )
       138                )
       139                for name, prompts in self.prompts.items()
       140            }
       141
       142        @staticmethod
       143        def _affordance_prompt(label: dict) -> str:
       144            action = label["word"][0]
       145            definition = " ".join(label["define"].split())
       146            prompt = f"an object that enables the action {action}"
       147            return f"{prompt}: {definition}." if definition else f"{prompt}."
       148
       149        @staticmethod
       150        def _multi_hot(indices: tuple[int, ...], size: int) -> torch.Tensor:
       151            if any(index < 0 or index >= size for index in indices):
       152                raise ValueError(f"Label IDs outside [0, {size}): {indices}")
       153            target = torch.zeros(size, dtype=torch.float32)
       154            if indices:
       155                target[list(indices)] = 1.0
       156            return target
       157
       158        @staticmethod
       159        def _crop_object(image: Image.Image, instance: ObjectInstance) -> Image.Image:
       160            width, height = image.size
       161            box = instance.box if instance.box is not None else (0, 0, width, height)
       162            if len(box) != 4 or not all(math.isfinite(value) for value in box):
       163                raise ValueError(
       164                    f"Invalid box in {instance.image_name}, object {instance.object_index}: {box}"
       165                )
       166            # OCL already stores xyxy coordinates, including for its COCO images.
       167            left, top, right, bottom = box
       168            left, top = max(0, left), max(0, top)
       169            right, bottom = min(width, right), min(height, bottom)
       170            if right <= left or bottom <= top:
       171                raise ValueError(
       172                    f"Empty box in {instance.image_name}, object {instance.object_index}: {box}"
       173                )
       174            crop_box = (math.floor(left), math.floor(top), math.ceil(right), math.ceil(bottom))
       175            return image.crop(crop_box).convert("RGB")
       176
       177        def __len__(self) -> int:
       178            return len(self.instances)
       179
       180        def __getitem__(self, index: int) -> dict:
       181            instance = self.instances[index]
       182            image_path = self.data_root / instance.image_name
       183            if not image_path.is_file():
       184                raise FileNotFoundError(f"Missing OCL image: {image_path}")
       185            with Image.open(image_path) as image:
       186                crop = self._crop_object(image, instance)
       187            pixel_values = self.image_processor(images=crop, return_tensors="pt")["pixel_values"][0]
       188            return {
       189                "pixel_values": pixel_values,
       190                "category_id": instance.category_id,
       191                "attributes": self._multi_hot(instance.attribute_ids, len(self.attribute_classes)),
       192                "affordances": self._multi_hot(instance.affordance_ids, len(self.affordance_classes)),
       193                "image_name": instance.image_name,
       194                "object_index": instance.object_index,
       195            }
       196
       197
       198    def load_dataset(
       199        data_root: str | Path,
       200        processor: CLIPProcessor,
       201        num_workers: int = 4,
       202        pin_memory: bool = True,
       203    ) -> tuple[OCLClipDataset, DataLoader]:
       204        if num_workers < 0:
       205            raise ValueError("num_workers must be non-negative")
       206        dataset = OCLClipDataset(data_root, processor)
       207        loader = DataLoader(
       208            dataset,
       209            batch_size=BATCH_SIZE,
       210            shuffle=False,
       211            drop_last=False,
       212            num_workers=num_workers,
       213            pin_memory=pin_memory,
       214            persistent_workers=num_workers > 0,
       215        )
       216        return dataset, loader
    ✓ • 0ms

## Activity

    $ nl -ba clip_inference.py
         1    """Evaluate frozen Hugging Face CLIP on the ten largest OCL categories."""
         2
         3    from __future__ import annotations
         4
         5    import argparse
         6    import json
         7    import os
         8    from pathlib import Path
         9
        10    import numpy as np
        11    import torch
        12    import torch.nn.functional as F
        13    from sklearn.metrics import average_precision_score
        14    from torch.utils.data import DataLoader
        15    from tqdm.auto import tqdm
        16    from transformers import CLIPModel, CLIPProcessor
        17
        18    from clip_dataset import BATCH_SIZE, NUM_CATEGORIES, OCLClipDataset, load_dataset
        19
        20
        21    def load_model(
        22        model_name: str,
        23        device: torch.device,
        24        local_files_only: bool = False,
        25    ) -> tuple[CLIPModel, CLIPProcessor]:
        26        processor = CLIPProcessor.from_pretrained(
        27            model_name, local_files_only=local_files_only, use_fast=False
        28        )
        29        model = CLIPModel.from_pretrained(model_name, local_files_only=local_files_only)
        30        for parameter in model.parameters():
        31            parameter.requires_grad_(False)
        32        model.to(device)
        33        model.eval()
        34        return model, processor
        35
        36
        37    @torch.inference_mode()
        38    def encode_candidate_labels(
        39        model: CLIPModel,
        40        text_inputs: dict[str, dict[str, torch.Tensor]],
        41        device: torch.device,
        42    ) -> dict[str, torch.Tensor]:
        43        embeddings = {}
        44        for task, tokens in text_inputs.items():
        45            chunks = []
        46            for start in range(0, tokens["input_ids"].shape[0], 64):
        47                inputs = {key: value[start : start + 64].to(device) for key, value in tokens.items()}
        48                features = model.get_text_features(**inputs)
        49                chunks.append(F.normalize(features.float(), dim=-1))
        50            embeddings[task] = torch.cat(chunks)
        51        return embeddings
        52
        53
        54    def multilabel_metrics(
        55        targets: np.ndarray,
        56        scores: np.ndarray,
        57        labels: list,
        58    ) -> dict:
        59        if targets.ndim != 2 or targets.shape != scores.shape or targets.shape[1] != len(labels):
        60            raise ValueError(
        61                "Multi-label targets, scores and label vocabulary must have matching shapes."
        62            )
        63        if not np.isfinite(scores).all():
        64            raise ValueError("Non-finite CLIP similarity scores encountered.")
        65        per_label = []
        66        valid_aps = []
        67        for index, label in enumerate(labels):
        68            positives = int(targets[:, index].sum())
        69            # Match the OCL evaluator: labels with no positives do not contribute to mAP.
        70            ap = (
        71                float(average_precision_score(targets[:, index], scores[:, index]))
        72                if positives else None
        73            )
        74            if ap is not None:
        75                valid_aps.append(ap)
        76            per_label.append({"id": index, "label": label, "positives": positives, "AP": ap})
        77        return {
        78            "mAP": float(np.mean(valid_aps)) if valid_aps else None,
        79            "num_evaluated_labels": len(valid_aps),
        80            "num_labels": len(labels),
        81            "labels_without_positives": "excluded",
        82            "per_label": per_label,
        83        }
        84
        85
        86    @torch.inference_mode()
        87    def run_inference(
        88        model: CLIPModel,
        89        dataset: OCLClipDataset,
        90        loader: DataLoader,
        91        device: torch.device,
        92        top_k: tuple[int, ...] = (1, 5),
        93    ) -> dict:
        94        top_k = tuple(sorted(set(top_k)))
        95        if not top_k or any(k < 1 or k > len(dataset.category_classes) for k in top_k):
        96            raise ValueError(
        97                f"top_k must contain values between 1 and {len(dataset.category_classes)}."
        98            )
        99        model.eval()
       100        text_features = encode_candidate_labels(model, dataset.text_inputs, device)
       101        correct = {k: 0 for k in top_k}
       102        num_objects = 0
       103        attribute_scores, affordance_scores = [], []
       104        attribute_targets, affordance_targets = [], []
       105
       106        for batch in tqdm(loader, desc="CLIP inference", unit="batch"):
       107            pixel_values = batch["pixel_values"].to(device, non_blocking=device.type == "cuda")
       108            features = model.get_image_features(pixel_values=pixel_values)
       109            image_features = F.normalize(features.float(), dim=-1)
       110            # Unit-length embeddings turn dot products into cosine similarities.
       111            category_scores = image_features @ text_features["category"].T
       112            ranking = category_scores.topk(max(top_k), dim=-1).indices
       113            targets = batch["category_id"].to(device)
       114            for k in top_k:
       115                correct[k] += int((ranking[:, :k] == targets[:, None]).any(dim=1).sum().item())
       116            num_objects += targets.numel()
       117
       118            # Multi-label AP uses independent scores; softmax would couple unrelated labels.
       119            attribute_scores.append((image_features @ text_features["attribute"].T).cpu())
       120            affordance_scores.append((image_features @ text_features["affordance"].T).cpu())
       121            attribute_targets.append(batch["attributes"])
       122            affordance_targets.append(batch["affordances"])
       123
       124        if num_objects == 0 or num_objects != len(dataset):
       125            raise RuntimeError(f"Expected {len(dataset)} objects, evaluated {num_objects}.")
       126        return {
       127            "num_objects": num_objects,
       128            "num_selected_objects_before_box_filter": dataset.num_selected_objects,
       129            "num_excluded_objects": len(dataset.excluded_objects),
       130            "excluded_objects": dataset.excluded_objects,
       131            "num_images": dataset.num_images,
       132            "metric_scale": "0..1",
       133            "category": {f"top_{k}_accuracy": correct[k] / num_objects for k in top_k},
       134            "attribute": multilabel_metrics(
       135                torch.cat(attribute_targets).numpy(),
       136                torch.cat(attribute_scores).numpy(),
       137                dataset.attribute_classes,
       138            ),
       139            "affordance": multilabel_metrics(
       140                torch.cat(affordance_targets).numpy(),
       141                torch.cat(affordance_scores).numpy(),
       142                dataset.affordance_classes,
       143            ),
       144        }
       145
       146
       147    def parse_args() -> argparse.Namespace:
       148        parser = argparse.ArgumentParser(description=__doc__)
       149        parser.add_argument("--data-root", type=Path, default=Path("./data"))
       150        parser.add_argument(
       151            "--model",
       152            default="openai/clip-vit-base-patch32",
       153            help="Hugging Face ID or local model directory",
       154        )
       155        parser.add_argument("--device", default="cuda", help="For example cuda, cuda:1, or cpu")
       156        parser.add_argument("--num-workers", type=int, default=4)
       157        parser.add_argument("--top-k", type=int, nargs="+", default=[1, 5])
       158        parser.add_argument(
       159            "--local-files-only",
       160            action="store_true",
       161            help="Load model and processor from local files/cache only",
       162        )
       163        parser.add_argument("--output", type=Path, default=Path("logs/clip_inference/metrics.json"))
       164        args = parser.parse_args()
       165        if args.num_workers < 0:
       166            parser.error("--num-workers must be non-negative")
       167        if any(k < 1 or k > NUM_CATEGORIES for k in args.top_k):
       168            parser.error(f"--top-k values must be between 1 and {NUM_CATEGORIES}")
       169        return args
       170
       171
       172    def main() -> None:
       173        args = parse_args()
       174        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
       175        device = torch.device(args.device)
       176        if device.type == "cuda" and not torch.cuda.is_available():
       177            raise RuntimeError(
       178                f"CUDA is unavailable (PyTorch {torch.__version__}, CUDA build {torch.version.cuda}). "
       179                "Run bash setup_clip_gpu.sh on the GPU server and check its NVIDIA driver."
       180            )
       181        device_name = torch.cuda.get_device_name(device) if device.type == "cuda" else str(device)
       182        print(f"Device: {device} ({device_name}); PyTorch: {torch.__version__}; CUDA: {torch.version.cuda}")
       183        model, processor = load_model(args.model, device, args.local_files_only)
       184        dataset, loader = load_dataset(
       185            args.data_root,
       186            processor,
       187            num_workers=args.num_workers,
       188            pin_memory=device.type == "cuda",
       189        )
       190        print(
       191            f"Images: {dataset.num_images}; objects: {len(dataset)}; batch size: {BATCH_SIZE}"
       192        )
       193        if dataset.excluded_objects:
       194            print(
       195                f"Excluded {len(dataset.excluded_objects)} of {dataset.num_selected_objects} "
       196                "selected objects with unusable boxes; details will be saved in the metrics JSON."
       197            )
       198        for category, count in dataset.selection_category_counts.items():
       199            print(
       200                f"  {category}: ranking objects={count}, "
       201                f"evaluation objects={dataset.evaluation_category_counts[category]}"
       202            )
       203
       204        results = run_inference(model, dataset, loader, device, tuple(args.top_k))
       205        results.update(
       206            {
       207                "model": args.model,
       208                "device": str(device),
       209                "device_name": device_name,
       210                "torch_version": torch.__version__,
       211                "cuda_build": torch.version.cuda,
       212                "data_root": str(dataset.data_root),
       213                "count_unit": "object_instance",
       214                "batch_size": BATCH_SIZE,
       215                "selected_categories": [
       216                    {
       217                        "id": index,
       218                        "name": name,
       219                        "selection_samples": dataset.selection_category_counts[name],
       220                        "evaluation_samples": dataset.evaluation_category_counts[name],
       221                    }
       222                    for index, name in enumerate(dataset.category_classes)
       223                ],
       224                "prompts": dataset.prompts,
       225            }
       226        )
       227        output = args.output.expanduser()
       228        output.parent.mkdir(parents=True, exist_ok=True)
       229        with output.open("w", encoding="utf-8") as handle:
       230            json.dump(results, handle, indent=2, allow_nan=False)
       231            handle.write("\n")
       232
       233        for name, accuracy in results["category"].items():
       234            print(f"{name}: {accuracy:.2%}")
       235        for task in ("attribute", "affordance"):
       236            metrics = results[task]
       237            value = "N/A" if metrics["mAP"] is None else f"{metrics['mAP']:.2%}"
       238            print(
       239                f"{task} mAP: {value} "
       240                f"({metrics['num_evaluated_labels']}/{metrics['num_labels']} labels with positives)"
       241            )
       242        print(f"Metrics saved to {output}")
       243
       244
       245    if __name__ == "__main__":
       246        main()
    ✓ • 7ms

## Activity

    $ nl -ba docs/clip_inference.md
         1    # Frozen CLIP inference on OCL
         2
         3    This standalone experiment implements `Test.md` with Hugging Face
         4    `openai/clip-vit-base-patch32`. It does not depend on the original OCRN training
         5    environment in `requirements.txt`.
         6
         7    ## Environment
         8
         9    Use Python 3.12 and the separate `requirements-clip.txt`. A local `.venv` has been
        10    prepared with CPU PyTorch; no model weights have been downloaded and no inference
        11    has been run. Recreate the environment on the remote server instead of copying
        12    `.venv`, since virtual environments contain machine-specific paths and binaries.
        13
        14    The CLIP environment pairs `torch==2.8.0` with `torchvision==0.23.0`.
        15    `torchvision==0.9.1` in the original `requirements.txt` pairs with `torch==1.8.1`
        16    and has wheels for Python 3.6-3.9; it is incompatible with this environment.
        17    When using pip, activate `.venv` and use `python -m pip`, or use
        18    `.venv/bin/python -m pip` directly, to select the project's interpreter.
        19
        20    From the repository root on a server with `uv` installed:
        21
        22    ```bash
        23    bash setup_clip_gpu.sh
        24    source .venv/bin/activate
        25    ```
        26
        27    The script creates `.venv` if needed; `uv` can download Python 3.12 if it is
        28    missing. It uses the `auto` PyTorch backend to choose a build for the server's
        29    detected accelerator, reinstalls both `torch` and `torchvision` to replace any
        30    existing CPU builds, and installs `pip` into the environment. It verifies
        31    `torch.cuda.is_available()`. This check does not load CLIP or perform inference.
        32    The script stops with an error if CUDA is unavailable.
        33
        34    For an explicit CUDA build, use `bash setup_clip_gpu.sh cu128`, or `cu126` for a
        35    server requiring that build. The NVIDIA driver must support the selected CUDA
        36    runtime. The inference command defaults to `--device cuda` and prints the GPU
        37    name, PyTorch version and CUDA build before loading the model.
        38
        39    ## Data layout and labels
        40
        41    The data is assumed to have already been prepared using `README.md`. Image paths
        42    in annotations are relative to `--data-root`, which defaults to `./data`:
        43
        44    ```text
        45    data/
        46      resources/
        47        OCL_annot_train.pkl
        48        OCL_annot_val.pkl
        49        OCL_annot_test.pkl
        50        OCL_class_object.json
        51        OCL_class_attribute.json
        52        OCL_class_affordance.json
        53      COCO/
        54        train2014/
        55        val2014/
        56      ImageNet/
        57        train/
        58        val/
        59      aPY/
        60      SUN/
        61      from_web/
        62    ```
        63
        64    For missing web images, use the project environment, which provides `requests`,
        65    Pillow and `tqdm`. From the repository root:
        66
        67    ```bash
        68    .venv/bin/python data/download_web_images.py --limit 5
        69    .venv/bin/python data/download_web_images.py
        70    ```
        71
        72    The first command checks a small batch; the second processes the full URL list.
        73    The downloader resolves paths relative to its own `data/` directory by default,
        74    so it can also be run from inside that directory. Use `--data-root` for another
        75    dataset location. It tries HTTPS before legacy HTTP URLs, uses socket timeouts
        76    and bounded retries, skips existing decodable images, and saves downloads only
        77    after image validation. One failed URL does not stop the remaining downloads.
        78
        79    Each run writes `data/web_download_failures.json` with counts, original URLs,
        80    target filenames and per-attempt errors, including HTTP status codes. The report
        81    covers only that invocation (`--limit` may restrict it). Exit status is 1 if any
        82    images failed and 130 after Ctrl-C; an interrupted run also reports pending
        83    entries. Rerun the same command to retry missing or invalid files while skipping
        84    completed downloads. Permanently unavailable images still need to be recovered
        85    before evaluating the complete dataset.
        86
        87    The actual annotation filenames are `OCL_annot_*.pkl`; the README's reference to
        88    `OCL_class_*.pkl` is a naming error. Each pickle contains a list of image records
        89    with `name`, `source`, and `objects`. Each object contains:
        90
        91    | Field | Meaning |
        92    | --- | --- |
        93    | `obj` | Category name, matching `OCL_class_object.json` (381 categories). |
        94    | `box` | Pixel coordinates `[x_min, y_min, x_max, y_max]`, already in xyxy format. |
        95    | `attr` | Positive indices into `OCL_class_attribute.json` (114 labels). |
        96    | `aff` | Positive indices into `OCL_class_affordance.json` (170 labels). |
        97    | `causal` | Attribute-to-affordance relations; unused in this CLIP baseline. |
        98
        99    Attribute labels are strings. Each affordance label is a dictionary with `word`
       100    (synonyms) and `define` (meaning). Affordance IDs are preserved even when two
       101    entries share the same verb; the text prompt also includes the definition.
       102
       103    `clip_dataset.py` counts **object instances grouped by `obj` (object category)**,
       104    including multiple objects with the same category in one image. It merges
       105    `OCL_annot_train.pkl`, `OCL_annot_val.pkl` and `OCL_annot_test.pkl` into one
       106    evaluation dataset, then keeps the ten most frequent categories. Equal counts
       107    are resolved alphabetically. All objects from these categories form the
       108    inference set. With the supplied annotations:
       109
       110    | Category | Annotated objects |
       111    | --- | ---: |
       112    | dog | 16,171 |
       113    | bird | 13,961 |
       114    | sheep | 13,821 |
       115    | car | 11,511 |
       116    | motorcycle | 8,519 |
       117    | apple | 8,382 |
       118    | cattle | 8,379 |
       119    | broccoli | 8,333 |
       120    | truck | 7,769 |
       121    | elephant | 7,032 |
       122    | Total | 103,878 |
       123
       124    The selection contains 103,878 annotated objects from 35,633 distinct
       125    images. One selected object has a zero-height box: `car`, object index
       126    12 in `COCO/val2014/COCO_val2014_000000315601.jpg`, box `[0, 266, 4, 266]`.
       127    It remains in the category statistics but cannot produce a valid crop, so the
       128    inference set has **103,877 usable objects**. Exclusions, including the image,
       129    object index, category and reason, are recorded in the metrics JSON.
       130
       131    Counts are recomputed from the annotations at runtime rather than hardcoded.
       132    Each dataset item is an object crop, so `batch_size=4` means four objects. Boxes
       133    are clipped to the image bounds; an absent box uses the full image, matching the
       134    original dataset's convention. Malformed, non-finite and zero/negative-area
       135    annotation boxes are excluded with an explicit report. Missing images and boxes
       136    that become empty after clipping to actual image dimensions raise errors.
       137
       138    The model's `CLIPProcessor` supplies RGB image resizing, center cropping,
       139    rescaling, and CLIP normalization. It produces `[4, 3, 224, 224]` image tensors
       140    for the default model (the final batch may be smaller). Its tokenizer processes
       141    the category, attribute, and affordance prompts once, with padding and truncation
       142    to CLIP's context length. Targets are category IDs in `[0, 9]` and multi-hot
       143    attribute/affordance vectors.
       144
       145    ## Run on the remote server
       146
       147    From the repository root, after activating the server environment:
       148
       149    ```bash
       150    python clip_inference.py --data-root ./data --device cuda
       151    ```
       152
       153    The command selects all 103,878 objects and evaluates the 103,877 objects with
       154    usable annotation boxes.
       155
       156    The first run downloads the Hugging Face model and processor to the standard
       157    Hugging Face cache. For an offline server, transfer a complete Hugging Face model
       158    directory containing the weights, configuration, processor and tokenizer files:
       159
       160    ```bash
       161    python clip_inference.py --model /path/to/clip-vit-base-patch32 --local-files-only --device cuda
       162    ```
       163
       164    Available options include `--num-workers 4`, `--top-k 1 5`,
       165    `--device cuda:1`, and `--output logs/clip_inference/metrics.json`. Use
       166    `--num-workers 0` if the server cannot use worker processes. Batch size remains
       167    fixed at four, with `shuffle=False` and `drop_last=False`.
       168
       169    `load_model` loads `CLIPModel`, sets every parameter's `requires_grad` to `False`,
       170    calls `model.to(device)` and `model.eval()`. Both text encoding and the complete
       171    inference loop use `torch.inference_mode()`. Candidate text features are computed
       172    once. Every object's image feature and each text feature are L2-normalized, so
       173    their dot product is cosine similarity.
       174
       175    The report contains:
       176
       177    - Top-1 and Top-5 category accuracy, or the requested Top-k values, among the
       178      selected ten categories. Counts are accumulated across all objects and divided
       179      by the total, not averaged equally across batches.
       180    - Attribute and affordance mAP on these same objects, using all 114 and 170
       181      candidate labels. Each label's AP uses its independent cosine scores without
       182      softmax. Labels with no positives are excluded from mAP, matching the original
       183      OCL evaluator, and receive `null` AP in the report.
       184    - Category counts before and after excluding unusable boxes, excluded objects,
       185      text prompts, label IDs, per-label AP/support, model, GPU name, PyTorch/CUDA
       186      versions, and number of evaluated objects/images.
       187
       188    Metrics in JSON use the range `[0, 1]`; the terminal displays percentages. This
       189    is a zero-shot prompt baseline, and its scores depend on the chosen text prompts.
    ✓ • 0ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        for base in [Path('/'),Path('/home'),Path('/home/linfu'),Path('/home/linfu/src'),Path('/home/linfu/src/Test'),Path('/home/linfu/src/Test/ObjectConceptLearning'),Path('/home/linfu/src/Test/ObjectConceptLearning/data')]:
            path = base/'AGENTS.md'
            if path.is_file():
                print(f'{path}:\n{path.read_text()}')
        root = Path('/home/linfu/src/Test/ObjectConceptLearning')
        for path in sorted(root.iterdir()):
            print(('DIR ' if path.is_dir() else 'FILE'), path.name)
        PY
    DIR  .git
    FILE .gitignore
    DIR  .venv
    FILE LICENSE
    FILE README.md
    FILE Test.md
    DIR  __pycache__
    DIR  aPY
    FILE calc_dataset_prior.py
    FILE clip_dataset.py
    FILE clip_inference.py
    DIR  config
    DIR  data
    DIR  docs
    FILE extract_feature.py
    DIR  models
    FILE requirements-clip.txt
    FILE requirements.txt
    FILE run_ocl.py
    FILE setup_clip_gpu.sh
    FILE test_ocl.py
    FILE test_tde.py
    DIR  tests
    DIR  utils
    ✓ • 121ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        for name in ['requirements-clip.txt','setup_clip_gpu.sh','requirements.txt','README.md','tests/test_clip_category_selection.py']:
            print(f'FILE {name}')
            for line, text in enumerate(Path(name).read_text().splitlines(), 1):
                print(f'{line:4} {text}')
        PY
    FILE requirements-clip.txt
       1 # Standalone CLIP inference environment (Python 3.12).
       2 # On the GPU server: bash setup_clip_gpu.sh
       3 torch==2.8.0
       4 torchvision==0.23.0
       5 transformers==4.57.1
       6 numpy==2.2.6
       7 Pillow==11.3.0
       8 scikit-learn==1.7.2
       9 tqdm==4.67.1
    FILE setup_clip_gpu.sh
       1 #!/usr/bin/env bash
       2 set -euo pipefail
       3
       4 project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
       5 torch_backend="${1:-auto}"
       6
       7 if ! command -v uv >/dev/null 2>&1; then
       8     printf '%s\n' 'Install uv on this server before running this script.' >&2
       9     exit 1
      10 fi
      11
      12 if [[ ! -x "$project_root/.venv/bin/python" ]]; then
      13     uv venv --python 3.12 "$project_root/.venv"
      14 fi
      15
      16 # Replace both CPU builds even when their public versions already match.
      17 uv pip install \
      18     --python "$project_root/.venv/bin/python" \
      19     --torch-backend "$torch_backend" \
      20     --reinstall-package torch \
      21     --reinstall-package torchvision \
      22     -r "$project_root/requirements-clip.txt" \
      23     pip
      24
      25 "$project_root/.venv/bin/python" - <<'PY'
      26 import torch
      27 import torchvision
      28
      29 if not torch.cuda.is_available():
      30     raise SystemExit(
      31         f"CUDA is unavailable: torch={torch.__version__}, CUDA build={torch.version.cuda}. "
      32         "Check the NVIDIA driver and, if necessary, choose a compatible backend "
      33         "with bash setup_clip_gpu.sh cu128 (or cu126)."
      34     )
      35 print(f"PyTorch: {torch.__version__}; torchvision: {torchvision.__version__}")
      36 print(f"CUDA build: {torch.version.cuda}")
      37 print(f"GPU: {torch.cuda.get_device_name(0)}")
      38 print("GPU environment ready. No CLIP model or inference has been run.")
      39 PY
    FILE requirements.txt
       1 torch==1.8.1
       2 torchvision==0.9.1
       3 numpy==1.20
       4 pillow==8.2.0
       5 tensorboard
       6 sklearn
       7 tqdm
       8 pyyaml
       9 easydict
      10 termcolor
    FILE README.md
       1 # Object Concept Learning
       2
       3 This the official repository of [Beyond Object Recognition: A New Benchmark towards Object Concept Learning](https://arxiv.org/abs/2212.02710) (ICCV 2023).
       4
       5
       6 We propose the challenging Object Concept Learning (OCL) task to push the envelope of object understanding, requiring machines to reason out affordances and simultaneously give the reason: what attributes make an object possess these affordances. To support OCL, we build a densely annotated knowledge base including extensive annotations for three levels of ob- ject concept (category, attribute, affordance), and the clear causal relations of three levels. This repo contains our **data and annotation**, and the **code implementation**.
       7
       8 <p align="center"><img src='docs/task.png' width=600></p>
       9
      10
      11
      12 ## Preparation
      13
      14 ### Requirements
      15
      16 See `requirements.txt`. Python 3.8 + PyTorch 1.8.1
      17
      18
      19 ### Datasets
      20
      21 To prepare data, you should download ImageNet(2012) to `./data/ImageNet` and download the url-expired web images from [here](https://drive.google.com/drive/folders/1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF?usp=share_link) and put to `./data/from_web.tgz`. The folder structure should be like:
      22 ```
      23 ./data
      24 ├── from_web.tgz
      25 ├── ImageNet/
      26 │   ├── train/
      27 │   │   ├── n02133161/
      28 │   │   ├── n02514041/
      29 │   │   └── ......
      30 │   └── val
      31 │       ├── ILSVRC2012_val_00011812.JPEG
      32 │       ├── ILSVRC2012_val_00036760.JPEG
      33 │       └── ......
      34 ├── resources/
      35 ├── prepare_data.sh
      36 └── ...
      37 ```
      38
      39
      40 Then run the script to download and reorganize the rest datasets:
      41 ```
      42 cd ./data;
      43 sh prepare_data.sh;
      44 ```
      45
      46
      47
      48 The annotation files have been put in `./data/resources`:
      49
      50 - `OCL_class_*.pkl` contains the annotation of the three splits:
      51   - The pickle files are stored in binary, please use `"rb"` mode.
      52   - Each file is a list of image annotations. Each image has multiple object instances with bounding box, attributes, affordances, object category and causal rules (attribute->affordance).
      53   - Most files are from COCO, ImageNet-1K, aPY and SUN-attribute. Around 5K images are from the internet, whose urls are listed in `image_urls_from_web.json`. Please use the md5 (or file name) to match the files to the annotations.
      54 - `OCL_class_*.json` contains the list of classes.
      55
      56
      57
      58 ## Pretrained model
      59
      60
      61 You may optionally download our pretrained OCRN model from [here](https://drive.google.com/drive/folders/1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF?usp=share_link).
      62
      63
      64 ## Usage
      65
      66 For the standalone Hugging Face CLIP inference experiment in `Test.md`, see the
      67 [CLIP inference guide](docs/clip_inference.md). It selects the ten largest object
      68 categories by instance count across all annotation files, then evaluates all
      69 objects from those categories. It uses batches of four object crops
      70 and reports category Top-k accuracy plus attribute/affordance mAP. Run
      71 `bash setup_clip_gpu.sh` on the GPU server to install its dependencies.
      72
      73 Extract feature and the object prior:
      74 ```
      75 python extract_feature.py --cfg config/Faster50Feature.yaml --splits train
      76 python extract_feature.py --cfg config/Faster50Feature.yaml --splits valtest
      77
      78 python calc_dataset_prior.py --feature_dir features/OCL_faster50_pt_frz
      79 ```
      80
      81 Train an OCRN (in three stages):
      82
      83 ```
      84 python -m torch.distributed.launch --nproc_per_node=4 run_ocl.py --cfg config/OCRN_stage1.yaml
      85
      86 python -m torch.distributed.launch --nproc_per_node=4 run_ocl.py --cfg config/OCRN_stage2.yaml --trained_weight ./logs/OCRN_stage1/checkpoint_ep170.pt --weight_type ocrn_attr
      87
      88 python -m torch.distributed.launch --nproc_per_node=4 run_ocl.py --cfg config/OCRN_stage3.yaml --trained_weight ./logs/OCRN_stage2/checkpoint_ep20.pt --weight_type pretrain
      89 ```
      90
      91
      92
      93 Test with GT boxes:
      94 ```
      95 python test_ocl.py --cfg config/OCRN_stage3.yaml --trained_weight ./logs/OCRN_stage3/checkpoint_ep10.pt
      96 ```
      97
      98
      99 Test on TDE metric:
     100 ```
     101 python test_tde.py --cfg config/OCRN_stage3.yaml --trained_weight ./logs/OCRN_stage3/checkpoint_ep10.pt
     102 ```
     103
     104
     105
     106
     107 ## Reference
     108
     109 ```
     110 @inproceedings{li2023beyond,
     111   title={Beyond Object Recognition: A New Benchmark towards Object Concept Learning},
     112   author={Li, Yong-Lu and Xu, Yue and Xu, Xinyu and Mao, Xiaohan and Yao, Yuan and Liu, Siqi and Lu, Cewu},
     113   booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
     114   pages={20029--20040},
     115   year={2023}
     116 }
     117 ```
     118
     119
     120 ## Acknowledgement
     121
     122 Our database is built upon [aPY](https://vision.cs.uiuc.edu/attributes/) (which also involves [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/index.html)), [SUN attribute](https://cs.brown.edu/~gmpatter/sunattributes.html), [MS-COCO](https://cocodataset.org) and [ImageNet](https://www.image-net.org) (and the [ImageNet-150K dataset](https://vipl.ict.ac.cn/en/resources/databases/201803/t20180316_34793.html)).
     123 Part of the images are collected via internet and we only provide URLs for redownloading due to licensing issues. Since some URLs have been expired or unreachable (~2K), we provide these images **for only non-commercial usage**.
     124
     125 Some of the images are collected from the internet, and we only offer URLs for re-download due to licensing concerns. Since certain URLs having expired or become inaccessible (~2K), we provide these images **only for non-commercial and educational use**.
    FILE tests/test_clip_category_selection.py
       1 """Offline regression checks for category counts; no images or CLIP weights."""
       2
       3 import json
       4 import pickle
       5 import tempfile
       6 import unittest
       7 from pathlib import Path
       8 from types import SimpleNamespace
       9
      10 import torch
      11
      12 from clip_dataset import OCLClipDataset, load_dataset
      13
      14
      15 class StubTokenizer:
      16     model_max_length = 77
      17
      18     def __call__(self, texts, **kwargs):
      19         tokens = torch.ones((len(texts), 2), dtype=torch.long)
      20         return {"input_ids": tokens, "attention_mask": tokens}
      21
      22
      23 class CategorySelectionTests(unittest.TestCase):
      24     def setUp(self):
      25         temporary = tempfile.TemporaryDirectory()
      26         self.addCleanup(temporary.cleanup)
      27         self.root = Path(temporary.name)
      28         resources = self.root / "resources"
      29         resources.mkdir()
      30         self.head = [f"head_{index:02d}" for index in range(10)]
      31         vocabularies = {
      32             "object": self.head + ["test_only"],
      33             "attribute": ["round"],
      34             "affordance": [{"word": ["carry"], "define": "have with oneself"}],
      35         }
      36         for name, labels in vocabularies.items():
      37             (resources / f"OCL_class_{name}.json").write_text(json.dumps(labels))
      38
      39         def record(split, label, count):
      40             return {
      41                 "name": f"{split}/{label}.jpg",
      42                 "objects": [
      43                     {"obj": label, "attr": [0], "aff": [0]} for _ in range(count)
      44                 ],
      45             }
      46
      47         splits = {
      48             "train": [record("train", label, 10) for label in self.head],
      49             "val": [record("val", self.head[0], 3)],
      50             "test": [record("test", label, 1) for label in self.head]
      51             + [record("test", "test_only", 9)],
      52         }
      53         for split, records in splits.items():
      54             with (resources / f"OCL_annot_{split}.pkl").open("wb") as handle:
      55                 pickle.dump(records, handle)
      56         self.processor = SimpleNamespace(image_processor=None, tokenizer=StubTokenizer())
      57
      58     def test_all_annotations_supply_counts_and_evaluation_objects(self):
      59         dataset, loader = load_dataset(
      60             self.root, self.processor, num_workers=0, pin_memory=False
      61         )
      62         self.assertEqual(dataset.category_classes, self.head)
      63         self.assertEqual(dataset.selection_category_counts[self.head[0]], 14)
      64         self.assertEqual(dataset.selection_category_counts[self.head[-1]], 11)
      65         self.assertEqual(len(dataset), 113)
      66         self.assertEqual(dataset.num_images, 21)
      67         self.assertEqual(dataset.evaluation_category_counts, dataset.selection_category_counts)
      68         self.assertEqual(loader.batch_size, 4)
      69         self.assertFalse(loader.drop_last)
      70
      71     def test_invalid_box_remains_in_ranking_and_is_reported_before_evaluation(self):
      72         path = self.root / "resources" / "OCL_annot_train.pkl"
      73         with path.open("rb") as handle:
      74             records = pickle.load(handle)
      75         records.append(
      76             {
      77                 "name": "train/invalid.jpg",
      78                 "objects": [
      79                     {"obj": self.head[0], "attr": [0], "aff": [0], "box": [0, 2, 4, 2]}
      80                 ],
      81             }
      82         )
      83         with path.open("wb") as handle:
      84             pickle.dump(records, handle)
      85         dataset = OCLClipDataset(self.root, self.processor)
      86         self.assertEqual(dataset.selection_category_counts[self.head[0]], 15)
      87         self.assertEqual(dataset.evaluation_category_counts[self.head[0]], 14)
      88         self.assertEqual(dataset.num_selected_objects, 114)
      89         self.assertEqual(len(dataset), 113)
      90         self.assertEqual(len(dataset.excluded_objects), 1)
      91         self.assertEqual(dataset.excluded_objects[0]["image_name"], "train/invalid.jpg")
      92
      93
      94 if __name__ == "__main__":
      95     unittest.main()
    ✓ • 96ms

## Assistant

核心 CLIP 推理代码已经具备，包含对象裁剪、固定 batch size 为 4、Top-k accuracy 和属性/可供性 mAP。需要先明确一个评估口径：当前代码合并了 train、val、test 三份标注；`Test.md` 提到了“测试集”，但没有明确是否仅指官方 test split。我会在指南中说明这个差异，同时检查其余图片路径和服务器环境脚本。

## Activity

    $ sed -n '172,260p' clip_inference.py
    def main() -> None:
        args = parse_args()
        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
        device = torch.device(args.device)
        if device.type == "cuda" and not torch.cuda.is_available():
            raise RuntimeError(
                f"CUDA is unavailable (PyTorch {torch.__version__}, CUDA build {torch.version.cuda}). "
                "Run bash setup_clip_gpu.sh on the GPU server and check its NVIDIA driver."
            )
        device_name = torch.cuda.get_device_name(device) if device.type == "cuda" else str(device)
        print(f"Device: {device} ({device_name}); PyTorch: {torch.__version__}; CUDA: {torch.version.cuda}")
        model, processor = load_model(args.model, device, args.local_files_only)
        dataset, loader = load_dataset(
            args.data_root,
            processor,
            num_workers=args.num_workers,
            pin_memory=device.type == "cuda",
        )
        print(
            f"Images: {dataset.num_images}; objects: {len(dataset)}; batch size: {BATCH_SIZE}"
        )
        if dataset.excluded_objects:
            print(
                f"Excluded {len(dataset.excluded_objects)} of {dataset.num_selected_objects} "
                "selected objects with unusable boxes; details will be saved in the metrics JSON."
            )
        for category, count in dataset.selection_category_counts.items():
            print(
                f"  {category}: ranking objects={count}, "
                f"evaluation objects={dataset.evaluation_category_counts[category]}"
            )
    
        results = run_inference(model, dataset, loader, device, tuple(args.top_k))
        results.update(
            {
                "model": args.model,
                "device": str(device),
                "device_name": device_name,
                "torch_version": torch.__version__,
                "cuda_build": torch.version.cuda,
                "data_root": str(dataset.data_root),
                "count_unit": "object_instance",
                "batch_size": BATCH_SIZE,
                "selected_categories": [
                    {
                        "id": index,
                        "name": name,
                        "selection_samples": dataset.selection_category_counts[name],
                        "evaluation_samples": dataset.evaluation_category_counts[name],
                    }
                    for index, name in enumerate(dataset.category_classes)
                ],
                "prompts": dataset.prompts,
            }
        )
        output = args.output.expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8") as handle:
            json.dump(results, handle, indent=2, allow_nan=False)
            handle.write("\n")
    
        for name, accuracy in results["category"].items():
            print(f"{name}: {accuracy:.2%}")
        for task in ("attribute", "affordance"):
            metrics = results[task]
            value = "N/A" if metrics["mAP"] is None else f"{metrics['mAP']:.2%}"
            print(
                f"{task} mAP: {value} "
                f"({metrics['num_evaluated_labels']}/{metrics['num_labels']} labels with positives)"
            )
        print(f"Metrics saved to {output}")
    
    
    if __name__ == "__main__":
        main()
    ✓ • 0ms

## Activity

    $ sed -n '1,38p' docs/clip_inference.md
    # Frozen CLIP inference on OCL
    
    This standalone experiment implements `Test.md` with Hugging Face
    `openai/clip-vit-base-patch32`. It does not depend on the original OCRN training
    environment in `requirements.txt`.
    
    ## Environment
    
    Use Python 3.12 and the separate `requirements-clip.txt`. A local `.venv` has been
    prepared with CPU PyTorch; no model weights have been downloaded and no inference
    has been run. Recreate the environment on the remote server instead of copying
    `.venv`, since virtual environments contain machine-specific paths and binaries.
    
    The CLIP environment pairs `torch==2.8.0` with `torchvision==0.23.0`.
    `torchvision==0.9.1` in the original `requirements.txt` pairs with `torch==1.8.1`
    and has wheels for Python 3.6-3.9; it is incompatible with this environment.
    When using pip, activate `.venv` and use `python -m pip`, or use
    `.venv/bin/python -m pip` directly, to select the project's interpreter.
    
    From the repository root on a server with `uv` installed:
    
    ```bash
    bash setup_clip_gpu.sh
    source .venv/bin/activate
    ```
    
    The script creates `.venv` if needed; `uv` can download Python 3.12 if it is
    missing. It uses the `auto` PyTorch backend to choose a build for the server's
    detected accelerator, reinstalls both `torch` and `torchvision` to replace any
    existing CPU builds, and installs `pip` into the environment. It verifies
    `torch.cuda.is_available()`. This check does not load CLIP or perform inference.
    The script stops with an error if CUDA is unavailable.
    
    For an explicit CUDA build, use `bash setup_clip_gpu.sh cu128`, or `cu126` for a
    server requiring that build. The NVIDIA driver must support the selected CUDA
    runtime. The inference command defaults to `--device cuda` and prints the GPU
    name, PyTorch version and CUDA build before loading the model.
    
    ✓ • 0ms

## Activity

    $ nl -ba data/prepare_data.sh
         1    # Extract annotation files
         2
         3    cd resources;
         4    tar -xzf OCL_annot.tgz;
         5    cd ..;
         6
         7
         8
         9    # Download and extract image data
        10
        11    echo "Downloading SUN-attribute";
        12    mkdir -p SUN;
        13    cd SUN;
        14    if [ ! -e "SUNAttributeDB_Images.tar.gz" ]; then
        15        wget https://cs.brown.edu/~gmpatter/Attributes/SUNAttributeDB_Images.tar.gz;
        16    fi
        17    if [ ! -e "images" ]; then
        18        tar -xzf SUNAttributeDB_Images.tar.gz;
        19    fi
        20    cd ..;
        21
        22
        23    echo "Downloading aPY";
        24    mkdir -p aPY;
        25    cd aPY;
        26    if [ ! -e "ayahoo_test_images.tar.gz" ]; then
        27        wget http://vision.cs.uiuc.edu/attributes/ayahoo_test_images.tar.gz;
        28    fi
        29    if [ ! -e "VOCtrainval_14-Jul-2008.tar" ]; then
        30        wget http://host.robots.ox.ac.uk/pascal/VOC/voc2008/VOCtrainval_14-Jul-2008.tar;
        31    fi
        32    if [ ! -e "ayahoo_test_images" ]; then
        33    tar -xzf ayahoo_test_images.tar.gz;
        34    tar -xf VOCtrainval_14-Jul-2008.tar;
        35    cd ..;
        36    fi
        37
        38    echo "Downloading COCO";
        39    mkdir -p COCO;
        40    cd COCO;
        41    wget http://images.cocodataset.org/zips/train2014.zip;
        42    wget http://images.cocodataset.org/zips/val2014.zip;
        43    unzip train2014.zip;
        44    unzip val2014.zip;
        45    cd ..;
        46
        47
        48    # Prepare web image data
        49    tar -xf from_web.tgz
        50    python download_web_images.py
    ✓ • 0ms

## Activity

    $ rg -n 'def|average_precision|mAP|box|attr|aff|data_root|img_path' utils/evaluator.py utils/dataset/OCL_dataset.py
    utils/dataset/OCL_dataset.py:17:    def __init__(self, phase):
    utils/dataset/OCL_dataset.py:26:        def load_pickle_and_assign_split(split):
    utils/dataset/OCL_dataset.py:43:        # construct attr/aff/obj list/matrix
    utils/dataset/OCL_dataset.py:44:        def load_class_json(name):
    utils/dataset/OCL_dataset.py:48:        self.attrs = load_class_json("attribute")
    utils/dataset/OCL_dataset.py:50:        self.affs = load_class_json("affordance")
    utils/dataset/OCL_dataset.py:53:        with open('data/resources/category_aff_matrix.json', "r") as fp:
    utils/dataset/OCL_dataset.py:54:            aff_matrix_file = json.load(fp)
    utils/dataset/OCL_dataset.py:55:            assert self.objs == aff_matrix_file['objs']
    utils/dataset/OCL_dataset.py:56:            self.aff_matrix = np.array(aff_matrix_file["aff_matrix"])
    utils/dataset/OCL_dataset.py:58:        self.num_aff = self.aff_matrix.shape[1]
    utils/dataset/OCL_dataset.py:59:        self.num_attr = len(self.attrs)
    utils/dataset/OCL_dataset.py:62:        logging.info("#obj %d, #attr %d, #aff %d" % (
    utils/dataset/OCL_dataset.py:63:            self.num_obj, self.num_attr, self.num_aff))
    utils/dataset/OCL_dataset.py:66:    def __len__(self):
    utils/dataset/OCL_dataset.py:69:    def __getitem__(self, index):
    utils/dataset/OCL_dataset.py:77:        attr = []
    utils/dataset/OCL_dataset.py:78:        aff = []
    utils/dataset/OCL_dataset.py:79:        gt_box = []
    utils/dataset/OCL_dataset.py:81:            a = torch.zeros([self.num_attr]).float()
    utils/dataset/OCL_dataset.py:82:            a[obj['attr']] = 1
    utils/dataset/OCL_dataset.py:83:            attr.append(a)
    utils/dataset/OCL_dataset.py:85:            b = torch.zeros([self.num_aff]).float()
    utils/dataset/OCL_dataset.py:86:            b[obj['aff']] = 1
    utils/dataset/OCL_dataset.py:87:            aff.append(b)
    utils/dataset/OCL_dataset.py:89:            x = obj.get('box', [0, 0, image_width, image_height])
    utils/dataset/OCL_dataset.py:90:            gt_box.append(x)
    utils/dataset/OCL_dataset.py:92:        attr = torch.stack(attr, 0)
    utils/dataset/OCL_dataset.py:93:        aff = torch.stack(aff, 0)
    utils/dataset/OCL_dataset.py:100:            gt_box = [(x[0] // 2, x[1] // 2, x[2] // 2, x[3] // 2) for x in gt_box]
    utils/dataset/OCL_dataset.py:107:            "gt_bbox": np.array(gt_box, dtype=np.float32),
    utils/dataset/OCL_dataset.py:108:            'gt_aff': aff,
    utils/dataset/OCL_dataset.py:109:            "gt_attr": attr,
    utils/dataset/OCL_dataset.py:114:        sample["main_bbox"] = sample["gt_bbox"]
    utils/dataset/OCL_dataset.py:121:    def __init__(self, phase, feature_dir):
    utils/dataset/OCL_dataset.py:131:    def __len__(self):
    utils/dataset/OCL_dataset.py:135:    def __getitem__(self, index):
    utils/dataset/OCL_dataset.py:144:        attr = torch.zeros([self.num_attr]).float()
    utils/dataset/OCL_dataset.py:145:        attr[obj['attr']] = 1
    utils/dataset/OCL_dataset.py:147:        aff = torch.zeros([self.num_aff]).float()
    utils/dataset/OCL_dataset.py:148:        aff[obj['aff']] = 1
    utils/dataset/OCL_dataset.py:153:            "gt_attr": attr,
    utils/dataset/OCL_dataset.py:155:            'gt_aff': aff,
    utils/evaluator.py:6:from collections import defaultdict
    utils/evaluator.py:9:def average_precision(truth, scores):
    utils/evaluator.py:12:        a = sklmetric.average_precision_score(truth, scores)
    utils/evaluator.py:19:def calc_roc_auc(truth, scores):
    utils/evaluator.py:28:def tde_evaluator(pred, gt):
    utils/evaluator.py:30:    :param pred:    dict includes attr_main (bz * num_attr), aff_main (bz * num_aff), tde_main (bz * num_attr * num_aff)
    utils/evaluator.py:31:    :param gt:      dict includes gt_attr (bz * num_attr), gt_aff (bz * num_aff), gt_causal (bz * num_attr * num_aff)
    utils/evaluator.py:37:    num_attr = gt['attr'].shape[1]
    utils/evaluator.py:38:    num_aff = gt['aff'].shape[1]
    utils/evaluator.py:41:    AP_simple = np.zeros((num_attr, num_aff))
    utils/evaluator.py:44:        np.tile(np.expand_dims(gt['aff'] == 1, 1), (1, num_attr, 1)) ^ (prob_diff > 0),
    utils/evaluator.py:48:    for i in range(num_attr):
    utils/evaluator.py:49:        for j in range(num_aff):
    utils/evaluator.py:50:            AP_simple[i, j] = average_precision(
    utils/evaluator.py:55:    mAP_simple_many300 = np.nanmean(np.where(many300>0,AP_simple,np.nan))
    utils/evaluator.py:61:    score_attr = np.where(
    utils/evaluator.py:62:        gt['attr'] == 1,
    utils/evaluator.py:63:        pred['attr_main'],
    utils/evaluator.py:64:        1 - pred['attr_main']
    utils/evaluator.py:66:    score_aff = np.where(
    utils/evaluator.py:67:        gt['aff'] == 1,
    utils/evaluator.py:68:        pred['aff_main'],
    utils/evaluator.py:69:        1 - pred['aff_main']
    utils/evaluator.py:72:                  np.tile(np.expand_dims(score_attr, 2), (1, 1, num_aff)) * \
    utils/evaluator.py:73:                  np.tile(np.expand_dims(score_aff, 1), (1, num_attr, 1))
    utils/evaluator.py:75:    AP_merge = np.zeros((num_attr, num_aff))
    utils/evaluator.py:76:    AUC_merge = np.zeros((num_attr, num_aff))
    utils/evaluator.py:77:    for i in range(num_attr):
    utils/evaluator.py:78:        for j in range(num_aff):
    utils/evaluator.py:79:            AP_merge[i, j] = average_precision(
    utils/evaluator.py:88:    mAP_merge_many300 = np.nanmean(np.where(many300>0,AP_merge,np.nan))
    utils/evaluator.py:91:    gt_attr_per_aff = np.transpose(gt['causal'], (0, 2, 1)).reshape(-1, num_attr)
    utils/evaluator.py:92:    mask = gt_attr_per_aff.sum(-1) > 0
    utils/evaluator.py:94:    gt_attr_per_aff = gt_attr_per_aff[mask]
    utils/evaluator.py:96:    score_attr_per_aff = np.where(
    utils/evaluator.py:97:        np.tile(np.expand_dims(gt['aff'] == 1, 1), (1, num_attr, 1)),
    utils/evaluator.py:101:    score_attr_per_aff = np.transpose(score_attr_per_aff, (0, 2, 1)).reshape(-1, num_attr)
    utils/evaluator.py:102:    score_attr_per_aff = score_attr_per_aff[mask]
    utils/evaluator.py:104:    idx = np.argsort(score_attr_per_aff, 1)[:, ::-1]
    utils/evaluator.py:106:    top1_label = gt_attr_per_aff[
    utils/evaluator.py:107:        np.tile(np.expand_dims(np.arange(len(gt_attr_per_aff)), 1), 1), idx[:, :1]]
    utils/evaluator.py:110:    top5_label = gt_attr_per_aff[
    utils/evaluator.py:111:        np.tile(np.expand_dims(np.arange(len(gt_attr_per_aff)), 1), 5), idx[:, :5]]
    utils/evaluator.py:116:        'top300_ITE_mAP': mAP_simple_many300 * 100,
    utils/evaluator.py:117:        'top300_abITE_mAP': mAP_merge_many300 * 100,
    utils/evaluator.py:123:def mAP_evaluator(prediction, gt_attr, store_ap=None, return_vec=False):
    utils/evaluator.py:124:    """prediction, gt_attr: (#instance, #category)
    utils/evaluator.py:125:    return mAP(float)"""
    utils/evaluator.py:126:    assert prediction.shape == gt_attr.shape
    utils/evaluator.py:129:    assert not np.any(np.isnan(gt_attr)), str(np.sum(np.isnan(gt_attr)))
    utils/evaluator.py:131:    ap = np.zeros((gt_attr.shape[1],))
    utils/evaluator.py:132:    pos = np.zeros((gt_attr.shape[1],))  # num of positive sample
    utils/evaluator.py:134:    for dim in range(gt_attr.shape[1]):
    utils/evaluator.py:137:        gt = gt_attr[:, dim]
    utils/evaluator.py:143:        ap[dim] = average_precision(gt, est)
    utils/evaluator.py:150:            for dim in range(gt_attr.shape[1]):
    utils/evaluator.py:156:        mAP = np.nanmean(ap)
    utils/evaluator.py:157:        return mAP * 100
    ✓ • 0ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        root = Path('/home/linfu/src/Test/ObjectConceptLearning')
        for base in [root/'data', root/'data/COCO', root/'data/ImageNet', root/'data/aPY', root/'data/SUN', root/'aPY']:
            print(f'{base}: exists={base.exists()}, symlink={base.is_symlink()}')
            if base.is_dir():
                for child in sorted(base.iterdir()):
                    if child.is_dir() or base.name == 'data':
                        print('  ', child.name, '-> '+str(child.resolve()) if child.is_symlink() else '')
        print('venv_python:', (root/'.venv/bin/python').resolve())
        for path in [root/'.venv/pyvenv.cfg',root/'.gitignore']:
            print(str(path), path.read_text() if path.exists() else 'MISSING')
        PY
    /home/linfu/src/Test/ObjectConceptLearning/data: exists=True, symlink=False
       .agents
       .aws
       .codex
       .git
       COCO
       SUN
       aPY
       download_web_images.py
       from_web
       from_web.tgz
       from_web.tgz:Zone.Identifier
       prepare_data.sh
       resources
       train2014
       val2014
       数据集
    /home/linfu/src/Test/ObjectConceptLearning/data/COCO: exists=True, symlink=False
       train2014 -> /home/linfu/src/Test/ObjectConceptLearning/data/train2014
       val2014 -> /home/linfu/src/Test/ObjectConceptLearning/data/val2014
    /home/linfu/src/Test/ObjectConceptLearning/data/ImageNet: exists=False, symlink=False
    /home/linfu/src/Test/ObjectConceptLearning/data/aPY: exists=True, symlink=False
       VOCdevkit
       ayahoo_test_images
    /home/linfu/src/Test/ObjectConceptLearning/data/SUN: exists=True, symlink=False
       images
    /home/linfu/src/Test/ObjectConceptLearning/aPY: exists=True, symlink=False
    venv_python: /usr/bin/python3.12
    /home/linfu/src/Test/ObjectConceptLearning/.venv/pyvenv.cfg home = /usr/bin
    implementation = CPython
    uv = 0.12.21
    version_info = 3.12.3
    include-system-site-packages = false
    
    /home/linfu/src/Test/ObjectConceptLearning/.gitignore # SymNet logs
    .vscode/
    .vscode/*
    .vscode/settings.json
    
    
    data/aPY
    data/SUN
    data/from_web
    data/ImageNet
    data/SUN
    logs
    weights
    features
    data_packed
    
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    *$py.class
    
    # C extensions
    *.so
    
    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    pip-wheel-metadata/
    share/python-wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST
    
    # PyInstaller
    #  Usually these files are written by a python script from a template
    #  before PyInstaller builds the exe, so as to inject date/other infos into it.
    *.manifest
    *.spec
    
    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt
    
    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    *.py,cover
    .hypothesis/
    .pytest_cache/
    
    # Translations
    *.mo
    *.pot
    
    # Django stuff:
    *.log
    local_settings.py
    db.sqlite3
    db.sqlite3-journal
    
    # Flask stuff:
    instance/
    .webassets-cache
    
    # Scrapy stuff:
    .scrapy
    
    # Sphinx documentation
    docs/_build/
    
    # PyBuilder
    target/
    
    # Jupyter Notebook
    .ipynb_checkpoints
    
    # IPython
    profile_default/
    ipython_config.py
    
    # pyenv
    .python-version
    
    # pipenv
    #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
    #   However, in case of collaboration, if having platform-specific dependencies or dependencies
    #   having no cross-platform support, pipenv may install dependencies that don't work, or not
    #   install all needed dependencies.
    #Pipfile.lock
    
    # PEP 582; used by e.g. github.com/David-OConnor/pyflow
    __pypackages__/
    
    # Celery stuff
    celerybeat-schedule
    celerybeat.pid
    
    # SageMath parsed files
    *.sage.py
    
    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/
    
    # Spyder project settings
    .spyderproject
    .spyproject
    
    # Rope project settings
    .ropeproject
    
    # mkdocs documentation
    /site
    
    # mypy
    .mypy_cache/
    .dmypy.json
    dmypy.json
    
    # Pyre type checker
    .pyre/
    data/SUN/.
    data/aPY/.
    data/train2014
    data/val2014
    data/数据集
    data/COCO
    
    
    ✓ • 11ms

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -p 'test_clip_category_selection.py' -v
    test_all_annotations_supply_counts_and_evaluation_objects (test_clip_category_selection.CategorySelectionTests.test_all_annotations_supply_counts_and_evaluation_objects) ... ok
    test_invalid_box_remains_in_ranking_and_is_reported_before_evaluation (test_clip_category_selection.CategorySelectionTests.test_invalid_box_remains_in_ranking_and_is_reported_before_evaluation) ... ok
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.023s
    
    OK
    ✓ • 2.53s

## Activity

    $ bash -n setup_clip_gpu.sh data/prepare_data.sh
    ✓ • 0ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        from collections import Counter
        import json, math, os, pickle
        root = Path('data')
        classes = {}
        for kind in ('object', 'attribute', 'affordance'):
            classes[kind] = json.loads((root/'resources'/f'OCL_class_{kind}.json').read_text())
            print('classes', kind, len(classes[kind]), 'first=', classes[kind][0])
        all_records = []
        for split in ('train', 'val', 'test'):
            with (root/'resources'/f'OCL_annot_{split}.pkl').open('rb') as f:
                records = pickle.load(f)
            counts = Counter(obj['obj'] for im in records for obj in im['objects'])
            print('split', split, 'images=',len(records),'objects=',sum(counts.values()))
            if split == 'test':
                top = sorted(counts.items(), key=lambda v: (-v[1],v[0]))[:10]
                print('test_top10',top, 'objects=',sum(n for _,n in top))
            all_records.extend(records)
        counts = Counter(obj['obj'] for im in all_records for obj in im['objects'])
        top = sorted(counts.items(), key=lambda v: (-v[1],v[0]))[:10]
        selected = dict(top)
        print('all_top10',top)
        print('duplicate_image_records',len(all_records)-len({im['name'] for im in all_records}))
        print('all_sources',Counter(im['name'].split('/')[0] for im in all_records))
        chosen_images = {}
        chosen_objects = Counter()
        invalid_boxes = []
        for im in all_records:
            for ix, obj in enumerate(im['objects']):
                if obj['obj'] not in selected:
                    continue
                chosen_images[im['name']] = im
                chosen_objects[im['name'].split('/')[0]] += 1
                box = obj.get('box')
                if box is not None and (len(box)!=4 or not all(math.isfinite(v) for v in box) or box[2]<=box[0] or box[3]<=box[1]):
                    invalid_boxes.append((im['name'],ix,obj['obj'],box))
        print('selected_images',len(chosen_images),'by_source',Counter(n.split('/')[0] for n in chosen_images))
        print('selected_objects_by_source',chosen_objects)
        missing = Counter()
        examples = {}
        for name in chosen_images:
            source = name.split('/')[0]
            if source == 'from_web':
                continue
            if not (root/name).is_file():
                missing[source]+=1
                examples.setdefault(source,[])
                if len(examples[source])<3:
                    examples[source].append(name)
        print('selected_missing_nonweb_images',missing)
        print('missing_examples',examples)
        print('invalid_boxes',invalid_boxes)
        for name in ['train2014','val2014']:
            p = root/'COCO'/name
            print('COCO_symlink',str(p),os.readlink(p) if p.is_symlink() else 'not a link')
        base = root/'数据集'
        if base.is_dir():
            print('extra_data_directory',[(p.name, p.is_dir()) for p in base.iterdir()])
        PY
    classes object 381 first= truck
    classes attribute 114 first= crumpled
    classes affordance 170 first= {'word': ['aim', 'take', 'train', 'take aim', 'direct'], 'define': 'point or cause to go (blows, weapons, or objects such as photographic equipment) towards\n'}
    split train images= 57416 objects= 135861
    split val images= 14446 objects= 25176
    split test images= 9101 objects= 25617
    test_top10 [('car', 1599), ('broccoli', 1282), ('boat', 1271), ('horse', 1229), ('dog', 1056), ('banana', 1050), ('truck', 1042), ('motorcycle', 1011), ('zebra', 928), ('sheep', 920)] objects= 11388
    all_top10 [('dog', 16171), ('bird', 13961), ('sheep', 13821), ('car', 11511), ('motorcycle', 8519), ('apple', 8382), ('cattle', 8379), ('broccoli', 8333), ('truck', 7769), ('elephant', 7032)]
    duplicate_image_records 0
    all_sources Counter({'COCO': 43841, 'ImageNet': 28586, 'from_web': 5384, 'aPY': 2791, 'SUN': 361})
    selected_images 35633 by_source Counter({'COCO': 25067, 'ImageNet': 7924, 'from_web': 1474, 'aPY': 1168})
    selected_objects_by_source Counter({'COCO': 76545, 'ImageNet': 14855, 'from_web': 9127, 'aPY': 3351})
    selected_missing_nonweb_images Counter({'ImageNet': 7924})
    missing_examples {'ImageNet': ['ImageNet/train/n03100240/n03100240_14168.JPEG', 'ImageNet/train/n03100240/n03100240_8483.JPEG', 'ImageNet/train/n03345487/n03345487_10424.JPEG']}
    invalid_boxes [('COCO/val2014/COCO_val2014_000000315601.jpg', 12, 'car', [0, 266, 4, 266])]
    COCO_symlink data/COCO/train2014 ../train2014
    COCO_symlink data/COCO/val2014 ../val2014
    extra_data_directory [('train2014.zip', False), ('val2014.zip', False)]
    ✓ • 4.45s

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 .venv/bin/python clip_inference.py --help
    usage: clip_inference.py [-h] [--data-root DATA_ROOT] [--model MODEL]
                             [--device DEVICE] [--num-workers NUM_WORKERS]
                             [--top-k TOP_K [TOP_K ...]] [--local-files-only]
                             [--output OUTPUT]
    
    Evaluate frozen Hugging Face CLIP on the ten largest OCL categories.
    
    options:
      -h, --help            show this help message and exit
      --data-root DATA_ROOT
      --model MODEL         Hugging Face ID or local model directory
      --device DEVICE       For example cuda, cuda:1, or cpu
      --num-workers NUM_WORKERS
      --top-k TOP_K [TOP_K ...]
      --local-files-only    Load model and processor from local files/cache only
      --output OUTPUT
    ✓ • 7.50s

## User

我来说明测试集的差异：这是个纯粹的测试任务，因此选出来的前十类数据全部都作为测试集

## Assistant

明白：合并三份标注，按对象实例数选出前十类，再将这些类别的全部有效对象作为测试集。当前实现与你的要求一致，无需修改划分逻辑。我会按这个口径给出指南，并将无法裁剪的异常框单独说明。

## Activity

    $ nl -ba utils/dataset/OCL_dataset.py
         1    from functools import lru_cache
         2    import sys
         3    import pickle
         4
         5    assert sys.version.startswith('3'), "Python version >= 3.8"
         6    from PIL import Image
         7    import numpy as np
         8    import os, json
         9    import logging
        10
        11    import torch, torchvision
        12    import torch.utils.data as tdata
        13
        14    from . import data_utils
        15
        16    class ImageDataset(tdata.Dataset):
        17        def __init__(self, phase):
        18            super(ImageDataset, self).__init__()
        19            self.logger = logging.getLogger(f"Dataset OCL")
        20            self.phase = phase
        21            self.transform = data_utils.imagenet_transform(phase)
        22
        23            # reading annotation pickle
        24            pkl_dir = "data/resources"
        25
        26            def load_pickle_and_assign_split(split):
        27                pkl_path = os.path.join(pkl_dir, f"OCL_annot_{split}.pkl")
        28                with open(pkl_path, 'rb') as fp:
        29                    pkl = pickle.load(fp)
        30                for x in pkl:
        31                    x['split'] = split
        32                return pkl
        33
        34            if phase == "train":
        35                self.pkl_data = load_pickle_and_assign_split("train")
        36            else:
        37                self.pkl_data = load_pickle_and_assign_split("val") + \
        38                        load_pickle_and_assign_split("test")
        39
        40            self.instance_indices = [(i, j) for i, img in enumerate(self.pkl_data) for j in range(len(img['objects']))]
        41            self.logger.info(f"{len(self.instance_indices)} instances")
        42
        43            # construct attr/aff/obj list/matrix
        44            def load_class_json(name):
        45                with open(os.path.join(pkl_dir, f"OCL_class_{name}.json"), "r") as fp:
        46                    return json.load(fp)
        47
        48            self.attrs = load_class_json("attribute")
        49            self.objs = load_class_json("object")
        50            self.affs = load_class_json("affordance")
        51            self.obj2id = {x: i for i, x in enumerate(self.objs)}
        52
        53            with open('data/resources/category_aff_matrix.json', "r") as fp:
        54                aff_matrix_file = json.load(fp)
        55                assert self.objs == aff_matrix_file['objs']
        56                self.aff_matrix = np.array(aff_matrix_file["aff_matrix"])
        57
        58            self.num_aff = self.aff_matrix.shape[1]
        59            self.num_attr = len(self.attrs)
        60            self.num_obj = len(self.objs)
        61
        62            logging.info("#obj %d, #attr %d, #aff %d" % (
        63                self.num_obj, self.num_attr, self.num_aff))
        64
        65
        66        def __len__(self):
        67            return len(self.pkl_data)
        68
        69        def __getitem__(self, index):
        70            info = self.pkl_data[index]
        71            objects = info["objects"]
        72            file_name = info["name"]
        73            file_path = os.path.join("data", file_name)
        74            image = Image.open(file_path).convert('RGB')
        75            image_width, image_height = image.size
        76
        77            attr = []
        78            aff = []
        79            gt_box = []
        80            for obj in objects:
        81                a = torch.zeros([self.num_attr]).float()
        82                a[obj['attr']] = 1
        83                attr.append(a)
        84
        85                b = torch.zeros([self.num_aff]).float()
        86                b[obj['aff']] = 1
        87                aff.append(b)
        88
        89                x = obj.get('box', [0, 0, image_width, image_height])
        90                gt_box.append(x)
        91
        92            attr = torch.stack(attr, 0)
        93            aff = torch.stack(aff, 0)
        94
        95
        96            if max(image_width, image_height) > 1800:
        97                image_width, image_height = image_width // 2, image_height // 2
        98                resize_trans = torchvision.transforms.Resize((image_width, image_height))
        99                image = resize_trans(image)
       100                gt_box = [(x[0] // 2, x[1] // 2, x[2] // 2, x[3] // 2) for x in gt_box]
       101            image = self.transform(image)
       102
       103
       104            sample = {
       105                "image": image,
       106                "file_name": file_name,
       107                "gt_bbox": np.array(gt_box, dtype=np.float32),
       108                'gt_aff': aff,
       109                "gt_attr": attr,
       110                'gt_obj_id': np.array([self.obj2id[obj['obj']] for obj in objects]),
       111                'val_mask': np.array([info['split'] == 'val' for _ in objects])
       112            }
       113
       114            sample["main_bbox"] = sample["gt_bbox"]
       115
       116            return sample
       117
       118
       119
       120    class FeatureDataset(ImageDataset):
       121        def __init__(self, phase, feature_dir):
       122            super(FeatureDataset, self).__init__(phase)
       123
       124            # reading feature .t7
       125            feature_path = os.path.join(feature_dir, f"{phase}.t7")
       126            logging.info("reading " + feature_path)
       127
       128            # load features into memory
       129            self.features_list, self.feature_dim = data_utils.features_loader(feature_path, self.pkl_data)
       130
       131        def __len__(self):
       132            return len(self.instance_indices)
       133
       134        @lru_cache(maxsize=None)
       135        def __getitem__(self, index):
       136            imgId, instId = self.instance_indices[index]
       137            img = self.pkl_data[imgId]
       138            obj = img['objects'][instId]
       139
       140            feature = self.features_list[imgId][instId, ...]
       141
       142            obj_id = self.obj2id[obj['obj']]
       143
       144            attr = torch.zeros([self.num_attr]).float()
       145            attr[obj['attr']] = 1
       146
       147            aff = torch.zeros([self.num_aff]).float()
       148            aff[obj['aff']] = 1
       149
       150
       151            sample = {
       152                "image": feature,
       153                "gt_attr": attr,
       154                'gt_obj_id': np.array(obj_id, dtype=int),
       155                'gt_aff': aff,
       156            }
       157
       158            # add val/test mask
       159            if 'split' in img:
       160                sample['val_mask'] = np.array(img['split'] == "val")
       161            sample['gt_causal'] = np.array(obj['causal'],dtype=int) if 'causal' in obj else []
       162
       163            return sample
    ✓ • 12ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        root = Path('/home/linfu/src/Test/ObjectConceptLearning')
        for name in ['clip_dataset.py','clip_inference.py','requirements-clip.txt','setup_clip_gpu.sh','docs/clip_inference.md','tests/test_clip_category_selection.py']:
            p = root/name
            print(name, p.stat().st_size)
        base = root/'data/数据集'
        if base.is_dir():
            for path in sorted(base.iterdir()):
                print('extra', path.name, 'directory' if path.is_dir() else f'{path.stat().st_size} bytes')
        PY
    clip_dataset.py 8669
    clip_inference.py 9687
    requirements-clip.txt 214
    setup_clip_gpu.sh 1289
    docs/clip_inference.md 8564
    tests/test_clip_category_selection.py 3712
    extra train2014.zip 13510573713 bytes
    extra val2014.zip 6645013297 bytes
    ✓ • 71ms

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 .venv/bin/python - <<'PY'
        import importlib.metadata as metadata
        import torch
        for name in ['torch','torchvision','transformers','numpy','Pillow','scikit-learn','tqdm','huggingface-hub']:
            print(name, metadata.version(name))
        print('cuda_build',torch.version.cuda)
        print('cuda_available',torch.cuda.is_available())
        from huggingface_hub import scan_cache_dir
        try:
            cache = scan_cache_dir()
            print('cached_clip_models', sorted(repo.repo_id for repo in cache.repos if 'clip' in repo.repo_id.lower()))
        except Exception as error:
            print('cache_status',type(error).__name__)
        PY
    torch 2.8.0+cpu
    torchvision 0.23.0+cpu
    transformers 4.57.1
    numpy 2.2.6
    Pillow 11.3.0
    scikit-learn 1.7.2
    tqdm 4.67.1
    huggingface-hub 0.36.2
    cuda_build None
    cuda_available False
    cache_status CacheNotFound
    ✓ • 2.94s

## Activity

    $ python - <<'PY'
        from pathlib import Path
        import pickle
        from collections import Counter
        root = Path('data')
        records = []
        for split in ('train','val','test'):
            with (root/'resources'/f'OCL_annot_{split}.pkl').open('rb') as f:
                records.extend(pickle.load(f))
        counts = Counter(obj['obj'] for row in records for obj in row['objects'])
        selected = set(name for name,_ in sorted(counts.items(),key=lambda item:(-item[1],item[0]))[:10])
        imagenet = [row for row in records if row['name'].startswith('ImageNet/') and any(obj['obj'] in selected for obj in row['objects'])]
        print('ImageNet selected path groups',dict(Counter('/'.join(row['name'].split('/')[:2]) for row in imagenet)))
        for split in ('train','val'):
            examples = [row['name'] for row in imagenet if row['name'].startswith(f'ImageNet/{split}/')][:2]
            print(split, examples)
        PY
    ImageNet selected path groups {'ImageNet/train': 7702, 'ImageNet/val': 222}
    train ['ImageNet/train/n03100240/n03100240_14168.JPEG', 'ImageNet/train/n03100240/n03100240_8483.JPEG']
    val ['ImageNet/val/ILSVRC2012_val_00023687.JPEG', 'ImageNet/val/ILSVRC2012_val_00045359.JPEG']
    ✓ • 3.58s

## Assistant

已确认主要数据缺口：当前 `data/ImageNet` 不存在，前十类中有 7,924 张图片依赖它；COCO 和 aPY 的所需路径均可找到。按你确认的口径，共选中 103,878 个对象，代码会记录并排除其中 1 个零高度框，最终评估 103,877 个对象。已有两项类别筛选测试通过，命令行入口也可正常加载；服务器上仍需验证 GPU 和真实模型推理。

## Assistant

按你确认的口径：**合并 train、val、test 三份标注，按对象实例数选择前十类，再将这些类别的全部有效对象用于测试。当前代码已经实现了这个逻辑。**

接下来主要需要完成三件事：**在服务器建立 GPU 环境、补齐 ImageNet 图片、验证并运行现有 CLIP 程序。**

| 角度 | 当前检查结果 | 接下来要做 |
|---|---|---|
| 环境准备 | 本地是 Python 3.12、CPU 版 PyTorch；已有 GPU 安装脚本 | 在服务器重新建立环境，验证 CUDA |
| 数据准备 | 按假设，`from_web` 已完整；所需 COCO、aPY 路径均存在；`data/ImageNet` 缺失 | 补齐本次测试涉及的 7,924 张 ImageNet 图片 |
| 代码完备 | 数据加载、对象裁剪、CLIP 推理和指标计算均已实现；两项类别筛选测试通过 | 准备模型权重，执行数据预检、小批量验证和完整测试 |

以下命令除特别注明外，都在服务器的 **`ObjectConceptLearning` 项目根目录**执行。

一、环境准备

**步骤 1：上传当前工作目录中的程序。**

至少包含：

```text
ObjectConceptLearning/
  clip_dataset.py
  clip_inference.py
  requirements-clip.txt
  setup_clip_gpu.sh
  Test.md
  tests/
  docs/clip_inference.md
  data/
```

这些 CLIP 文件目前有部分尚未提交到 Git，因此仅在服务器克隆原始仓库会遗漏它们。上传本地现有文件，并在服务器重建 `.venv`。

本次实验使用 [requirements-clip.txt](/home/linfu/src/Test/ObjectConceptLearning/requirements-clip.txt)，其中固定了：

```text
Python       3.12
torch        2.8.0
torchvision  0.23.0
transformers 4.57.1
```

原始 `requirements.txt` 对应旧版 OCRN 环境，不能与这套依赖混装。

**步骤 2：检查服务器 GPU，安装 uv 和 Python。**

```bash
cd /你的路径/ObjectConceptLearning

nvidia-smi

curl -LsSf https://astral.sh/uv/install.sh -o /tmp/uv-install.sh
sh /tmp/uv-install.sh
export PATH="$HOME/.local/bin:$PATH"

uv python install 3.12
```

`nvidia-smi` 应能显示分配给你的 NVIDIA GPU。单卡即可运行本实验；实际显存需求以随后的小批量验证为准。

**步骤 3：建立 GPU 环境。**

```bash
bash setup_clip_gpu.sh
source .venv/bin/activate
python -m pip check
```

[setup_clip_gpu.sh](/home/linfu/src/Test/ObjectConceptLearning/setup_clip_gpu.sh) 会创建环境、安装 CUDA 版依赖，并验证 `torch.cuda.is_available()`。

验收条件是脚本输出 GPU 型号、PyTorch/CUDA 版本以及：

```text
GPU environment ready.
```

如果自动选择后 CUDA 不可用，需要检查驱动与 PyTorch CUDA 构建的兼容性；脚本也支持显式选择 `cu128` 或 `cu126`。这一步通过后，再继续模型推理。

二、数据准备

**步骤 4：按本次选中的对象补齐图片。**

我重新统计了三份标注，前十类依次为：

```text
dog, bird, sheep, car, motorcycle,
apple, cattle, broccoli, truck, elephant
```

共涉及 **35,633 张图片、103,878 个标注对象**：

| 图片来源 | 所需不同图片数 | 当前本地状态 |
|---|---:|---|
| COCO | 25,067 | 所需路径均存在 |
| ImageNet | 7,924 | 缺失 |
| from_web | 1,474 | 按你的前提，已准备完整 |
| aPY | 1,168 | 所需路径均存在 |
| SUN | 0 | 当前前十类无需读取 |

这里的“路径存在”尚不代表每张图片都经过了解码检查。

ImageNet 是当前明确的数据缺口，其中包括 **7,702 张 train 图片和 222 张 val 图片**。服务器上需要形成这样的结构：

```text
data/
  resources/
    OCL_annot_train.pkl
    OCL_annot_val.pkl
    OCL_annot_test.pkl
    OCL_class_object.json
    OCL_class_attribute.json
    OCL_class_affordance.json
  COCO/
    train2014/
    val2014/
  ImageNet/
    train/
      n03100240/
        n03100240_14168.JPEG
      ...
    val/
      ILSVRC2012_val_00023687.JPEG
      ...
  aPY/
    VOCdevkit/
    ayahoo_test_images/
  from_web/
```

如果服务器已有 ImageNet，可以将 `data/ImageNet` 链接到现有目录，但必须核对标注中的相对路径。尤其注意：这里的验证图片路径是直接位于 `ImageNet/val/` 下，部分 ImageNet 副本会按类别重新组织验证集。

本次实验只要求选中对象所引用的图片齐全；无需为了运行这些对象而补齐其他类别的全部图片。

**步骤 5：处理上传时的软链接和标注文件。**

你本地的 COCO 目录实际使用了：

```text
data/COCO/train2014 -> ../train2014
data/COCO/val2014   -> ../val2014
```

上传时必须同时上传链接目标，或者使用 `rsync -L` 将链接对应的实际图片复制过去。例如，在本地执行：

```bash
rsync -avPL data/COCO USER@HOST:/你的路径/ObjectConceptLearning/data/
```

三个 `OCL_annot_*.pkl` 和三个类别 JSON 必须全部上传。标注含义为：

| 字段 | 含义 |
|---|---|
| `obj` | 对象类别名称；完整词表包含 381 类 |
| `box` | 像素坐标 `[xmin, ymin, xmax, ymax]` |
| `attr` | 114 个属性标签中的正例索引 |
| `aff` | 170 个可供性标签中的正例索引 |

`attr`、`aff` 都是多标签，当前代码会转换成 multi-hot 向量。

另外，[prepare_data.sh](/home/linfu/src/Test/ObjectConceptLearning/data/prepare_data.sh:32) 存在重复执行时的目录问题：aPY 段的 `cd ..` 位于条件分支内部，已有图片目录时会留在错误的工作目录。**对于已经准备好的数据，按上述结构校验即可。** 如果还要重新运行该脚本，应先将那条 `cd ..` 移到 `fi` 之后。

三、代码完备与执行

**步骤 6：确认现有实现覆盖要求。**

| `Test.md` 要求 | 当前实现 |
|---|---|
| 自定义 PyTorch `Dataset` | `OCLClipDataset` |
| 按样本数选前十类 | 合并三份标注后，按对象实例数排序 |
| 一张图片中的多个对象分别推理 | 按每个对象的标注框裁剪 |
| 图像预处理、文本 tokenization | 使用 CLIP processor 和 tokenizer |
| `batch_size=4` | 已固定；每批是四个对象 |
| 预训练模型、GPU、冻结参数、推理模式 | `load_model` 和 `torch.inference_mode()` |
| 余弦相似度和 Top-k accuracy | 特征归一化后计算点积，累计全部对象的正确数 |
| 属性与可供性 mAP | 分别计算每个标签 AP，再求均值 |
| 保存实验结果 | 输出 `metrics.json` |

核心代码见 [clip_dataset.py](/home/linfu/src/Test/ObjectConceptLearning/clip_dataset.py) 和 [clip_inference.py](/home/linfu/src/Test/ObjectConceptLearning/clip_inference.py)。

本次实验可以直接使用这条 CLIP 推理流程，无需执行原仓库的 OCRN 三阶段训练。

有一个已知数据例外：选中的一个 `car` 对象框为 `[0, 266, 4, 266]`，高度为零。代码会明确记录并排除它。因此，当前标注对应的最终有效对象数为 **103,877**。

**步骤 7：准备 CLIP 模型权重。**

在可以联网、且安装好上述环境的机器上执行：

```bash
python - <<'PY'
from transformers import CLIPModel, CLIPProcessor

name = "openai/clip-vit-base-patch32"
target = "./weights/clip-vit-base-patch32"

CLIPProcessor.from_pretrained(
    name, use_fast=False
).save_pretrained(target)

CLIPModel.from_pretrained(name).save_pretrained(target)
print("Model saved:", target)
PY
```

如果服务器不能访问 Hugging Face，在其他联网机器执行后，将整个 `weights/clip-vit-base-patch32/` 上传到服务器。该目录同时包含模型、预处理和 tokenizer 所需文件。

**步骤 8：执行现有测试和小批量验证。**

先运行已有回归测试：

```bash
python -m unittest discover \
  -s tests \
  -p 'test_clip_category_selection.py' \
  -v
```

再执行下面的检查。它会验证选中图片的路径、读取第一批对象，并在 GPU 上计算三种任务的相似度：

```bash
python - <<'PY'
import torch
import torch.nn.functional as F

from clip_dataset import load_dataset
from clip_inference import load_model, encode_candidate_labels

device = torch.device("cuda")
model, processor = load_model(
    "./weights/clip-vit-base-patch32",
    device,
    local_files_only=True,
)
dataset, loader = load_dataset(
    "./data", processor, num_workers=0
)

names = {item.image_name for item in dataset.instances}
missing = sorted(
    name for name in names
    if not (dataset.data_root / name).is_file()
)

print("Categories:", dataset.selection_category_counts)
print("Images:", dataset.num_images)
print("Objects:", len(dataset))
print("Excluded:", len(dataset.excluded_objects))
print("Missing:", len(missing), missing[:10])

if missing:
    raise SystemExit("Complete the missing images before inference.")

batch = next(iter(loader))
print("Image batch:", tuple(batch["pixel_values"].shape))

with torch.inference_mode():
    text = encode_candidate_labels(model, dataset.text_inputs, device)
    image = F.normalize(
        model.get_image_features(
            pixel_values=batch["pixel_values"].to(device)
        ).float(),
        dim=-1,
    )
    for task, embeddings in text.items():
        scores = image @ embeddings.T
        assert torch.isfinite(scores).all()
        print(task, tuple(scores.shape))

print("Smoke test passed.")
PY
```

预期关键输出：

```text
Images: 35633
Objects: 103877
Excluded: 1
Missing: 0
Image batch: (4, 3, 224, 224)
category (4, 10)
attribute (4, 114)
affordance (4, 170)
Smoke test passed.
```

这验证了全部所需路径和第一批的真实推理。正式长任务前，建议进一步逐图解码检查，以提前发现损坏图片；当前程序遇到缺图或无法使用的图片会报错。

**步骤 9：执行完整测试。**

```bash
mkdir -p logs/clip_inference

CUDA_VISIBLE_DEVICES=0 nohup python -u clip_inference.py \
  --data-root ./data \
  --model ./weights/clip-vit-base-patch32 \
  --local-files-only \
  --device cuda \
  --num-workers 4 \
  --top-k 1 5 \
  --output logs/clip_inference/metrics.json \
  > logs/clip_inference/run.log 2>&1 &
```

查看进度：

```bash
tail -f logs/clip_inference/run.log
```

当前有效对象数对应 **25,970 个 batch**，最后一批只有一个对象。代码按全部对象累计正确率，能够正确处理最后的小批次。如果服务器的 DataLoader 多进程出现问题，将 `--num-workers` 改为 `0`。

**步骤 10：检查结果并保存实验记录。**

正常完成后，应获得：

```text
logs/clip_inference/run.log
logs/clip_inference/metrics.json
```

检查结果中是否包含：

- 实际评估对象数 `103877`，排除对象数 `1`。
- 十个类别及其筛选数量、实际评估数量。
- Category Top-1、Top-5 accuracy。
- Attribute mAP、Affordance mAP，以及逐标签 AP。
- 模型名称、提示词、GPU 和 PyTorch/CUDA 版本。

JSON 中指标使用 `0～1`，终端显示百分比。属性和可供性 mAP 都在这批选中对象上计算；没有正例的标签不参与平均，结果会记录参与评估的标签数量。

我目前完成的是代码核对、标注统计、非 web 图片路径检查和两项已有测试。**真实 GPU 推理和最终指标仍需在服务器执行步骤 8～10 后确认。**

## User

我该用什么方式把这个项目传到指定的服务器上呢？以及imagenet

## Assistant

我会给你一套可替换服务器地址后使用的传输命令，并说明如何准备和放置 ImageNet。先确认本机可用的传输工具和项目数据目录。

## Activity

    $ command -v rsync ssh scp tar
    /usr/bin/rsync
    /usr/bin/ssh
    /usr/bin/scp
    /usr/bin/tar
    ✓ • 89ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        root = Path('/home/linfu/src/Test/ObjectConceptLearning')
        for name in ['clip_dataset.py','clip_inference.py','requirements-clip.txt','setup_clip_gpu.sh','tests','docs','Test.md','data/resources','data/COCO/train2014','data/COCO/val2014','data/train2014','data/val2014','data/aPY','data/from_web','data/ImageNet']:
            p = root/name
            print(f'{name}: exists={p.exists()}, symlink={p.is_symlink()}')
        PY
    clip_dataset.py: exists=True, symlink=False
    clip_inference.py: exists=True, symlink=False
    requirements-clip.txt: exists=True, symlink=False
    setup_clip_gpu.sh: exists=True, symlink=False
    tests: exists=True, symlink=False
    docs: exists=True, symlink=False
    Test.md: exists=True, symlink=False
    data/resources: exists=True, symlink=False
    data/COCO/train2014: exists=True, symlink=True
    data/COCO/val2014: exists=True, symlink=True
    data/train2014: exists=True, symlink=False
    data/val2014: exists=True, symlink=False
    data/aPY: exists=True, symlink=False
    data/from_web: exists=True, symlink=False
    data/ImageNet: exists=False, symlink=False
    ✓ • 202ms

## Assistant

本机已有 `rsync` 和 SSH，适合上传这些数据，传输中断后也可以继续补传。我会根据前十类的标注生成两份图片清单：一份用于上传 COCO、aPY 和 web 图片，另一份列出所需的 7,924 张 ImageNet 图片，方便从现有 ImageNet 副本中按需复制。

## Activity

    $ python - <<'PY'
        from collections import Counter
        from pathlib import Path
        import json
        import pickle
        
        root = Path('/home/linfu/src/Test/ObjectConceptLearning/data')
        records = []
        for split in ('train', 'val', 'test'):
            with (root / 'resources' / f'OCL_annot_{split}.pkl').open('rb') as handle:
                records.extend(pickle.load(handle))
        counts = Counter(obj['obj'] for record in records for obj in record['objects'])
        top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10]
        selected = {name for name, _ in top}
        image_names = sorted({
            record['name'] for record in records
            if any(obj['obj'] in selected for obj in record['objects'])
        })
        non_imagenet = [name for name in image_names if not name.startswith('ImageNet/')]
        imagenet = [name.removeprefix('ImageNet/') for name in image_names if name.startswith('ImageNet/')]
        assert len(image_names) == 35633
        assert len(non_imagenet) == 27709
        assert len(imagenet) == 7924
        assert all(not Path(name).is_absolute() and '..' not in Path(name).parts for name in image_names)
        folder = root / 'transfer_lists'
        outputs = {
            'ocl_non_imagenet.txt': '\n'.join(non_imagenet) + '\n',
            'imagenet_required.txt': '\n'.join(imagenet) + '\n',
            'selection.json': json.dumps({
                'selection_splits': ['train', 'val', 'test'],
                'count_unit': 'object_instance',
                'selected_categories': dict(top),
                'num_selected_objects_before_box_filter': sum(count for _, count in top),
                'num_selected_images': len(image_names),
                'images_by_source': dict(sorted(Counter(name.split('/')[0] for name in image_names).items())),
                'manifest_roots': {'ocl_non_imagenet.txt': 'data/', 'imagenet_required.txt': 'data/ImageNet/'},
                'note': 'Manifests contain every selected image path, without filtering by local availability.',
            }, indent=2) + '\n',
        }
        for name in outputs:
            if (folder / name).exists():
                raise SystemExit(f'Refusing to overwrite existing file: {folder / name}')
        folder.mkdir(exist_ok=True)
        for name, content in outputs.items():
            (folder / name).write_text(content, encoding='ascii')
            print(f'Created {folder / name}')
        print(f'Non-ImageNet images: {len(non_imagenet)}')
        print(f'ImageNet images: {len(imagenet)}')
        print('ImageNet splits:', dict(Counter(name.split('/')[0] for name in imagenet)))
        PY
    Created /home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/ocl_non_imagenet.txt
    Created /home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/imagenet_required.txt
    Created /home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/selection.json
    Non-ImageNet images: 27709
    ImageNet images: 7924
    ImageNet splits: {'train': 7702, 'val': 222}
    ✓ • 4.99s

## Assistant

建议使用 **`rsync + SSH`**。本机已经安装好这些工具，适合传输大量图片；中断后重复执行同一命令即可补传。

ImageNet 优先使用服务器已有的数据集。如果需要从本地上传，只传本次实验需要的 **7,924 张图片**即可。

我已根据当前标注生成两份清单：

| 清单 | 内容 |
|---|---|
| [ocl_non_imagenet.txt](/home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/ocl_non_imagenet.txt) | 27,709 张 COCO、aPY、web 图片，路径相对于 `data/` |
| [imagenet_required.txt](/home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/imagenet_required.txt) | 7,924 张 ImageNet 图片，路径相对于 ImageNet 根目录 |

清单覆盖选中类别的全部图片，没有因为本地缺文件而跳过任何图片。

**步骤 1：填写服务器信息。**

以下命令在**本地终端**执行。将用户名、服务器地址、端口和目标目录替换为实际值：

```bash
cd /home/linfu/src/Test/ObjectConceptLearning

OCL_TARGET='USER@SERVER_IP'
OCL_PORT=22
OCL_REMOTE='/home/USER/ObjectConceptLearning'
```

测试登录并创建目标目录：

```bash
ssh -p "$OCL_PORT" "$OCL_TARGET"

# 登录成功后，退出回到本地
exit
```

```bash
ssh -p "$OCL_PORT" "$OCL_TARGET" \
  "mkdir -p '$OCL_REMOTE/data'"
```

服务器也需要安装 `rsync`。

**步骤 2：上传程序、标注和传输清单。**

在本地执行：

```bash
rsync -avP \
  -e "ssh -p $OCL_PORT" \
  --exclude='__pycache__/' \
  *.py *.sh requirements*.txt README.md Test.md LICENSE \
  config models utils tests docs \
  "$OCL_TARGET:$OCL_REMOTE/"
```

```bash
rsync -avP \
  -e "ssh -p $OCL_PORT" \
  data/resources \
  data/transfer_lists \
  data/prepare_data.sh \
  data/download_web_images.py \
  "$OCL_TARGET:$OCL_REMOTE/data/"
```

这样会上传当前工作目录里的 CLIP 程序，包括尚未提交到 Git 的文件。服务器上的 Python 环境按照上一条指南重新建立，模型权重也可以直接在服务器下载。

**步骤 3：上传本次测试需要的非 ImageNet 图片。**

在本地执行：

```bash
rsync -aL --partial --info=progress2 \
  -e "ssh -p $OCL_PORT" \
  --files-from=data/transfer_lists/ocl_non_imagenet.txt \
  data/ \
  "$OCL_TARGET:$OCL_REMOTE/data/"
```

这里：

- `--files-from`：只传清单中的图片，并保留目录结构。
- `-L`：跟随本地 COCO 的软链接，上传实际图片。
- `--partial`：保留未完成的传输，方便再次执行时补传。

这些命令不包含删除服务器文件的选项。如果出现 `No such file or directory`，需要补齐对应源文件后重新执行，不能将这次传输视为完成。

**步骤 4：根据实际情况准备 ImageNet。**

需要的是 **ImageNet-1K / ILSVRC2012 原始图片**。OCL 标注框使用像素坐标，因此图片应保持原始尺寸。

有三种情况：

**情况 A：服务器已经有 ImageNet，优先使用这一种。**

登录服务器，在项目根目录执行。假设共享数据集位于 `/shared/datasets/ILSVRC2012`，且项目中的 `data/ImageNet` 尚不存在：

```bash
cd /你的路径/ObjectConceptLearning

ln -s /shared/datasets/ILSVRC2012 data/ImageNet
```

需要匹配这样的布局：

```text
data/ImageNet/
  train/
    n03100240/
      n03100240_14168.JPEG
    ...
  val/
    ILSVRC2012_val_00023687.JPEG
    ...
```

特别检查 `val/`：OCL 使用的是直接放置验证图片的路径。如果共享数据集的验证图片按类别分目录，需要在项目侧建立与标注匹配的目录或链接。

**情况 B：本地或另一台机器已经有 ImageNet。**

在同时能访问 ImageNet 和传输清单的机器上执行：

```bash
rsync -aL --partial --info=progress2 \
  -e "ssh -p $OCL_PORT" \
  --files-from=data/transfer_lists/imagenet_required.txt \
  /本地ImageNet根目录/ \
  "$OCL_TARGET:$OCL_REMOTE/data/ImageNet/"
```

`/本地ImageNet根目录/` 下应该直接包含 `train/`、`val/`。

这只上传所需的：

```text
train：7,702 张
val：    222 张
合计： 7,924 张
```

**情况 C：本地和服务器都没有 ImageNet。**

从 [ImageNet 官方下载页面](https://www.image-net.org/download.php) 获取访问权限，下载：

```text
ILSVRC2012_img_train.tar
ILSVRC2012_img_val.tar
```

建议直接下载到服务器，避免再上传完整压缩包。完整下载和展开需要预留数百 GB 空间，尤其是保留外层压缩包和训练集内部分类压缩包时。

在服务器项目根目录执行下面的解压命令，先替换两个下载路径：

```bash
bash -e <<'SH'
mkdir -p data/ImageNet/train data/ImageNet/val

tar -xf /下载路径/ILSVRC2012_img_train.tar \
  -C data/ImageNet/train

# 训练集外层压缩包中，每个类别还有一个 tar，需要再次解压。
for ocl_archive in data/ImageNet/train/*.tar; do
  ocl_class="${ocl_archive##*/}"
  ocl_class="${ocl_class%.tar}"
  mkdir -p "data/ImageNet/train/$ocl_class"
  tar -xf "$ocl_archive" -C "data/ImageNet/train/$ocl_class"
done

tar -xf /下载路径/ILSVRC2012_img_val.tar \
  -C data/ImageNet/val
SH
```

这里使用的是 ILSVRC2012 的 train 和 val **图片来源**；按你确定的实验口径，其中选中对象仍然全部用于测试。

**步骤 5：在服务器验证图片是否全部到位。**

在服务器项目根目录执行：

```bash
python3 - <<'PY'
from pathlib import Path

data = Path("data")
checks = [
    ("ocl_non_imagenet.txt", data),
    ("imagenet_required.txt", data / "ImageNet"),
]

total_missing = 0
for filename, root in checks:
    names = (data / "transfer_lists" / filename).read_text().splitlines()
    missing = [name for name in names if not (root / name).is_file()]
    print(f"{filename}: expected={len(names)}, missing={len(missing)}")
    for name in missing[:10]:
        print("  MISSING:", root / name)
    total_missing += len(missing)

raise SystemExit(1 if total_missing else 0)
PY
```

预期输出：

```text
ocl_non_imagenet.txt: expected=27709, missing=0
imagenet_required.txt: expected=7924, missing=0
```

这个检查确认文件路径完整。通过后，再按上一条指南建立 GPU 环境、执行小批量推理并启动完整测试。

目前已生成传输清单，尚未连接服务器或上传文件。

## User

情况C，请你给出可行的纯命令行操作

## Assistant

我先核实 ImageNet 官方下载入口的命令行访问方式，再给你一套可在服务器执行的下载、解压和校验命令；重点确认登录授权是否会影响直接下载。

## Activity

    $ curl -L --fail --silent --show-error --max-time 30 https://www.image-net.org/download.php
    <?php
    require('user.php');
    require('common.php');
    $userid = $session->userID();
    $userinfo = $session->getUserInfo();
    $requestid = $userdb->getLiveRequestID($userid);
    $requestinfo = $userdb->getRequestInfo($requestid);
    if( $session->loggedIn() ) {
        redirect_to('download-images.php');
    }
    require('commonheader.php');
    ?>
    
    <div id="wrap">
      <div id="main">
        <h3>
        Download
        </h3>
        <br clear="all">
        <div class="hr"></div>
        <div id="about_content" class="aboutoverview">
          <?php if( !$session->loggedIn() ): ?>
            <h5>Download ImageNet Data</h5>
            The most highly-used subset of ImageNet is the <a href="./challenges/LSVRC/index.php">ImageNet Large Scale Visual Recognition Challenge (ILSVRC)</a> 2012-2017 image classification and localization dataset. This dataset spans 1000 object classes and contains 1,281,167 training images, 50,000 validation images and 100,000 test images. This subset is available on <a href="https://www.kaggle.com/c/imagenet-object-localization-challenge/overview/description">Kaggle</a>.
            <br><br>
            For access to the full ImageNet dataset and other commonly used subsets, please login or request access. In doing so, you will need to agree to our terms of access.
            <br><br>
            Terms of access:
            <div class="accessagreement">
            <?php
            include('accessagreement.php');
            ?>
            </div>
          <?php endif; ?>
        </div><!--/about_content-->
      </div><!--/main-->
    </div><!--/wrap-->
    
    <br clear="all">
    
    <p>
    <?php
    require('commonfooter.php');
    ?>
    ✓ • 2.05s

## Activity

    $ curl -L --fail --silent --show-error --head --max-time 30 https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar
    HTTP/1.1 200 OK
    Date: Thu, 22 Oct 2026 15:30:09 GMT
    Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
    Last-Modified: Thu, 14 Jun 2012 19:01:15 GMT
    ETag: "226f606800-4c27352eaf4c0"
    Accept-Ranges: bytes
    Content-Length: 147897477120
    Access-Control-Allow-Origin: *
    Content-Type: application/x-tar
    
    HTTP/1.1 200 OK
    Date: Thu, 22 Oct 2026 15:30:09 GMT
    Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
    Last-Modified: Thu, 14 Jun 2012 17:39:50 GMT
    ETag: "192076000-4c2722fbfc580"
    Accept-Ranges: bytes
    Content-Length: 6744924160
    Access-Control-Allow-Origin: *
    Content-Type: application/x-tar
    
    ✓ • 1.67s

## Activity

    $ rg -n -A 10 'ARCHIVE_META' .venv/lib/python3.12/site-packages/torchvision/datasets/imagenet.py
    14:ARCHIVE_META = {
    15-    "train": ("ILSVRC2012_img_train.tar", "1d675b47d978889d74fa0da5fadfb00e"),
    16-    "val": ("ILSVRC2012_img_val.tar", "29b22e2961454d5413ddabcf34fc5622"),
    17-    "devkit": ("ILSVRC2012_devkit_t12.tar.gz", "fa75699e90414af021442c21a62c3abf"),
    18-}
    19-
    20-META_FILE = "meta.bin"
    21-
    22-
    23-class ImageNet(ImageFolder):
    24-    """`ImageNet <http://image-net.org/>`_ 2012 Classification Dataset.
    --
    145:    archive_meta = ARCHIVE_META["devkit"]
    146-    if file is None:
    147-        file = archive_meta[0]
    148-    md5 = archive_meta[1]
    149-
    150-    _verify_archive(root, file, md5)
    151-
    152-    with get_tmp_dir() as tmp_dir:
    153-        extract_archive(os.path.join(root, file), tmp_dir)
    154-
    155-        devkit_root = os.path.join(tmp_dir, "ILSVRC2012_devkit_t12")
    --
    174:    archive_meta = ARCHIVE_META["train"]
    175-    if file is None:
    176-        file = archive_meta[0]
    177-    md5 = archive_meta[1]
    178-
    179-    _verify_archive(root, file, md5)
    180-
    181-    train_root = os.path.join(root, folder)
    182-    extract_archive(os.path.join(root, file), train_root)
    183-
    184-    archives = [os.path.join(train_root, archive) for archive in os.listdir(train_root)]
    --
    204:    archive_meta = ARCHIVE_META["val"]
    205-    if file is None:
    206-        file = archive_meta[0]
    207-    md5 = archive_meta[1]
    208-    if wnids is None:
    209-        wnids = load_meta_file(root)[1]
    210-
    211-    _verify_archive(root, file, md5)
    212-
    213-    val_root = os.path.join(root, folder)
    214-    extract_archive(os.path.join(root, file), val_root)
    ✓ • 366ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        from collections import Counter
        p = Path('transfer_lists/imagenet_required.txt')
        paths = p.read_text().splitlines()
        print('required_images', len(paths))
        print('splits', dict(Counter(name.split('/')[0] for name in paths)))
        print('train_synsets', len({name.split('/')[1] for name in paths if name.startswith('train/')}))
        print('preview', paths[:3])
        PY
    required_images 7924
    splits {'train': 7702, 'val': 222}
    train_synsets 190
    preview ['train/n01518878/n01518878_10004.JPEG', 'train/n01518878/n01518878_10706.JPEG', 'train/n01518878/n01518878_10878.JPEG']
    ✓ • 460ms

## Assistant

已核实：官方 train 和 val 直链目前都返回 tar 文件，并支持断点续传，无需交互式登录。两个压缩包合计约 154.6 GB。我会补一个命令行脚本，只解压清单中的 7,924 张图片，避免完整展开 ImageNet 占用更多空间。

## Activity

    $ python - <<'PY'
        from pathlib import Path
        import tempfile
        p = Path('extract_imagenet_subset.py')
        print('helper_exists', p.exists())
        print('temp_dir', tempfile.mkdtemp(prefix='ocl-imagenet-check-'))
        PY
    helper_exists False
    temp_dir /tmp/ocl-imagenet-check-egurnta3
    ✓ • 74ms

## User

我的服务器硬盘空间不足，有什么折衷的方法吗？目前只有100G的空间

## Assistant

可以。我们可以只准备本次测试需要的图片，并让服务器直接从下载流中解压，避免保存完整的 ImageNet 压缩包。这样能大幅降低磁盘需求，但如果传输中断，可能需要重新读取下载流。我会先检查所需图片的体积，再验证这个方案。

## Activity

    $ curl -L --fail --silent --show-error --max-time 30 --range 0-1023 --max-filesize 1048576 --dump-header - --output /tmp/ocl-imagenet-check-egurnta3/train-prefix.bin https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar
    HTTP/1.1 206 Partial Content
    Date: Thu, 22 Oct 2026 15:45:34 GMT
    Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
    Last-Modified: Thu, 14 Jun 2012 19:01:15 GMT
    ETag: "226f606800-4c27352eaf4c0"
    Accept-Ranges: bytes
    Content-Length: 1024
    Access-Control-Allow-Origin: *
    Content-Range: bytes 0-1023/147897477120
    Content-Type: application/x-tar
    
    ✓ • 1.31s

## Activity

    $ df -h /home/linfu/src/Test/ObjectConceptLearning/data
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sdd       1007G   66G  890G   7% /home/linfu/src/Test/ObjectConceptLearning/data
    ✓ • 162ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        from collections import defaultdict
        root = Path('/home/linfu/src/Test/ObjectConceptLearning/data')
        totals = defaultdict(lambda: [0, 0, 0])
        for name in (root/'transfer_lists/ocl_non_imagenet.txt').read_text().splitlines():
            source = name.split('/')[0]
            p = root/name
            if p.is_file():
                totals[source][0] += 1
                totals[source][1] += p.stat().st_size
            else:
                totals[source][2] += 1
        for source, (count, size, missing) in sorted(totals.items()):
            print(source, 'found=',count, 'GiB=',round(size/1024**3,3), 'missing=',missing)
        PY
    COCO found= 25067 GiB= 4.271 missing= 0
    aPY found= 1168 GiB= 0.13 missing= 0
    from_web found= 1205 GiB= 0.142 missing= 269
    ✓ • 2.81s

## Activity

    $ python - <<'PY'
        import tarfile
        from pathlib import Path
        header = Path('/tmp/ocl-imagenet-check-egurnta3/train-prefix.bin').read_bytes()
        member = tarfile.TarInfo.frombuf(header[:512], 'utf-8', 'strict')
        print('first_train_member', member.name)
        print('first_train_member_size', member.size)
        PY
    first_train_member n01440764.tar
    first_train_member_size 157368320
    ✓ • 160ms

## Assistant

当前工作机的文件系统报告约 890 GiB 可用，因此更直接的方案是：在本地下载压缩包，只解压所需图片，再上传到服务器。服务器所需的 COCO 和 aPY 图片合计约 4.4 GiB；加上选中的 ImageNet、web 图片和运行环境，通常能控制在 100 GB 内，同时保留原定的全部测试对象。

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/extract_imagenet_subset.py
    """Extract the OCL image manifest without expanding the whole ImageNet dataset."""
    
    from __future__ import annotations
    
    import argparse
    import os
    from pathlib import Path, PurePosixPath
    import shutil
    import sys
    import tarfile
    import tempfile
    
    
    def load_manifest(path: Path) -> list[str]:
        names = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not names or len(names) != len(set(names)):
            raise ValueError("The image manifest must be non-empty and contain no duplicates.")
        for name in names:
            path_parts = PurePosixPath(name).parts
            if (
                PurePosixPath(name).is_absolute()
                or ".." in path_parts
                or not (
                    (len(path_parts) == 3 and path_parts[0] == "train")
                    or (len(path_parts) == 2 and path_parts[0] == "val")
                )
            ):
                raise ValueError(f"Unexpected ImageNet path: {name}")
        return names
    
    
    def copy_image(archive: tarfile.TarFile, member: tarfile.TarInfo, destination: Path) -> bool:
        if not member.isfile() or member.size <= 0:
            raise ValueError(f"Expected a non-empty image file: {member.name}")
        if destination.is_file() and destination.stat().st_size == member.size:
            return False
    
        destination.parent.mkdir(parents=True, exist_ok=True)
        source = archive.extractfile(member)
        if source is None:
            raise ValueError(f"Cannot read archive member: {member.name}")
    
        temporary = None
        try:
            # Publish only complete files so an interrupted extraction can be rerun.
            with source, tempfile.NamedTemporaryFile(
                dir=destination.parent, prefix=f".{destination.name}.", suffix=".part", delete=False
            ) as output:
                temporary = Path(output.name)
                shutil.copyfileobj(source, output, length=1024 * 1024)
            if temporary.stat().st_size != member.size:
                raise ValueError(f"Incomplete archive member: {member.name}")
            os.replace(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return True
    
    
    def extract_images(
        archive: tarfile.TarFile,
        requested: dict[str, str],
        output_dir: Path,
        found: set[str],
    ) -> tuple[int, int]:
        remaining = dict(requested)
        copied = skipped = 0
        for member in archive:
            relative = remaining.pop(PurePosixPath(member.name).name, None)
            if relative is None:
                continue
            if copy_image(archive, member, output_dir / relative):
                copied += 1
            else:
                skipped += 1
            found.add(relative)
            if not remaining:
                break
        return copied, skipped
    
    
    def extract_subset(archive_dir: Path, output_dir: Path, names: list[str]) -> tuple[int, int]:
        train = {}
        val = {}
        for name in names:
            parts = PurePosixPath(name).parts
            if parts[0] == "train":
                train.setdefault(f"{parts[1]}.tar", {})[parts[2]] = name
            else:
                val[parts[1]] = name
    
        found = set()
        copied = skipped = 0
        if train:
            total_classes = len(train)
            completed_classes = 0
            with tarfile.open(archive_dir / "ILSVRC2012_img_train.tar", mode="r:") as outer:
                for member in outer:
                    requested = train.pop(PurePosixPath(member.name).name, None)
                    if requested is None:
                        continue
                    if not member.isfile():
                        raise ValueError(f"Expected a class archive: {member.name}")
                    class_file = outer.extractfile(member)
                    if class_file is None:
                        raise ValueError(f"Cannot read class archive: {member.name}")
                    # Uncompressed nested tar files support seeking; no class tar is written to disk.
                    with class_file, tarfile.open(fileobj=class_file, mode="r:") as inner:
                        new, existing = extract_images(inner, requested, output_dir, found)
                    copied += new
                    skipped += existing
                    completed_classes += 1
                    if completed_classes == 1 or completed_classes % 10 == 0 or not train:
                        print(
                            f"Train classes: {completed_classes}/{total_classes}; "
                            f"images copied: {copied}; size-matched existing images: {skipped}",
                            flush=True,
                        )
                    if not train:
                        break
    
        if val:
            with tarfile.open(archive_dir / "ILSVRC2012_img_val.tar", mode="r:") as archive:
                new, existing = extract_images(archive, val, output_dir, found)
            copied += new
            skipped += existing
    
        missing = sorted(set(names) - found)
        if missing:
            raise ValueError(
                f"{len(missing)} requested images were not found in the archives: {missing[:10]}"
            )
        print(f"Complete: {len(found)} images; copied={copied}; size-matched existing={skipped}.")
        print(f"Output directory: {output_dir.resolve()}")
        return copied, skipped
    
    
    def main() -> None:
        data_dir = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--archive-dir", type=Path, default=data_dir / "imagenet_archives")
        parser.add_argument("--output-dir", type=Path, default=data_dir / "ImageNet")
        parser.add_argument(
            "--manifest", type=Path, default=data_dir / "transfer_lists" / "imagenet_required.txt"
        )
        args = parser.parse_args()
        names = load_manifest(args.manifest.expanduser())
        extract_subset(args.archive_dir.expanduser(), args.output_dir.expanduser(), names)
    
    
    if __name__ == "__main__":
        try:
            main()
        except (OSError, ValueError, tarfile.TarError) as error:
            print(f"Error: {error}", file=sys.stderr)
            raise SystemExit(1)

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
        from contextlib import redirect_stdout
        from pathlib import Path
        import importlib.util
        import io
        import tarfile
        import tempfile
        from unittest.mock import patch
        
        spec = importlib.util.spec_from_file_location('subset', 'extract_imagenet_subset.py')
        subset = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(subset)
        
        def archive_bytes(entries):
            buffer = io.BytesIO()
            with tarfile.open(fileobj=buffer, mode='w') as archive:
                for name, data in entries:
                    entry = tarfile.TarInfo(name)
                    entry.size = len(data)
                    archive.addfile(entry, io.BytesIO(data))
            return buffer.getvalue()
        
        with tempfile.TemporaryDirectory(prefix='ocl-subset-test-') as directory:
            base = Path(directory)
            archives = base/'archives'
            archives.mkdir()
            output = base/'images'
            first = archive_bytes([('a.JPEG', b'image-a'), ('unused.JPEG', b'unused-after-first-image')])
            middle = archive_bytes([('unselected.JPEG', b'not-selected')])
            last = archive_bytes([('extra.JPEG', b'extra'), ('b.JPEG', b'image-b')])
            (archives/'ILSVRC2012_img_train.tar').write_bytes(archive_bytes([
                ('n00000001.tar', first), ('n00000002.tar', middle), ('n00000003.tar', last)
            ]))
            (archives/'ILSVRC2012_img_val.tar').write_bytes(archive_bytes([
                ('ILSVRC2012_val_00000001.JPEG', b'image-val'), ('other.JPEG', b'not-selected')
            ]))
            names = ['train/n00000001/a.JPEG', 'train/n00000003/b.JPEG', 'val/ILSVRC2012_val_00000001.JPEG']
            expected = dict(zip(names, [b'image-a', b'image-b', b'image-val']))
            with redirect_stdout(io.StringIO()):
                assert subset.extract_subset(archives, output, names) == (3, 0)
                assert subset.extract_subset(archives, output, names) == (0, 3)
                (output/names[0]).write_bytes(b'partial')
                assert subset.extract_subset(archives, output, names) == (0, 3)
                (output/names[0]).write_bytes(b'bad')
                assert subset.extract_subset(archives, output, names) == (1, 2)
            assert {str(p.relative_to(output)) for p in output.rglob('*') if p.is_file()} == set(names)
            assert all((output/name).read_bytes() == body for name, body in expected.items())
            assert not list(output.rglob('*.tar'))
            assert not list(output.rglob('*.part'))
            for extra in ['train/n00000001/missing.JPEG', 'train/n99999999/missing.JPEG']:
                try:
                    with redirect_stdout(io.StringIO()):
                        subset.extract_subset(archives, output, names+[extra])
                except ValueError as error:
                    assert 'not found' in str(error)
                else:
                    raise AssertionError('Missing image was not reported')
            for bad in ['../outside.JPEG\n', '/val/outside.JPEG\n', 'train/n1/a.JPEG\ntrain/n1/a.JPEG\n', '']:
                manifest = base/'bad.txt'
                manifest.write_text(bad)
                try:
                    subset.load_manifest(manifest)
                except ValueError:
                    pass
                else:
                    raise AssertionError(f'Invalid manifest accepted: {bad!r}')
            def interrupt_copy(source, destination, length):
                destination.write(b'incomplete')
                raise OSError('simulated interrupted extraction')
            interrupted_output = base/'interrupted'
            try:
                with patch.object(subset.shutil, 'copyfileobj', interrupt_copy):
                    subset.extract_subset(archives, interrupted_output, names)
            except OSError:
                pass
            else:
                raise AssertionError('Expected interruption')
            assert not [p for p in interrupted_output.rglob('*') if p.is_file()]
            real_names = subset.load_manifest(Path('transfer_lists/imagenet_required.txt'))
            assert len(real_names) == 7924
        print('PASS: nested archives, exact selection, reruns, size-mismatch recovery, missing images, invalid manifests, interrupted writes, real manifest count.')
        PY
    PASS: nested archives, exact selection, reruns, size-mismatch recovery, missing images, invalid manifests, interrupted writes, real manifest count.
    ✓ • 568ms

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 python extract_imagenet_subset.py --help
    usage: extract_imagenet_subset.py [-h] [--archive-dir ARCHIVE_DIR]
                                      [--output-dir OUTPUT_DIR]
                                      [--manifest MANIFEST]
    
    Extract the OCL image manifest without expanding the whole ImageNet dataset.
    
    options:
      -h, --help            show this help message and exit
      --archive-dir ARCHIVE_DIR
      --output-dir OUTPUT_DIR
      --manifest MANIFEST
    ✓ • 95ms

## Assistant

可以。**按服务器有 100 GB 可用空间来安排，推荐“本地下载完整压缩包 → 只提取所需图片 → 上传子集”。** 这样仍然覆盖原定的全部测试对象。

当前本机文件系统报告约 **890 GiB 可用空间**，适合承担下载。服务器只接收图片子集：

| 数据 | 服务器上需要保存的内容 |
|---|---|
| COCO | 25,067 张，实测约 4.27 GiB |
| aPY | 1,168 张，实测约 0.13 GiB |
| web | 选中的 1,474 张 |
| ImageNet | 选中的 7,924 张 |
| 环境、模型和缓存 | 建议另预留 15–25 GB |

代价是：**本地仍需下载约 154.6 GB 的 ImageNet 压缩包**，但上传到服务器的只有子集。

我已准备好 [extract_imagenet_subset.py](/home/linfu/src/Test/ObjectConceptLearning/data/extract_imagenet_subset.py)。它直接读取训练包内部的类别 tar，只提取清单中的图片，不会把全部 ImageNet 或中间类别 tar 展开到磁盘。

**步骤 1：在本地下载，暂时不要在服务器执行这些命令。**

官方直链已验证可用，并支持断点续传：

```bash
cd /home/linfu/src/Test/ObjectConceptLearning
mkdir -p data/imagenet_archives

curl -L --fail --retry 5 --connect-timeout 30 \
  --continue-at - \
  --output data/imagenet_archives/ILSVRC2012_img_train.tar \
  https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar

curl -L --fail --retry 5 --connect-timeout 30 \
  --continue-at - \
  --output data/imagenet_archives/ILSVRC2012_img_val.tar \
  https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar
```

如果中断，重新执行对应的 `curl` 命令即可续传。

**步骤 2：校验下载完整性。**

仍在本地项目根目录执行：

```bash
md5sum -c <<'EOF'
1d675b47d978889d74fa0da5fadfb00e  data/imagenet_archives/ILSVRC2012_img_train.tar
29b22e2961454d5413ddabcf34fc5622  data/imagenet_archives/ILSVRC2012_img_val.tar
EOF
```

两个文件都显示 `OK` 后继续。这两个校验值与 torchvision 的 ImageNet 数据集实现一致。

**步骤 3：只提取所需的 7,924 张图片。**

```bash
python3 data/extract_imagenet_subset.py \
  --archive-dir data/imagenet_archives \
  --manifest data/transfer_lists/imagenet_required.txt \
  --output-dir data/ImageNet

du -sh data/ImageNet
```

完成后应显示：

```text
Complete: 7924 images; ...
```

输出结构直接匹配 OCL 标注：

```text
data/ImageNet/
  train/
    n01518878/
      ...
  val/
    ILSVRC2012_val_*.JPEG
```

脚本可以重复执行，会跳过已存在且大小匹配的图片。

**步骤 4：仅上传 ImageNet 子集。**

替换服务器连接信息，在本地执行：

```bash
OCL_TARGET='USER@SERVER_IP'
OCL_PORT=22
OCL_REMOTE='/home/USER/ObjectConceptLearning'

ssh -p "$OCL_PORT" "$OCL_TARGET" \
  "mkdir -p '$OCL_REMOTE/data/ImageNet'"

rsync -a --partial --info=progress2 \
  -e "ssh -p $OCL_PORT" \
  data/ImageNet/ \
  "$OCL_TARGET:$OCL_REMOTE/data/ImageNet/"
```

**步骤 5：其他图片也按清单上传。**

```bash
rsync -aL --partial --info=progress2 \
  -e "ssh -p $OCL_PORT" \
  --files-from=data/transfer_lists/ocl_non_imagenet.txt \
  data/ \
  "$OCL_TARGET:$OCL_REMOTE/data/"
```

这条命令只上传所需的 COCO、aPY 和 web 图片。标注和程序继续按前一条指南上传；`data/imagenet_archives/` 留在本地。

在服务器上检查实际占用：

```bash
cd /你的路径/ObjectConceptLearning
df -h .
du -sh data
```

子集解压脚本已通过小型嵌套 tar 的筛选、重复执行和中断写入测试；尚未下载或解压完整 ImageNet。如果必须完全在这台 100 GB 服务器上准备，也可以采用流式提取，但下载中断后的恢复更复杂，当前更推荐上述本地准备方案。

## User

我能跳过本地完整下载的步骤吗，这会消耗大量的时间，而我时间很紧迫。只用索引下载有需要的文件。

## Assistant

可以尝试利用官方 tar 文件的 HTTP Range 支持，只读取索引信息和所需图片的数据段。我会验证这种方式，并准备可断点重跑的脚本，尽量减少下载量和磁盘占用。

## Activity

    $ cat extract_imagenet_subset.py
    """Extract the OCL image manifest without expanding the whole ImageNet dataset."""
    
    from __future__ import annotations
    
    import argparse
    import os
    from pathlib import Path, PurePosixPath
    import shutil
    import sys
    import tarfile
    import tempfile
    
    
    def load_manifest(path: Path) -> list[str]:
        names = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not names or len(names) != len(set(names)):
            raise ValueError("The image manifest must be non-empty and contain no duplicates.")
        for name in names:
            path_parts = PurePosixPath(name).parts
            if (
                PurePosixPath(name).is_absolute()
                or ".." in path_parts
                or not (
                    (len(path_parts) == 3 and path_parts[0] == "train")
                    or (len(path_parts) == 2 and path_parts[0] == "val")
                )
            ):
                raise ValueError(f"Unexpected ImageNet path: {name}")
        return names
    
    
    def copy_image(archive: tarfile.TarFile, member: tarfile.TarInfo, destination: Path) -> bool:
        if not member.isfile() or member.size <= 0:
            raise ValueError(f"Expected a non-empty image file: {member.name}")
        if destination.is_file() and destination.stat().st_size == member.size:
            return False
    
        destination.parent.mkdir(parents=True, exist_ok=True)
        source = archive.extractfile(member)
        if source is None:
            raise ValueError(f"Cannot read archive member: {member.name}")
    
        temporary = None
        try:
            # Publish only complete files so an interrupted extraction can be rerun.
            with source, tempfile.NamedTemporaryFile(
                dir=destination.parent, prefix=f".{destination.name}.", suffix=".part", delete=False
            ) as output:
                temporary = Path(output.name)
                shutil.copyfileobj(source, output, length=1024 * 1024)
            if temporary.stat().st_size != member.size:
                raise ValueError(f"Incomplete archive member: {member.name}")
            os.replace(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return True
    
    
    def extract_images(
        archive: tarfile.TarFile,
        requested: dict[str, str],
        output_dir: Path,
        found: set[str],
    ) -> tuple[int, int]:
        remaining = dict(requested)
        copied = skipped = 0
        for member in archive:
            relative = remaining.pop(PurePosixPath(member.name).name, None)
            if relative is None:
                continue
            if copy_image(archive, member, output_dir / relative):
                copied += 1
            else:
                skipped += 1
            found.add(relative)
            if not remaining:
                break
        return copied, skipped
    
    
    def extract_subset(archive_dir: Path, output_dir: Path, names: list[str]) -> tuple[int, int]:
        train = {}
        val = {}
        for name in names:
            parts = PurePosixPath(name).parts
            if parts[0] == "train":
                train.setdefault(f"{parts[1]}.tar", {})[parts[2]] = name
            else:
                val[parts[1]] = name
    
        found = set()
        copied = skipped = 0
        if train:
            total_classes = len(train)
            completed_classes = 0
            with tarfile.open(archive_dir / "ILSVRC2012_img_train.tar", mode="r:") as outer:
                for member in outer:
                    requested = train.pop(PurePosixPath(member.name).name, None)
                    if requested is None:
                        continue
                    if not member.isfile():
                        raise ValueError(f"Expected a class archive: {member.name}")
                    class_file = outer.extractfile(member)
                    if class_file is None:
                        raise ValueError(f"Cannot read class archive: {member.name}")
                    # Uncompressed nested tar files support seeking; no class tar is written to disk.
                    with class_file, tarfile.open(fileobj=class_file, mode="r:") as inner:
                        new, existing = extract_images(inner, requested, output_dir, found)
                    copied += new
                    skipped += existing
                    completed_classes += 1
                    if completed_classes == 1 or completed_classes % 10 == 0 or not train:
                        print(
                            f"Train classes: {completed_classes}/{total_classes}; "
                            f"images copied: {copied}; size-matched existing images: {skipped}",
                            flush=True,
                        )
                    if not train:
                        break
    
        if val:
            with tarfile.open(archive_dir / "ILSVRC2012_img_val.tar", mode="r:") as archive:
                new, existing = extract_images(archive, val, output_dir, found)
            copied += new
            skipped += existing
    
        missing = sorted(set(names) - found)
        if missing:
            raise ValueError(
                f"{len(missing)} requested images were not found in the archives: {missing[:10]}"
            )
        print(f"Complete: {len(found)} images; copied={copied}; size-matched existing={skipped}.")
        print(f"Output directory: {output_dir.resolve()}")
        return copied, skipped
    
    
    def main() -> None:
        data_dir = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--archive-dir", type=Path, default=data_dir / "imagenet_archives")
        parser.add_argument("--output-dir", type=Path, default=data_dir / "ImageNet")
        parser.add_argument(
            "--manifest", type=Path, default=data_dir / "transfer_lists" / "imagenet_required.txt"
        )
        args = parser.parse_args()
        names = load_manifest(args.manifest.expanduser())
        extract_subset(args.archive_dir.expanduser(), args.output_dir.expanduser(), names)
    
    
    if __name__ == "__main__":
        try:
            main()
        except (OSError, ValueError, tarfile.TarError) as error:
            print(f"Error: {error}", file=sys.stderr)
            raise SystemExit(1)
    ✓ • 66ms

## Activity

    $ git status --short
     M .gitignore
     M README.md
     M data/download_web_images.py
     M data/prepare_data.sh
    ?? Test.md
    ?? aPY/
    ?? clip_dataset.py
    ?? clip_inference.py
    ?? data/extract_imagenet_subset.py
    ?? data/from_web.tgz
    ?? data/from_web.tgz:Zone.Identifier
    ?? data/resources/OCL_annot_test.pkl
    ?? data/resources/OCL_annot_train.pkl
    ?? data/resources/OCL_annot_val.pkl
    ?? data/transfer_lists/
    ?? data/web_download_failures.json
    ?? docs/clip_inference.md
    ?? requirements-clip.txt
    ?? setup_clip_gpu.sh
    ?? tests/
    ✓ • 71ms

## Activity

    $ python - <<'PY'
        import importlib.util
        for name in ['requests','PIL']:
            print(name, importlib.util.find_spec(name) is not None)
        PY
    requests True
    PIL False
    ✓ • 189ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        from collections import Counter
        for p in [Path('/home/linfu/src/Test/ObjectConceptLearning/AGENTS.md'),Path('AGENTS.md')]:
            if p.is_file():
                print(p, p.read_text())
        paths=Path('transfer_lists/imagenet_required.txt').read_text().splitlines()
        print('images', len(paths))
        print('splits', dict(Counter(x.split('/')[0] for x in paths)))
        print('train_classes', len({x.split('/')[1] for x in paths if x.startswith('train/')}))
        print('output_exists', Path('ImageNet').exists())
        print('files', [p.name for p in Path('.').iterdir() if p.is_file()])
        PY
    images 7924
    splits {'train': 7702, 'val': 222}
    train_classes 190
    output_exists False
    files ['prepare_data.sh', 'from_web.tgz:Zone.Identifier', 'web_download_failures.json', 'download_web_images.py', 'from_web.tgz', 'extract_imagenet_subset.py']
    ✓ • 252ms

## Assistant

这里有个关键区别：现有清单只有文件名，tar 下载还需要每张图片的字节位置。首次运行必须读取归档头来建立位置索引；索引会缓存，后续可直接下载所需图片。我会并行处理训练类别和验证集索引，但首次建索引仍会有网络请求开销，不能保证立即完成。

## Activity

    $ curl -L --fail --silent --show-error --max-time 30 --range 0-511 --max-filesize 1024 --dump-header - --output /tmp/ocl-imagenet-val-header-20261023.bin https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_val.tar
    HTTP/1.1 206 Partial Content
    Date: Thu, 22 Oct 2026 16:14:04 GMT
    Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
    Last-Modified: Thu, 14 Jun 2012 17:39:50 GMT
    ETag: "192076000-4c2722fbfc580"
    Accept-Ranges: bytes
    Content-Length: 512
    Access-Control-Allow-Origin: *
    Content-Range: bytes 0-511/6744924160
    Content-Type: application/x-tar
    
    ✓ • 1.41s

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/download_imagenet_subset.py
    """Download selected original ImageNet images using cached tar offsets and HTTP Range."""
    
    from __future__ import annotations
    
    import argparse
    from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
    import io
    import json
    import os
    from pathlib import Path, PurePosixPath
    import re
    import sys
    import tarfile
    import tempfile
    import threading
    import time
    
    import requests
    from PIL import Image
    
    from extract_imagenet_subset import load_manifest
    
    
    BASE_URL = "https://image-net.org/data/ILSVRC/2012"
    PATTERNS = {
        "classes": re.compile(r"n\d{8}\.tar"),
        "train": re.compile(r"n\d{8}_\d+\.JPEG"),
        "val": re.compile(r"ILSVRC2012_val_\d{8}\.JPEG"),
    }
    
    
    def atomic_write(path: Path, content: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=path.parent, prefix=f".{path.name}.", suffix=".part", delete=False
            ) as handle:
                temporary = Path(handle.name)
                handle.write(content)
            os.replace(temporary, path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    
    
    class RangeClient:
        def __init__(self, timeout: float, retries: int) -> None:
            self.timeout = timeout
            self.retries = retries
            self.local = threading.local()
            self.stop = threading.Event()
            self.lock = threading.Lock()
            self.requests = 0
            self.bytes = 0
    
        def fetch(self, url: str, start: int, end: int, identity: dict | None = None) -> tuple[bytes, dict]:
            if start < 0 or end < start:
                raise ValueError(f"Invalid byte range: {start}-{end}")
            if not hasattr(self.local, "session"):
                self.local.session = requests.Session()
            headers = {"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"}
            if identity:
                if identity.get("etag") and not identity["etag"].startswith("W/"):
                    headers["If-Match"] = identity["etag"]
                elif identity.get("last_modified"):
                    headers["If-Unmodified-Since"] = identity["last_modified"]
            for attempt in range(self.retries + 1):
                if self.stop.is_set():
                    raise InterruptedError("Download stopped")
                try:
                    with self.lock:
                        self.requests += 1
                    with self.local.session.get(
                        url, headers=headers, stream=True, timeout=(self.timeout, self.timeout)
                    ) as response:
                        if response.status_code == 429 or response.status_code >= 500:
                            response.raise_for_status()
                        if response.status_code != 206:
                            raise ValueError(
                                f"Expected HTTP 206 for {url}, got {response.status_code}. "
                                "Refusing a response that could download the entire archive."
                            )
                        match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", response.headers.get("Content-Range", ""))
                        if not match or (int(match[1]), int(match[2])) != (start, end):
                            raise ValueError("The server returned an incorrect Content-Range.")
                        metadata = {
                            "url": url,
                            "size": int(match[3]),
                            "etag": response.headers.get("ETag"),
                            "last_modified": response.headers.get("Last-Modified"),
                        }
                        if end >= metadata["size"]:
                            raise ValueError("The range extends beyond the archive.")
                        if identity and metadata != identity:
                            raise ValueError("The remote archive changed; rerun to rebuild its cached indexes.")
                        if response.headers.get("Content-Encoding", "identity") != "identity":
                            raise ValueError("Encoded HTTP responses cannot be used for tar offsets.")
                        chunks = []
                        received = 0
                        for chunk in response.iter_content(chunk_size=64 * 1024):
                            if self.stop.is_set():
                                raise InterruptedError("Download stopped")
                            received += len(chunk)
                            with self.lock:
                                self.bytes += len(chunk)
                            if received > end - start + 1:
                                raise ValueError("The server sent more bytes than requested.")
                            chunks.append(chunk)
                        if received != end - start + 1:
                            raise requests.exceptions.ChunkedEncodingError("Incomplete range response")
                        return b"".join(chunks), metadata
                except requests.RequestException as error:
                    if attempt == self.retries:
                        raise RuntimeError(f"Range request failed after retries: {error}") from error
                    if self.stop.wait(min(2 ** attempt, 8)):
                        raise InterruptedError("Download stopped") from error
            raise RuntimeError("Unreachable retry state")
    
    
    class RemoteArchive:
        def __init__(self, client: RangeClient, url: str) -> None:
            self.client = client
            self.first_header, self.identity = client.fetch(url, 0, 511)
            if not self.identity["etag"] and not self.identity["last_modified"]:
                raise ValueError("The archive needs an ETag or Last-Modified value for reliable cache reuse.")
            self.size = self.identity["size"]
    
        def read(self, offset: int, size: int) -> bytes:
            if size <= 0 or offset < 0 or offset + size > self.size:
                raise ValueError(f"Invalid archive read: offset={offset}, size={size}")
            if offset == 0 and size == 512:
                return self.first_header
            return self.client.fetch(
                self.identity["url"], offset, offset + size - 1, self.identity
            )[0]
    
    
    def parse_header(block: bytes) -> tarfile.TarInfo:
        member = tarfile.TarInfo.frombuf(block, "utf-8", "strict")
        if member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE):
            raise ValueError(f"Unsupported tar header type for {member.name!r}: {member.type!r}")
        return member
    
    
    def find_header(source: RemoteArchive, start: int, end: int, kind: str) -> int | None:
        # Validation can be indexed in parallel: locate a checksum-valid JPEG header
        # after each aligned partition boundary, then follow the normal tar offsets.
        cursor = ((start + 511) // 512) * 512
        while cursor + 512 <= end:
            block = source.read(cursor, min(64 * 1024, end - cursor))
            for index in range(0, len(block) - 511, 512):
                candidate = block[index:index + 512]
                if not candidate.startswith(b"ILSVRC2012_val_"):
                    continue
                try:
                    member = parse_header(candidate)
                except (ValueError, tarfile.TarError, UnicodeError):
                    continue
                if member.isfile() and PATTERNS[kind].fullmatch(member.name) and member.size > 0:
                    return cursor + index
            cursor += len(block)
        return None
    
    
    def index_members(
        source: RemoteArchive,
        cache: Path,
        start: int,
        scan_end: int,
        data_end: int,
        kind: str,
        needed: set[str],
        discover_start: bool = False,
    ) -> dict:
        signature = {
            "version": 1, "source": source.identity, "start": start,
            "scan_end": scan_end, "data_end": data_end, "kind": kind,
        }
        state = {}
        if cache.is_file():
            state = json.loads(cache.read_text(encoding="utf-8"))
        if state.get("signature") != signature:
            state = {"signature": signature, "cursor": None if discover_start else start,
                     "complete": False, "members": {}}
        if needed.issubset(state["members"]) or state["complete"]:
            return state["members"]
        processed = 0
        last_saved = time.monotonic()
        try:
            if state["cursor"] is None:
                state["cursor"] = find_header(source, start, scan_end, kind)
                if state["cursor"] is None:
                    state["complete"] = True
                    return state["members"]
            while state["cursor"] + 512 <= scan_end:
                if source.client.stop.is_set():
                    raise InterruptedError("Indexing stopped")
                offset = state["cursor"]
                header = source.read(offset, 512)
                if header == bytes(512):
                    state["complete"] = True
                    break
                member = parse_header(header)
                name = PurePosixPath(member.name).name
                next_header = offset + 512 + ((member.size + 511) // 512) * 512
                if member.size < 0 or next_header > data_end:
                    raise ValueError(f"Tar member exceeds its archive: {member.name}")
                if member.isfile() and PATTERNS[kind].fullmatch(name):
                    entry = {"offset": offset + 512, "size": member.size}
                    if name in state["members"] and state["members"][name] != entry:
                        raise ValueError(f"Duplicate tar member name: {name}")
                    state["members"][name] = entry
                state["cursor"] = next_header
                processed += 1
                if needed.issubset(state["members"]):
                    break
                if processed % 128 == 0 or time.monotonic() - last_saved >= 15:
                    atomic_write(cache, json.dumps(state).encode("utf-8"))
                    last_saved = time.monotonic()
            if state["cursor"] is not None and state["cursor"] + 512 > scan_end:
                state["complete"] = True
        finally:
            atomic_write(cache, json.dumps(state).encode("utf-8"))
        return state["members"]
    
    
    def valid_image(path: Path, expected_size: int) -> bool:
        if not path.is_file() or path.stat().st_size != expected_size:
            return False
        try:
            with Image.open(path) as image:
                image.load()
            return True
        except (OSError, ValueError, Image.DecompressionBombError):
            return False
    
    
    def process_group(source, cache, start, end, data_end, kind, requested, args, discover=False):
        members = index_members(source, cache, start, end, data_end, kind, set(requested), discover)
        found = {}
        downloaded = existing = 0
        for name in sorted(set(requested).intersection(members)):
            relative = requested[name]
            entry = members[name]
            if not (0 < entry["size"] <= 128 * 1024 * 1024):
                raise ValueError(f"Unexpected image size for {relative}: {entry['size']}")
            found[relative] = entry["size"]
            if args.index_only:
                continue
            destination = args.output_dir / relative
            if valid_image(destination, entry["size"]):
                existing += 1
                continue
            content = source.read(entry["offset"], entry["size"])
            with Image.open(io.BytesIO(content)) as image:
                image.load()
            atomic_write(destination, content)
            downloaded += 1
        return found, downloaded, existing
    
    
    def run(args) -> int:
        names = load_manifest(args.manifest)
        if args.limit is not None:
            names = names[:args.limit]
        train = {}
        val = {}
        for name in names:
            parts = PurePosixPath(name).parts
            if parts[0] == "train":
                train.setdefault(parts[1] + ".tar", {})[parts[2]] = name
            else:
                val[parts[1]] = name
        client = RangeClient(args.timeout, args.retries)
        jobs = []
        if train:
            source = RemoteArchive(client, args.train_url)
            print(f"Indexing outer training tar for {len(train)} required classes...", flush=True)
            outer = index_members(source, args.index_dir / "train_outer.json", 0, source.size,
                                  source.size, "classes", set(train))
            missing_classes = sorted(set(train) - set(outer))
            if missing_classes:
                raise ValueError(f"Classes missing from training archive: {missing_classes}")
            for name, requested in sorted(train.items()):
                entry = outer[name]
                jobs.append((source, args.index_dir / "train" / f"{name}.json",
                             entry["offset"], entry["offset"] + entry["size"],
                             entry["offset"] + entry["size"], "train", requested, args, False))
        if val:
            source = RemoteArchive(client, args.val_url)
            chunk_size = args.val_chunk_mib * 1024 * 1024
            for start in range(0, source.size, chunk_size):
                end = min(start + chunk_size, source.size)
                jobs.append((source, args.index_dir / "val" / f"{start}.json", start, end,
                             source.size, "val", val, args, start != 0))
        found = {}
        downloaded = existing = completed = 0
        errors = []
        executor = ThreadPoolExecutor(max_workers=args.workers)
        pending = {executor.submit(process_group, *job) for job in jobs}
        last_progress = time.monotonic()
        try:
            while pending:
                done, pending = wait(pending, timeout=10, return_when=FIRST_COMPLETED)
                for future in done:
                    completed += 1
                    try:
                        images, new, old = future.result()
                        if set(images).intersection(found):
                            raise ValueError("The same image appeared in more than one archive partition.")
                        found.update(images)
                        downloaded += new
                        existing += old
                    except Exception as error:
                        errors.append(str(error))
                        print(f"Group failed; rerun will reuse saved progress: {error}", file=sys.stderr, flush=True)
                if done or time.monotonic() - last_progress >= 20:
                    print(f"Groups {completed}/{len(jobs)}; images {len(found)}/{len(names)}; "
                          f"HTTP requests {client.requests}; received {client.bytes / 1024**2:.1f} MiB", flush=True)
                    last_progress = time.monotonic()
        except BaseException:
            client.stop.set()
            raise
        finally:
            executor.shutdown(wait=True, cancel_futures=True)
        missing = sorted(set(names) - set(found))
        report = {
            "mode": "index_only" if args.index_only else "download",
            "requested_images": len(names), "completed_images": len(found),
            "downloaded_images": downloaded, "existing_images": existing,
            "selected_image_bytes": sum(found.values()), "http_requests": client.requests,
            "received_bytes": client.bytes, "missing_images": missing, "errors": errors,
        }
        atomic_write(args.index_dir / "last_run.json", json.dumps(report, indent=2).encode("utf-8"))
        print(f"Selected image bytes: {sum(found.values()) / 1024**3:.3f} GiB")
        print(f"Report: {args.index_dir / 'last_run.json'}")
        if missing or errors:
            print(f"Incomplete: {len(missing)} images; first missing paths: {missing[:10]}", file=sys.stderr)
            return 1
        action = "indexed" if args.index_only else "downloaded or verified"
        print(f"Complete: {len(names)} images {action}.")
        return 0
    
    
    def main() -> int:
        data = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--manifest", type=Path, default=data / "transfer_lists" / "imagenet_required.txt")
        parser.add_argument("--output-dir", type=Path, default=data / "ImageNet")
        parser.add_argument("--index-dir", type=Path, default=data / "imagenet_index")
        parser.add_argument("--workers", type=int, default=8)
        parser.add_argument("--timeout", type=float, default=30)
        parser.add_argument("--retries", type=int, default=4)
        parser.add_argument("--val-chunk-mib", type=int, default=64)
        parser.add_argument("--limit", type=int, help="Use only the first N manifest entries for a smoke test")
        parser.add_argument("--index-only", action="store_true", help="Build reusable offsets without downloading images")
        parser.add_argument("--train-url", default=f"{BASE_URL}/ILSVRC2012_img_train.tar")
        parser.add_argument("--val-url", default=f"{BASE_URL}/ILSVRC2012_img_val.tar")
        args = parser.parse_args()
        if not 1 <= args.workers <= 64 or args.timeout <= 0 or args.retries < 0 or args.val_chunk_mib < 1:
            parser.error("Use 1..64 workers, a positive timeout/chunk size, and non-negative retries.")
        if args.limit is not None and args.limit < 1:
            parser.error("--limit must be positive")
        for name in ("manifest", "output_dir", "index_dir"):
            setattr(args, name, getattr(args, name).expanduser().resolve())
        return run(args)
    
    
    if __name__ == "__main__":
        try:
            raise SystemExit(main())
        except KeyboardInterrupt:
            print("Interrupted. Rerun the same command to reuse cached indexes and complete images.", file=sys.stderr)
            raise SystemExit(130)
        except (OSError, ValueError, RuntimeError, tarfile.TarError) as error:
            print(f"Error: {error}", file=sys.stderr)
            raise SystemExit(1)

## Assistant

脚本已加入索引缓存、并行处理、失败重试和图片解码检查。它会拒绝服务器返回的整包响应，避免意外下载 154 GB。现在我在验证 tar 字节位置和断点重跑逻辑，随后会用官方文件下载少量真实图片做检查。

## Activity

    $ python - <<'PY'
        from pathlib import Path
        import tarfile
        for name, offset in [('/tmp/ocl-imagenet-check-egurnta3/train-prefix.bin',512),('/tmp/ocl-imagenet-val-header-20261023.bin',0)]:
            data=Path(name).read_bytes()[offset:offset+512]
            info=tarfile.TarInfo.frombuf(data,'utf-8','strict')
            print(name,info.name,info.size,info.type)
        PY
    /tmp/ocl-imagenet-check-egurnta3/train-prefix.bin n01440764_2708.JPEG 2160232 b'0'
    /tmp/ocl-imagenet-val-header-20261023.bin ILSVRC2012_val_00046108.JPEG 2794 b'0'
    ✓ • 322ms

## User

继续

## Assistant

当前版本的索引器有一个性能问题：如果逐个 tar 条目发 HTTP 请求，训练集会产生大量请求。我会改成按大块 Range 请求扫描 tar 头部，保留索引缓存和断点恢复；这样不会占用服务器磁盘，也避免逐条请求的严重性能损失。

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/download_imagenet_subset.py
    @@ -145,22 +145,2 @@
     
    -def find_header(source: RemoteArchive, start: int, end: int, kind: str) -> int | None:
    -    # Validation can be indexed in parallel: locate a checksum-valid JPEG header
    -    # after each aligned partition boundary, then follow the normal tar offsets.
    -    cursor = ((start + 511) // 512) * 512
    -    while cursor + 512 <= end:
    -        block = source.read(cursor, min(64 * 1024, end - cursor))
    -        for index in range(0, len(block) - 511, 512):
    -            candidate = block[index:index + 512]
    -            if not candidate.startswith(b"ILSVRC2012_val_"):
    -                continue
    -            try:
    -                member = parse_header(candidate)
    -            except (ValueError, tarfile.TarError, UnicodeError):
    -                continue
    -            if member.isfile() and PATTERNS[kind].fullmatch(member.name) and member.size > 0:
    -                return cursor + index
    -        cursor += len(block)
    -    return None
    -
    -
     def index_members(
    @@ -173,3 +153,3 @@
         needed: set[str],
    -    discover_start: bool = False,
    +    scan_chunk_size: int,
     ) -> dict:
    @@ -178,2 +158,3 @@
             "scan_end": scan_end, "data_end": data_end, "kind": kind,
    +        "scan_chunk_size": scan_chunk_size,
         }
    @@ -183,3 +164,3 @@
         if state.get("signature") != signature:
    -        state = {"signature": signature, "cursor": None if discover_start else start,
    +        state = {"signature": signature, "cursor": start,
                      "complete": False, "members": {}}
    @@ -190,7 +171,2 @@
         try:
    -        if state["cursor"] is None:
    -            state["cursor"] = find_header(source, start, scan_end, kind)
    -            if state["cursor"] is None:
    -                state["complete"] = True
    -                return state["members"]
             while state["cursor"] + 512 <= scan_end:
    @@ -199,19 +175,35 @@
                 offset = state["cursor"]
    -            header = source.read(offset, 512)
    -            if header == bytes(512):
    -                state["complete"] = True
    -                break
    -            member = parse_header(header)
    -            name = PurePosixPath(member.name).name
    -            next_header = offset + 512 + ((member.size + 511) // 512) * 512
    -            if member.size < 0 or next_header > data_end:
    -                raise ValueError(f"Tar member exceeds its archive: {member.name}")
    -            if member.isfile() and PATTERNS[kind].fullmatch(name):
    -                entry = {"offset": offset + 512, "size": member.size}
    -                if name in state["members"] and state["members"][name] != entry:
    -                    raise ValueError(f"Duplicate tar member name: {name}")
    -                state["members"][name] = entry
    -            state["cursor"] = next_header
    -            processed += 1
    -            if needed.issubset(state["members"]):
    +            block_end = min(scan_end, offset + scan_chunk_size)
    +            block = source.read(offset, block_end - offset)
    +            relative = 0
    +            while relative + 512 <= len(block):
    +                header = block[relative : relative + 512]
    +                absolute = offset + relative
    +                if header == bytes(512):
    +                    state["complete"] = True
    +                    state["cursor"] = scan_end
    +                    break
    +                member = parse_header(header)
    +                name = PurePosixPath(member.name).name
    +                next_header = absolute + 512 + ((member.size + 511) // 512) * 512
    +                if member.size < 0 or next_header > data_end:
    +                    raise ValueError(f"Tar member exceeds its archive: {member.name}")
    +                if member.isfile() and PATTERNS[kind].fullmatch(name):
    +                    entry = {"offset": absolute + 512, "size": member.size}
    +                    if name in state["members"] and state["members"][name] != entry:
    +                        raise ValueError(f"Duplicate tar member name: {name}")
    +                    state["members"][name] = entry
    +                processed += 1
    +                # If the next header is outside this block, skip the unneeded
    +                # image payload and request the next block at that exact header.
    +                if next_header + 512 > block_end:
    +                    state["cursor"] = next_header
    +                    break
    +                relative = next_header - offset
    +                state["cursor"] = next_header
    +                if needed.issubset(state["members"]):
    +                    break
    +            else:
    +                state["cursor"] = block_end
    +            if state["complete"] or needed.issubset(state["members"]):
                     break
    @@ -220,3 +212,3 @@
                     last_saved = time.monotonic()
    -        if state["cursor"] is not None and state["cursor"] + 512 > scan_end:
    +        if state["cursor"] + 512 > scan_end:
                 state["complete"] = True
    @@ -238,4 +230,6 @@
     
    -def process_group(source, cache, start, end, data_end, kind, requested, args, discover=False):
    -    members = index_members(source, cache, start, end, data_end, kind, set(requested), discover)
    +def process_group(source, cache, start, end, data_end, kind, requested, args, scan_chunk_size):
    +    members = index_members(
    +        source, cache, start, end, data_end, kind, set(requested), scan_chunk_size
    +    )
         found = {}
    @@ -279,4 +273,12 @@
             print(f"Indexing outer training tar for {len(train)} required classes...", flush=True)
    -        outer = index_members(source, args.index_dir / "train_outer.json", 0, source.size,
    -                              source.size, "classes", set(train))
    +        outer = index_members(
    +            source,
    +            args.index_dir / "train_outer.json",
    +            0,
    +            source.size,
    +            source.size,
    +            "classes",
    +            set(train),
    +            512,
    +        )
             missing_classes = sorted(set(train) - set(outer))
    @@ -288,10 +290,8 @@
                              entry["offset"], entry["offset"] + entry["size"],
    -                         entry["offset"] + entry["size"], "train", requested, args, False))
    +                         entry["offset"] + entry["size"], "train", requested, args,
    +                         args.train_chunk_mib * 1024 * 1024))
         if val:
             source = RemoteArchive(client, args.val_url)
    -        chunk_size = args.val_chunk_mib * 1024 * 1024
    -        for start in range(0, source.size, chunk_size):
    -            end = min(start + chunk_size, source.size)
    -            jobs.append((source, args.index_dir / "val" / f"{start}.json", start, end,
    -                         source.size, "val", val, args, start != 0))
    +        jobs.append((source, args.index_dir / "val.json", 0, source.size, source.size,
    +                     "val", val, args, args.val_chunk_mib * 1024 * 1024))
         found = {}
    @@ -354,2 +354,3 @@
         parser.add_argument("--retries", type=int, default=4)
    +    parser.add_argument("--train-chunk-mib", type=int, default=8)
         parser.add_argument("--val-chunk-mib", type=int, default=64)
    @@ -360,3 +361,9 @@
         args = parser.parse_args()
    -    if not 1 <= args.workers <= 64 or args.timeout <= 0 or args.retries < 0 or args.val_chunk_mib < 1:
    +    if (
    +        not 1 <= args.workers <= 64
    +        or args.timeout <= 0
    +        or args.retries < 0
    +        or args.train_chunk_mib < 1
    +        or args.val_chunk_mib < 1
    +    ):
             parser.error("Use 1..64 workers, a positive timeout/chunk size, and non-negative retries.")

## Activity

    $ sed -n '125,260p' download_imagenet_subset.py
            if not self.identity["etag"] and not self.identity["last_modified"]:
                raise ValueError("The archive needs an ETag or Last-Modified value for reliable cache reuse.")
            self.size = self.identity["size"]
    
        def read(self, offset: int, size: int) -> bytes:
            if size <= 0 or offset < 0 or offset + size > self.size:
                raise ValueError(f"Invalid archive read: offset={offset}, size={size}")
            if offset == 0 and size == 512:
                return self.first_header
            return self.client.fetch(
                self.identity["url"], offset, offset + size - 1, self.identity
            )[0]
    
    
    def parse_header(block: bytes) -> tarfile.TarInfo:
        member = tarfile.TarInfo.frombuf(block, "utf-8", "strict")
        if member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE):
            raise ValueError(f"Unsupported tar header type for {member.name!r}: {member.type!r}")
        return member
    
    
    def index_members(
        source: RemoteArchive,
        cache: Path,
        start: int,
        scan_end: int,
        data_end: int,
        kind: str,
        needed: set[str],
        scan_chunk_size: int,
    ) -> dict:
        signature = {
            "version": 1, "source": source.identity, "start": start,
            "scan_end": scan_end, "data_end": data_end, "kind": kind,
            "scan_chunk_size": scan_chunk_size,
        }
        state = {}
        if cache.is_file():
            state = json.loads(cache.read_text(encoding="utf-8"))
        if state.get("signature") != signature:
            state = {"signature": signature, "cursor": start,
                     "complete": False, "members": {}}
        if needed.issubset(state["members"]) or state["complete"]:
            return state["members"]
        processed = 0
        last_saved = time.monotonic()
        try:
            while state["cursor"] + 512 <= scan_end:
                if source.client.stop.is_set():
                    raise InterruptedError("Indexing stopped")
                offset = state["cursor"]
                block_end = min(scan_end, offset + scan_chunk_size)
                block = source.read(offset, block_end - offset)
                relative = 0
                while relative + 512 <= len(block):
                    header = block[relative : relative + 512]
                    absolute = offset + relative
                    if header == bytes(512):
                        state["complete"] = True
                        state["cursor"] = scan_end
                        break
                    member = parse_header(header)
                    name = PurePosixPath(member.name).name
                    next_header = absolute + 512 + ((member.size + 511) // 512) * 512
                    if member.size < 0 or next_header > data_end:
                        raise ValueError(f"Tar member exceeds its archive: {member.name}")
                    if member.isfile() and PATTERNS[kind].fullmatch(name):
                        entry = {"offset": absolute + 512, "size": member.size}
                        if name in state["members"] and state["members"][name] != entry:
                            raise ValueError(f"Duplicate tar member name: {name}")
                        state["members"][name] = entry
                    processed += 1
                    # If the next header is outside this block, skip the unneeded
                    # image payload and request the next block at that exact header.
                    if next_header + 512 > block_end:
                        state["cursor"] = next_header
                        break
                    relative = next_header - offset
                    state["cursor"] = next_header
                    if needed.issubset(state["members"]):
                        break
                else:
                    state["cursor"] = block_end
                if state["complete"] or needed.issubset(state["members"]):
                    break
                if processed % 128 == 0 or time.monotonic() - last_saved >= 15:
                    atomic_write(cache, json.dumps(state).encode("utf-8"))
                    last_saved = time.monotonic()
            if state["cursor"] + 512 > scan_end:
                state["complete"] = True
        finally:
            atomic_write(cache, json.dumps(state).encode("utf-8"))
        return state["members"]
    
    
    def valid_image(path: Path, expected_size: int) -> bool:
        if not path.is_file() or path.stat().st_size != expected_size:
            return False
        try:
            with Image.open(path) as image:
                image.load()
            return True
        except (OSError, ValueError, Image.DecompressionBombError):
            return False
    
    
    def process_group(source, cache, start, end, data_end, kind, requested, args, scan_chunk_size):
        members = index_members(
            source, cache, start, end, data_end, kind, set(requested), scan_chunk_size
        )
        found = {}
        downloaded = existing = 0
        for name in sorted(set(requested).intersection(members)):
            relative = requested[name]
            entry = members[name]
            if not (0 < entry["size"] <= 128 * 1024 * 1024):
                raise ValueError(f"Unexpected image size for {relative}: {entry['size']}")
            found[relative] = entry["size"]
            if args.index_only:
                continue
            destination = args.output_dir / relative
            if valid_image(destination, entry["size"]):
                existing += 1
                continue
            content = source.read(entry["offset"], entry["size"])
            with Image.open(io.BytesIO(content)) as image:
                image.load()
            atomic_write(destination, content)
            downloaded += 1
        return found, downloaded, existing
    
    
    def run(args) -> int:
        names = load_manifest(args.manifest)
        if args.limit is not None:
            names = names[:args.limit]
    ✓ • 82ms

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python download_imagenet_subset.py --help
    usage: download_imagenet_subset.py [-h] [--manifest MANIFEST]
                                       [--output-dir OUTPUT_DIR]
                                       [--index-dir INDEX_DIR] [--workers WORKERS]
                                       [--timeout TIMEOUT] [--retries RETRIES]
                                       [--train-chunk-mib TRAIN_CHUNK_MIB]
                                       [--val-chunk-mib VAL_CHUNK_MIB]
                                       [--limit LIMIT] [--index-only]
                                       [--train-url TRAIN_URL] [--val-url VAL_URL]
    
    Download selected original ImageNet images using cached tar offsets and HTTP
    Range.
    
    options:
      -h, --help            show this help message and exit
      --manifest MANIFEST
      --output-dir OUTPUT_DIR
      --index-dir INDEX_DIR
      --workers WORKERS
      --timeout TIMEOUT
      --retries RETRIES
      --train-chunk-mib TRAIN_CHUNK_MIB
      --val-chunk-mib VAL_CHUNK_MIB
      --limit LIMIT         Use only the first N manifest entries for a smoke test
      --index-only          Build reusable offsets without downloading images
      --train-url TRAIN_URL
      --val-url VAL_URL
    ✓ • 650ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/download_imagenet_subset.py
    @@ -1,2 +1,6 @@
    -"""Download selected original ImageNet images using cached tar offsets and HTTP Range."""
    +"""Download selected ImageNet images using cached tar offsets and HTTP Range.
    +
    +The first index scan reads ahead to reduce request overhead. These temporary
    +blocks can contain unselected images, but are never written to disk.
    +"""
     
    @@ -158,3 +162,2 @@
             "scan_end": scan_end, "data_end": data_end, "kind": kind,
    -        "scan_chunk_size": scan_chunk_size,
         }
    @@ -211,2 +214,5 @@
                     atomic_write(cache, json.dumps(state).encode("utf-8"))
    +                if kind == "classes":
    +                    print(f"Outer index: {len(state['members'])} classes cached; "
    +                          f"HTTP requests: {source.client.requests}", flush=True)
                     last_saved = time.monotonic()
    @@ -286,2 +292,5 @@
                 raise ValueError(f"Classes missing from training archive: {missing_classes}")
    +        class_bytes = sum(outer[name]["size"] for name in train)
    +        print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB. "
    +              "Read-ahead indexing can transfer much of this data without storing it.", flush=True)
             for name, requested in sorted(train.items()):
    @@ -291,3 +300,3 @@
                              entry["offset"] + entry["size"], "train", requested, args,
    -                         args.train_chunk_mib * 1024 * 1024))
    +                         512 if args.header_only else args.train_chunk_mib * 1024 * 1024))
         if val:
    @@ -295,3 +304,4 @@
             jobs.append((source, args.index_dir / "val.json", 0, source.size, source.size,
    -                     "val", val, args, args.val_chunk_mib * 1024 * 1024))
    +                     "val", val, args,
    +                     512 if args.header_only else args.val_chunk_mib * 1024 * 1024))
         found = {}
    @@ -358,2 +368,6 @@
         parser.add_argument("--index-only", action="store_true", help="Build reusable offsets without downloading images")
    +    parser.add_argument(
    +        "--header-only", action="store_true",
    +        help="Index with 512-byte header reads; less bandwidth, many more HTTP requests",
    +    )
         parser.add_argument("--train-url", default=f"{BASE_URL}/ILSVRC2012_img_train.tar")

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python - <<'PY'
        from contextlib import redirect_stdout, redirect_stderr
        from pathlib import Path
        from types import SimpleNamespace
        from unittest.mock import patch
        import hashlib
        import io
        import json
        import tarfile
        import tempfile
        
        import download_imagenet_subset as module
        from PIL import Image
        
        def jpeg(color):
            buffer = io.BytesIO()
            Image.new('RGB', (19, 23), color).save(buffer, format='JPEG')
            return buffer.getvalue()
        
        def make_tar(entries):
            buffer = io.BytesIO()
            with tarfile.open(fileobj=buffer, mode='w') as archive:
                for name, body in entries:
                    member = tarfile.TarInfo(name)
                    member.size = len(body)
                    archive.addfile(member, io.BytesIO(body))
            return buffer.getvalue()
        
        red, blue, green = jpeg('red'), jpeg('blue'), jpeg('green')
        first = make_tar([('n00000001_1.JPEG', red + bytes(17000)), ('n00000001_2.JPEG', blue), ('n00000001_3.JPEG', green)])
        second = make_tar([('n00000003_1.JPEG', green), ('n00000003_2.JPEG', red)])
        train = make_tar([('n00000000.tar', make_tar([('n00000000_1.JPEG', blue)])), ('n00000001.tar', first), ('n00000003.tar', second)])
        val = make_tar([
            ('ILSVRC2012_val_00000001.JPEG', red),
            ('ILSVRC2012_val_00000002.JPEG', blue + bytes(1300000)),
            ('ILSVRC2012_val_00000003.JPEG', green),
            ('ILSVRC2012_val_00000004.JPEG', red + bytes(1100000)),
            ('ILSVRC2012_val_00000005.JPEG', blue),
        ])
        fixtures = {'train': train, 'val': val}
        clients = []
        class FakeClient(module.RangeClient):
            def __init__(self, timeout, retries):
                super().__init__(timeout, retries)
                clients.append(self)
                self.ranges = []
            def fetch(self, url, start, end, identity=None):
                body = fixtures[url]
                metadata = {'url':url, 'size':len(body), 'etag':hashlib.sha256(body).hexdigest(), 'last_modified':'fixed'}
                assert 0 <= start <= end < len(body)
                assert identity is None or identity == metadata
                with self.lock:
                    self.requests += 1
                    self.bytes += end-start+1
                    self.ranges.append((url, start, end))
                return body[start:end+1], metadata
        
        with tempfile.TemporaryDirectory(prefix='ocl-range-fixtures-') as directory:
            root = Path(directory)
            names = ['train/n00000001/n00000001_2.JPEG', 'train/n00000003/n00000003_1.JPEG', 'val/ILSVRC2012_val_00000001.JPEG', 'val/ILSVRC2012_val_00000003.JPEG', 'val/ILSVRC2012_val_00000005.JPEG']
            manifest = root/'manifest.txt'
            manifest.write_text('\n'.join(names)+'\n')
            args = SimpleNamespace(manifest=manifest, limit=None, timeout=3, retries=0, train_url='train', val_url='val', index_dir=root/'indexes', output_dir=root/'images', workers=3, train_chunk_mib=1, val_chunk_mib=1, index_only=False, header_only=False)
            with patch.object(module, 'RangeClient', FakeClient), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                assert module.run(args) == 0
                output = args.output_dir
                assert {str(p.relative_to(output)) for p in output.rglob('*.JPEG')} == set(names)
                assert [p.read_bytes() for p in [output/n for n in names]] == [blue, green, red, green, blue]
                assert not list(output.rglob('*.tar'))
                assert module.run(args) == 0
                report = json.loads((args.index_dir/'last_run.json').read_text())
                assert (report['downloaded_images'], report['existing_images']) == (0, 5)
                assert clients[-1].requests == 2, clients[-1].ranges
                target = output/names[0]
                target.write_bytes(bytes(len(blue)))
                assert module.run(args) == 0
                assert target.read_bytes() == blue
                assert clients[-1].requests == 3
                args.output_dir = root/'index-only-images'
                args.index_only = True
                assert module.run(args) == 0
                assert not args.output_dir.exists()
                args.index_only = False
                args.output_dir = output
                args.header_only = True
                assert module.run(args) == 0
                assert clients[-1].requests == 2, 'Changing scan mode must reuse indexes'
                args.index_dir = root/'headers-only'
                args.output_dir = root/'headers-only-images'
                assert module.run(args) == 0
                assert clients[-1].bytes < 10000, clients[-1].bytes
                manifest.write_text('train/n00000001/n00000001_999.JPEG\n')
                assert module.run(args) == 1
                assert json.loads((args.index_dir/'last_run.json').read_text())['missing_images'] == ['train/n00000001/n00000001_999.JPEG']
            # A deliberately interrupted index resumes at the next unprocessed header.
            client = FakeClient(3,0)
            source = module.RemoteArchive(client,'train')
            cache = root/'interrupted-index.json'
            original_read = source.read
            calls = [0]
            def interrupted(offset, size):
                calls[0] += 1
                if calls[0] == 2:
                    raise OSError('simulated disconnection')
                return original_read(offset,size)
            source.read = interrupted
            try:
                module.index_members(source,cache,0,len(train),len(train),'classes',{'n00000003.tar'},512)
            except OSError:
                pass
            else:
                raise AssertionError('Expected disconnection')
            saved = json.loads(cache.read_text())
            assert saved['cursor'] > 0 and 'n00000000.tar' in saved['members']
            source.read = original_read
            indexed = module.index_members(source,cache,0,len(train),len(train),'classes',{'n00000003.tar'},4096)
            assert 'n00000003.tar' in indexed
        
        # Reject full-archive and mismatched range responses before consuming their bodies.
        class Response:
            def __init__(self,status,headers,body):
                self.status_code=status
                self.headers=headers
                self.body=body
                self.consumed=False
            def __enter__(self): return self
            def __exit__(self,*args): pass
            def iter_content(self,chunk_size):
                self.consumed=True
                yield self.body
        class Session:
            def __init__(self,response): self.response=response
            def get(self,*args,**kwargs): return self.response
        for response in [Response(200,{},b'whole archive'),Response(206,{'Content-Range':'bytes 1-4/8'},b'abcd')]:
            client=module.RangeClient(3,0)
            client.local.session=Session(response)
            try: client.fetch('test',0,3)
            except ValueError: pass
            else: raise AssertionError('Invalid HTTP response accepted')
            assert not response.consumed
        response=Response(206,{'Content-Range':'bytes 0-3/8','ETag':'stable'},b'abcd')
        client=module.RangeClient(3,0)
        client.local.session=Session(response)
        assert client.fetch('test',0,3)[0] == b'abcd'
        print('PASS: nested offsets, chunk boundaries, selected bytes, reusable indexes, header-only mode, corrupt-image repair, missing-image reporting, checkpoint recovery, HTTP 200 refusal, Content-Range checks.')
        PY
    PASS: nested offsets, chunk boundaries, selected bytes, reusable indexes, header-only mode, corrupt-image repair, missing-image reporting, checkpoint recovery, HTTP 200 refusal, Content-Range checks.
    ✓ • 1.08s

## Activity

    $ python - <<'PY'
        from pathlib import Path
        import tempfile
        import tarfile
        root = Path(tempfile.mkdtemp(prefix='ocl-range-live-'))
        train = tarfile.TarInfo.frombuf(Path('/tmp/ocl-imagenet-check-egurnta3/train-prefix.bin').read_bytes()[512:1024], 'utf-8', 'strict')
        val = tarfile.TarInfo.frombuf(Path('/tmp/ocl-imagenet-val-header-20261023.bin').read_bytes(), 'utf-8', 'strict')
        manifest = root/'manifest.txt'
        manifest.write_text(f'train/n01440764/{train.name}\nval/{val.name}\n')
        print(root)
        print(manifest.read_text())
        PY
    /tmp/ocl-range-live-2dnbvy9q
    train/n01440764/n01440764_2708.JPEG
    val/ILSVRC2012_val_00046108.JPEG
    
    ✓ • 351ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B download_imagenet_subset.py --manifest /tmp/ocl-range-live-2dnbvy9q/manifest.txt --output-dir /tmp/ocl-range-live-2dnbvy9q/images --index-dir /tmp/ocl-range-live-2dnbvy9q/index --workers 2 --train-chunk-mib 1 --val-chunk-mib 1 --timeout 20 --retries 1
    Indexing outer training tar for 1 required classes...
    Required training class archives total 0.15 GiB. Read-ahead indexing can transfer much of this data without storing it.
    Groups 1/2; images 1/2; HTTP requests 6; received 2.5 MiB
    Groups 2/2; images 2/2; HTTP requests 6; received 4.1 MiB
    Selected image bytes: 0.002 GiB
    Report: /tmp/ocl-range-live-2dnbvy9q/index/last_run.json
    Complete: 2 images downloaded or verified.
    ✓ • 6.06s

## Assistant

两张真实 ImageNet 图片的分段下载验证已成功：训练集嵌套 tar 和验证集 tar 都能通过 Range 定位并下载，约 4.1 MiB 网络读取；脚本没有保存完整压缩包。接下来我会做最终语法、回归测试，并给你服务器上可直接执行的命令。

## Activity

    $ sed -n '1,80p' download_imagenet_subset.py && sed -n '350,520p' download_imagenet_subset.py
    """Download selected ImageNet images using cached tar offsets and HTTP Range.
    
    The first index scan reads ahead to reduce request overhead. These temporary
    blocks can contain unselected images, but are never written to disk.
    """
    
    from __future__ import annotations
    
    import argparse
    from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
    import io
    import json
    import os
    from pathlib import Path, PurePosixPath
    import re
    import sys
    import tarfile
    import tempfile
    import threading
    import time
    
    import requests
    from PIL import Image
    
    from extract_imagenet_subset import load_manifest
    
    
    BASE_URL = "https://image-net.org/data/ILSVRC/2012"
    PATTERNS = {
        "classes": re.compile(r"n\d{8}\.tar"),
        "train": re.compile(r"n\d{8}_\d+\.JPEG"),
        "val": re.compile(r"ILSVRC2012_val_\d{8}\.JPEG"),
    }
    
    
    def atomic_write(path: Path, content: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=path.parent, prefix=f".{path.name}.", suffix=".part", delete=False
            ) as handle:
                temporary = Path(handle.name)
                handle.write(content)
            os.replace(temporary, path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    
    
    class RangeClient:
        def __init__(self, timeout: float, retries: int) -> None:
            self.timeout = timeout
            self.retries = retries
            self.local = threading.local()
            self.stop = threading.Event()
            self.lock = threading.Lock()
            self.requests = 0
            self.bytes = 0
    
        def fetch(self, url: str, start: int, end: int, identity: dict | None = None) -> tuple[bytes, dict]:
            if start < 0 or end < start:
                raise ValueError(f"Invalid byte range: {start}-{end}")
            if not hasattr(self.local, "session"):
                self.local.session = requests.Session()
            headers = {"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"}
            if identity:
                if identity.get("etag") and not identity["etag"].startswith("W/"):
                    headers["If-Match"] = identity["etag"]
                elif identity.get("last_modified"):
                    headers["If-Unmodified-Since"] = identity["last_modified"]
            for attempt in range(self.retries + 1):
                if self.stop.is_set():
                    raise InterruptedError("Download stopped")
                try:
                    with self.lock:
                        self.requests += 1
                    with self.local.session.get(
                        url, headers=headers, stream=True, timeout=(self.timeout, self.timeout)
                    ) as response:
            return 1
        action = "indexed" if args.index_only else "downloaded or verified"
        print(f"Complete: {len(names)} images {action}.")
        return 0
    
    
    def main() -> int:
        data = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--manifest", type=Path, default=data / "transfer_lists" / "imagenet_required.txt")
        parser.add_argument("--output-dir", type=Path, default=data / "ImageNet")
        parser.add_argument("--index-dir", type=Path, default=data / "imagenet_index")
        parser.add_argument("--workers", type=int, default=8)
        parser.add_argument("--timeout", type=float, default=30)
        parser.add_argument("--retries", type=int, default=4)
        parser.add_argument("--train-chunk-mib", type=int, default=8)
        parser.add_argument("--val-chunk-mib", type=int, default=64)
        parser.add_argument("--limit", type=int, help="Use only the first N manifest entries for a smoke test")
        parser.add_argument("--index-only", action="store_true", help="Build reusable offsets without downloading images")
        parser.add_argument(
            "--header-only", action="store_true",
            help="Index with 512-byte header reads; less bandwidth, many more HTTP requests",
        )
        parser.add_argument("--train-url", default=f"{BASE_URL}/ILSVRC2012_img_train.tar")
        parser.add_argument("--val-url", default=f"{BASE_URL}/ILSVRC2012_img_val.tar")
        args = parser.parse_args()
        if (
            not 1 <= args.workers <= 64
            or args.timeout <= 0
            or args.retries < 0
            or args.train_chunk_mib < 1
            or args.val_chunk_mib < 1
        ):
            parser.error("Use 1..64 workers, a positive timeout/chunk size, and non-negative retries.")
        if args.limit is not None and args.limit < 1:
            parser.error("--limit must be positive")
        for name in ("manifest", "output_dir", "index_dir"):
            setattr(args, name, getattr(args, name).expanduser().resolve())
        return run(args)
    
    
    if __name__ == "__main__":
        try:
            raise SystemExit(main())
        except KeyboardInterrupt:
            print("Interrupted. Rerun the same command to reuse cached indexes and complete images.", file=sys.stderr)
            raise SystemExit(130)
        except (OSError, ValueError, RuntimeError, tarfile.TarError) as error:
            print(f"Error: {error}", file=sys.stderr)
            raise SystemExit(1)
    ✓ • 39ms

## Activity

    $ git diff --stat -- data/download_imagenet_subset.py data/extract_imagenet_subset.py && git status --short data/download_imagenet_subset.py data/extract_imagenet_subset.py
    ?? data/download_imagenet_subset.py
    ?? data/extract_imagenet_subset.py
    ✓ • 87ms

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 python -m py_compile download_imagenet_subset.py extract_imagenet_subset.py
    ✓ • 198ms

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m unittest discover -s ../tests -p 'test_clip_category_selection.py' -v
    test_clip_category_selection (unittest.loader._FailedTest.test_clip_category_selection) ... ERROR
    
    ======================================================================
    ERROR: test_clip_category_selection (unittest.loader._FailedTest.test_clip_category_selection)
    ----------------------------------------------------------------------
    ImportError: Failed to import test module: test_clip_category_selection
    Traceback (most recent call last):
      File "/usr/lib/python3.12/unittest/loader.py", line 394, in _find_test_path
        module = self._get_module_from_name(name)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/usr/lib/python3.12/unittest/loader.py", line 337, in _get_module_from_name
        __import__(name)
      File "/home/linfu/src/Test/ObjectConceptLearning/tests/test_clip_category_selection.py", line 12, in <module>
        from clip_dataset import OCLClipDataset, load_dataset
    ModuleNotFoundError: No module named 'clip_dataset'
    
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    FAILED (errors=1)
    ✗ (1) • 3.91s

## Activity

    $ nl -ba download_imagenet_subset.py
         1    """Download selected ImageNet images using cached tar offsets and HTTP Range.
         2
         3    The first index scan reads ahead to reduce request overhead. These temporary
         4    blocks can contain unselected images, but are never written to disk.
         5    """
         6
         7    from __future__ import annotations
         8
         9    import argparse
        10    from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
        11    import io
        12    import json
        13    import os
        14    from pathlib import Path, PurePosixPath
        15    import re
        16    import sys
        17    import tarfile
        18    import tempfile
        19    import threading
        20    import time
        21
        22    import requests
        23    from PIL import Image
        24
        25    from extract_imagenet_subset import load_manifest
        26
        27
        28    BASE_URL = "https://image-net.org/data/ILSVRC/2012"
        29    PATTERNS = {
        30        "classes": re.compile(r"n\d{8}\.tar"),
        31        "train": re.compile(r"n\d{8}_\d+\.JPEG"),
        32        "val": re.compile(r"ILSVRC2012_val_\d{8}\.JPEG"),
        33    }
        34
        35
        36    def atomic_write(path: Path, content: bytes) -> None:
        37        path.parent.mkdir(parents=True, exist_ok=True)
        38        temporary = None
        39        try:
        40            with tempfile.NamedTemporaryFile(
        41                dir=path.parent, prefix=f".{path.name}.", suffix=".part", delete=False
        42            ) as handle:
        43                temporary = Path(handle.name)
        44                handle.write(content)
        45            os.replace(temporary, path)
        46        finally:
        47            if temporary is not None:
        48                temporary.unlink(missing_ok=True)
        49
        50
        51    class RangeClient:
        52        def __init__(self, timeout: float, retries: int) -> None:
        53            self.timeout = timeout
        54            self.retries = retries
        55            self.local = threading.local()
        56            self.stop = threading.Event()
        57            self.lock = threading.Lock()
        58            self.requests = 0
        59            self.bytes = 0
        60
        61        def fetch(self, url: str, start: int, end: int, identity: dict | None = None) -> tuple[bytes, dict]:
        62            if start < 0 or end < start:
        63                raise ValueError(f"Invalid byte range: {start}-{end}")
        64            if not hasattr(self.local, "session"):
        65                self.local.session = requests.Session()
        66            headers = {"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"}
        67            if identity:
        68                if identity.get("etag") and not identity["etag"].startswith("W/"):
        69                    headers["If-Match"] = identity["etag"]
        70                elif identity.get("last_modified"):
        71                    headers["If-Unmodified-Since"] = identity["last_modified"]
        72            for attempt in range(self.retries + 1):
        73                if self.stop.is_set():
        74                    raise InterruptedError("Download stopped")
        75                try:
        76                    with self.lock:
        77                        self.requests += 1
        78                    with self.local.session.get(
        79                        url, headers=headers, stream=True, timeout=(self.timeout, self.timeout)
        80                    ) as response:
        81                        if response.status_code == 429 or response.status_code >= 500:
        82                            response.raise_for_status()
        83                        if response.status_code != 206:
        84                            raise ValueError(
        85                                f"Expected HTTP 206 for {url}, got {response.status_code}. "
        86                                "Refusing a response that could download the entire archive."
        87                            )
        88                        match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", response.headers.get("Content-Range", ""))
        89                        if not match or (int(match[1]), int(match[2])) != (start, end):
        90                            raise ValueError("The server returned an incorrect Content-Range.")
        91                        metadata = {
        92                            "url": url,
        93                            "size": int(match[3]),
        94                            "etag": response.headers.get("ETag"),
        95                            "last_modified": response.headers.get("Last-Modified"),
        96                        }
        97                        if end >= metadata["size"]:
        98                            raise ValueError("The range extends beyond the archive.")
        99                        if identity and metadata != identity:
       100                            raise ValueError("The remote archive changed; rerun to rebuild its cached indexes.")
       101                        if response.headers.get("Content-Encoding", "identity") != "identity":
       102                            raise ValueError("Encoded HTTP responses cannot be used for tar offsets.")
       103                        chunks = []
       104                        received = 0
       105                        for chunk in response.iter_content(chunk_size=64 * 1024):
       106                            if self.stop.is_set():
       107                                raise InterruptedError("Download stopped")
       108                            received += len(chunk)
       109                            with self.lock:
       110                                self.bytes += len(chunk)
       111                            if received > end - start + 1:
       112                                raise ValueError("The server sent more bytes than requested.")
       113                            chunks.append(chunk)
       114                        if received != end - start + 1:
       115                            raise requests.exceptions.ChunkedEncodingError("Incomplete range response")
       116                        return b"".join(chunks), metadata
       117                except requests.RequestException as error:
       118                    if attempt == self.retries:
       119                        raise RuntimeError(f"Range request failed after retries: {error}") from error
       120                    if self.stop.wait(min(2 ** attempt, 8)):
       121                        raise InterruptedError("Download stopped") from error
       122            raise RuntimeError("Unreachable retry state")
       123
       124
       125    class RemoteArchive:
       126        def __init__(self, client: RangeClient, url: str) -> None:
       127            self.client = client
       128            self.first_header, self.identity = client.fetch(url, 0, 511)
       129            if not self.identity["etag"] and not self.identity["last_modified"]:
       130                raise ValueError("The archive needs an ETag or Last-Modified value for reliable cache reuse.")
       131            self.size = self.identity["size"]
       132
       133        def read(self, offset: int, size: int) -> bytes:
       134            if size <= 0 or offset < 0 or offset + size > self.size:
       135                raise ValueError(f"Invalid archive read: offset={offset}, size={size}")
       136            if offset == 0 and size == 512:
       137                return self.first_header
       138            return self.client.fetch(
       139                self.identity["url"], offset, offset + size - 1, self.identity
       140            )[0]
       141
       142
       143    def parse_header(block: bytes) -> tarfile.TarInfo:
       144        member = tarfile.TarInfo.frombuf(block, "utf-8", "strict")
       145        if member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE):
       146            raise ValueError(f"Unsupported tar header type for {member.name!r}: {member.type!r}")
       147        return member
       148
       149
       150    def index_members(
       151        source: RemoteArchive,
       152        cache: Path,
       153        start: int,
       154        scan_end: int,
       155        data_end: int,
       156        kind: str,
       157        needed: set[str],
       158        scan_chunk_size: int,
       159    ) -> dict:
       160        signature = {
       161            "version": 1, "source": source.identity, "start": start,
       162            "scan_end": scan_end, "data_end": data_end, "kind": kind,
       163        }
       164        state = {}
       165        if cache.is_file():
       166            state = json.loads(cache.read_text(encoding="utf-8"))
       167        if state.get("signature") != signature:
       168            state = {"signature": signature, "cursor": start,
       169                     "complete": False, "members": {}}
       170        if needed.issubset(state["members"]) or state["complete"]:
       171            return state["members"]
       172        processed = 0
       173        last_saved = time.monotonic()
       174        try:
       175            while state["cursor"] + 512 <= scan_end:
       176                if source.client.stop.is_set():
       177                    raise InterruptedError("Indexing stopped")
       178                offset = state["cursor"]
       179                block_end = min(scan_end, offset + scan_chunk_size)
       180                block = source.read(offset, block_end - offset)
       181                relative = 0
       182                while relative + 512 <= len(block):
       183                    header = block[relative : relative + 512]
       184                    absolute = offset + relative
       185                    if header == bytes(512):
       186                        state["complete"] = True
       187                        state["cursor"] = scan_end
       188                        break
       189                    member = parse_header(header)
       190                    name = PurePosixPath(member.name).name
       191                    next_header = absolute + 512 + ((member.size + 511) // 512) * 512
       192                    if member.size < 0 or next_header > data_end:
       193                        raise ValueError(f"Tar member exceeds its archive: {member.name}")
       194                    if member.isfile() and PATTERNS[kind].fullmatch(name):
       195                        entry = {"offset": absolute + 512, "size": member.size}
       196                        if name in state["members"] and state["members"][name] != entry:
       197                            raise ValueError(f"Duplicate tar member name: {name}")
       198                        state["members"][name] = entry
       199                    processed += 1
       200                    # If the next header is outside this block, skip the unneeded
       201                    # image payload and request the next block at that exact header.
       202                    if next_header + 512 > block_end:
       203                        state["cursor"] = next_header
       204                        break
       205                    relative = next_header - offset
       206                    state["cursor"] = next_header
       207                    if needed.issubset(state["members"]):
       208                        break
       209                else:
       210                    state["cursor"] = block_end
       211                if state["complete"] or needed.issubset(state["members"]):
       212                    break
       213                if processed % 128 == 0 or time.monotonic() - last_saved >= 15:
       214                    atomic_write(cache, json.dumps(state).encode("utf-8"))
       215                    if kind == "classes":
       216                        print(f"Outer index: {len(state['members'])} classes cached; "
       217                              f"HTTP requests: {source.client.requests}", flush=True)
       218                    last_saved = time.monotonic()
       219            if state["cursor"] + 512 > scan_end:
       220                state["complete"] = True
       221        finally:
       222            atomic_write(cache, json.dumps(state).encode("utf-8"))
       223        return state["members"]
       224
       225
       226    def valid_image(path: Path, expected_size: int) -> bool:
       227        if not path.is_file() or path.stat().st_size != expected_size:
       228            return False
       229        try:
       230            with Image.open(path) as image:
       231                image.load()
       232            return True
       233        except (OSError, ValueError, Image.DecompressionBombError):
       234            return False
       235
       236
       237    def process_group(source, cache, start, end, data_end, kind, requested, args, scan_chunk_size):
       238        members = index_members(
       239            source, cache, start, end, data_end, kind, set(requested), scan_chunk_size
       240        )
       241        found = {}
       242        downloaded = existing = 0
       243        for name in sorted(set(requested).intersection(members)):
       244            relative = requested[name]
       245            entry = members[name]
       246            if not (0 < entry["size"] <= 128 * 1024 * 1024):
       247                raise ValueError(f"Unexpected image size for {relative}: {entry['size']}")
       248            found[relative] = entry["size"]
       249            if args.index_only:
       250                continue
       251            destination = args.output_dir / relative
       252            if valid_image(destination, entry["size"]):
       253                existing += 1
       254                continue
       255            content = source.read(entry["offset"], entry["size"])
       256            with Image.open(io.BytesIO(content)) as image:
       257                image.load()
       258            atomic_write(destination, content)
       259            downloaded += 1
       260        return found, downloaded, existing
       261
       262
       263    def run(args) -> int:
       264        names = load_manifest(args.manifest)
       265        if args.limit is not None:
       266            names = names[:args.limit]
       267        train = {}
       268        val = {}
       269        for name in names:
       270            parts = PurePosixPath(name).parts
       271            if parts[0] == "train":
       272                train.setdefault(parts[1] + ".tar", {})[parts[2]] = name
       273            else:
       274                val[parts[1]] = name
       275        client = RangeClient(args.timeout, args.retries)
       276        jobs = []
       277        if train:
       278            source = RemoteArchive(client, args.train_url)
       279            print(f"Indexing outer training tar for {len(train)} required classes...", flush=True)
       280            outer = index_members(
       281                source,
       282                args.index_dir / "train_outer.json",
       283                0,
       284                source.size,
       285                source.size,
       286                "classes",
       287                set(train),
       288                512,
       289            )
       290            missing_classes = sorted(set(train) - set(outer))
       291            if missing_classes:
       292                raise ValueError(f"Classes missing from training archive: {missing_classes}")
       293            class_bytes = sum(outer[name]["size"] for name in train)
       294            print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB. "
       295                  "Read-ahead indexing can transfer much of this data without storing it.", flush=True)
       296            for name, requested in sorted(train.items()):
       297                entry = outer[name]
       298                jobs.append((source, args.index_dir / "train" / f"{name}.json",
       299                             entry["offset"], entry["offset"] + entry["size"],
       300                             entry["offset"] + entry["size"], "train", requested, args,
       301                             512 if args.header_only else args.train_chunk_mib * 1024 * 1024))
       302        if val:
       303            source = RemoteArchive(client, args.val_url)
       304            jobs.append((source, args.index_dir / "val.json", 0, source.size, source.size,
       305                         "val", val, args,
       306                         512 if args.header_only else args.val_chunk_mib * 1024 * 1024))
       307        found = {}
       308        downloaded = existing = completed = 0
       309        errors = []
       310        executor = ThreadPoolExecutor(max_workers=args.workers)
       311        pending = {executor.submit(process_group, *job) for job in jobs}
       312        last_progress = time.monotonic()
       313        try:
       314            while pending:
       315                done, pending = wait(pending, timeout=10, return_when=FIRST_COMPLETED)
       316                for future in done:
       317                    completed += 1
       318                    try:
       319                        images, new, old = future.result()
       320                        if set(images).intersection(found):
       321                            raise ValueError("The same image appeared in more than one archive partition.")
       322                        found.update(images)
       323                        downloaded += new
       324                        existing += old
       325                    except Exception as error:
       326                        errors.append(str(error))
       327                        print(f"Group failed; rerun will reuse saved progress: {error}", file=sys.stderr, flush=True)
       328                if done or time.monotonic() - last_progress >= 20:
       329                    print(f"Groups {completed}/{len(jobs)}; images {len(found)}/{len(names)}; "
       330                          f"HTTP requests {client.requests}; received {client.bytes / 1024**2:.1f} MiB", flush=True)
       331                    last_progress = time.monotonic()
       332        except BaseException:
       333            client.stop.set()
       334            raise
       335        finally:
       336            executor.shutdown(wait=True, cancel_futures=True)
       337        missing = sorted(set(names) - set(found))
       338        report = {
       339            "mode": "index_only" if args.index_only else "download",
       340            "requested_images": len(names), "completed_images": len(found),
       341            "downloaded_images": downloaded, "existing_images": existing,
       342            "selected_image_bytes": sum(found.values()), "http_requests": client.requests,
       343            "received_bytes": client.bytes, "missing_images": missing, "errors": errors,
       344        }
       345        atomic_write(args.index_dir / "last_run.json", json.dumps(report, indent=2).encode("utf-8"))
       346        print(f"Selected image bytes: {sum(found.values()) / 1024**3:.3f} GiB")
       347        print(f"Report: {args.index_dir / 'last_run.json'}")
       348        if missing or errors:
       349            print(f"Incomplete: {len(missing)} images; first missing paths: {missing[:10]}", file=sys.stderr)
       350            return 1
       351        action = "indexed" if args.index_only else "downloaded or verified"
       352        print(f"Complete: {len(names)} images {action}.")
       353        return 0
       354
       355
       356    def main() -> int:
       357        data = Path(__file__).resolve().parent
       358        parser = argparse.ArgumentParser(description=__doc__)
       359        parser.add_argument("--manifest", type=Path, default=data / "transfer_lists" / "imagenet_required.txt")
       360        parser.add_argument("--output-dir", type=Path, default=data / "ImageNet")
       361        parser.add_argument("--index-dir", type=Path, default=data / "imagenet_index")
       362        parser.add_argument("--workers", type=int, default=8)
       363        parser.add_argument("--timeout", type=float, default=30)
       364        parser.add_argument("--retries", type=int, default=4)
       365        parser.add_argument("--train-chunk-mib", type=int, default=8)
       366        parser.add_argument("--val-chunk-mib", type=int, default=64)
       367        parser.add_argument("--limit", type=int, help="Use only the first N manifest entries for a smoke test")
       368        parser.add_argument("--index-only", action="store_true", help="Build reusable offsets without downloading images")
       369        parser.add_argument(
       370            "--header-only", action="store_true",
       371            help="Index with 512-byte header reads; less bandwidth, many more HTTP requests",
       372        )
       373        parser.add_argument("--train-url", default=f"{BASE_URL}/ILSVRC2012_img_train.tar")
       374        parser.add_argument("--val-url", default=f"{BASE_URL}/ILSVRC2012_img_val.tar")
       375        args = parser.parse_args()
       376        if (
       377            not 1 <= args.workers <= 64
       378            or args.timeout <= 0
       379            or args.retries < 0
       380            or args.train_chunk_mib < 1
       381            or args.val_chunk_mib < 1
       382        ):
       383            parser.error("Use 1..64 workers, a positive timeout/chunk size, and non-negative retries.")
       384        if args.limit is not None and args.limit < 1:
       385            parser.error("--limit must be positive")
       386        for name in ("manifest", "output_dir", "index_dir"):
       387            setattr(args, name, getattr(args, name).expanduser().resolve())
       388        return run(args)
       389
       390
       391    if __name__ == "__main__":
       392        try:
       393            raise SystemExit(main())
       394        except KeyboardInterrupt:
       395            print("Interrupted. Rerun the same command to reuse cached indexes and complete images.", file=sys.stderr)
       396            raise SystemExit(130)
       397        except (OSError, ValueError, RuntimeError, tarfile.TarError) as error:
       398            print(f"Error: {error}", file=sys.stderr)
       399            raise SystemExit(1)
    ✓ • 79ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/download_imagenet_subset.py
    @@ -293,4 +293,7 @@
             class_bytes = sum(outer[name]["size"] for name in train)
    -        print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB. "
    -              "Read-ahead indexing can transfer much of this data without storing it.", flush=True)
    +        print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB.", flush=True)
    +        if args.header_only:
    +            print("Indexing headers only: low bandwidth, but many HTTP requests.", flush=True)
    +        else:
    +            print("Read-ahead indexing can transfer much of this data without storing it.", flush=True)
             for name, requested in sorted(train.items()):

## Activity

    $ PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -p 'test_clip_category_selection.py' -v
    test_all_annotations_supply_counts_and_evaluation_objects (test_clip_category_selection.CategorySelectionTests.test_all_annotations_supply_counts_and_evaluation_objects) ... ok
    test_invalid_box_remains_in_ranking_and_is_reported_before_evaluation (test_clip_category_selection.CategorySelectionTests.test_invalid_box_remains_in_ranking_and_is_reported_before_evaluation) ... ok
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.032s
    
    OK
    ✓ • 1.93s

## Activity

    $ python - <<'PY'
        from pathlib import Path
        import ast
        import json
        path=Path('download_imagenet_subset.py')
        ast.parse(path.read_text())
        report=json.loads(Path('/tmp/ocl-range-live-2dnbvy9q/index/last_run.json').read_text())
        print('syntax=OK')
        print('real_download_report', report)
        print('required_input_files', {name:Path(name).is_file() for name in ['download_imagenet_subset.py','extract_imagenet_subset.py','transfer_lists/imagenet_required.txt']})
        PY
    syntax=OK
    real_download_report {'mode': 'download', 'requested_images': 2, 'completed_images': 2, 'downloaded_images': 2, 'existing_images': 0, 'selected_image_bytes': 2163026, 'http_requests': 6, 'received_bytes': 4261202, 'missing_images': [], 'errors': []}
    required_input_files {'download_imagenet_subset.py': True, 'extract_imagenet_subset.py': True, 'transfer_lists/imagenet_required.txt': True}
    ✓ • 91ms

## Assistant

可以，脚本已经完成：[download_imagenet_subset.py](/home/linfu/src/Test/ObjectConceptLearning/data/download_imagenet_subset.py)。已成功通过官方链接分段下载两张真实图片，无需保存完整 tar。

**需要说明：目前只有文件名清单，首次仍需建立“文件名 → 字节位置”索引。省流量和省时间有不同取舍：**

| 模式 | 首次运行行为 | 取舍 |
|---|---|---|
| `--header-only` | 读取归档头建立索引，再下载目标图片 | 流量少，但大量小请求可能较慢 |
| 默认模式 | 分块预读建立索引，再下载目标图片 | 请求更少，但可能额外读取数十 GB 数据；这些数据不落盘 |

两种模式最终都只保存需要的 **7,924 张图片**。索引缓存后，重跑会直接复用。

**1. 将这三个文件上传到服务器，保持目录结构。**

```text
ObjectConceptLearning/data/
  download_imagenet_subset.py
  extract_imagenet_subset.py
  transfer_lists/
    imagenet_required.txt
```

其中第二个脚本提供清单解析函数，不会触发完整下载。

**2. 在服务器准备一个轻量下载环境。**

以下命令在项目根目录执行，不需要 GPU：

```bash
cd /你的路径/ObjectConceptLearning

python3 -m venv .venv-download
.venv-download/bin/python -m pip install requests Pillow

mkdir -p logs
```

**3. 按你要求，使用仅读取归档头的模式。**

```bash
nohup .venv-download/bin/python -u data/download_imagenet_subset.py \
  --header-only \
  --workers 8 \
  --manifest data/transfer_lists/imagenet_required.txt \
  --output-dir data/ImageNet \
  --index-dir data/imagenet_index \
  > logs/imagenet_download.log 2>&1 &
```

查看进度：

```bash
tail -f logs/imagenet_download.log
```

程序会依次建立类别位置索引、建立图片位置索引、下载并检查图片。它会校验 HTTP `206` 和返回的字节范围，避免服务器忽略 Range 后意外下载整包。

**如果网络延迟较高、建索引明显太慢，可在停止当前任务后去掉 `--header-only` 重跑。** 已有索引仍然复用，但后续会增加预读流量。不要同时运行两个任务写入同一目录。

**4. 中断后继续与验收。**

中断后重新执行原命令即可。保留 `data/imagenet_index/`，程序会复用已建立的索引，并跳过大小正确且能解码的图片。

全部成功后应显示：

```text
Complete: 7924 images downloaded or verified.
```

查看报告和磁盘占用：

```bash
cat data/imagenet_index/last_run.json
du -sh data/ImageNet data/imagenet_index
```

报告应满足：

```text
completed_images: 7924
missing_images: []
errors: []
```

这能跳过本地完整下载，也适合你的 100 GB 服务器。**但首次建立索引仍有耗时，不能保证仅靠小流量就比预读模式更快；目前验证的是两张真实图片和断点恢复等测试，尚未完成全部 7,924 张下载。**

## User

你直接把图片下载好，并整理data目录，使其符合test.md

## User

继续，先检查现在的文件状态避免上次打断时导致了重复下载。

## Assistant

我先检查现有图片、索引缓存、临时文件和后台下载进程，确认上次中断留下了什么，再补齐缺失图片并校验目录与 `Test.md` 的要求。

## Activity

    $ df -h .
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sdd       1007G   66G  890G   7% /home/linfu/src/Test/ObjectConceptLearning/data
    ✓ • 71ms

## Activity

    $ git status --short
     M .gitignore
     M README.md
     M data/download_web_images.py
     M data/prepare_data.sh
    ?? Test.md
    ?? aPY/
    ?? clip_dataset.py
    ?? clip_inference.py
    ?? data/download_imagenet_subset.py
    ?? data/extract_imagenet_subset.py
    ?? data/from_web.tgz
    ?? data/from_web.tgz:Zone.Identifier
    ?? data/resources/OCL_annot_test.pkl
    ?? data/resources/OCL_annot_train.pkl
    ?? data/resources/OCL_annot_val.pkl
    ?? data/transfer_lists/
    ?? data/web_download_failures.json
    ?? docs/clip_inference.md
    ?? requirements-clip.txt
    ?? setup_clip_gpu.sh
    ?? tests/
    ✓ • 75ms

## Activity

    $ ps -eo pid,ppid,etime,stat,args
        PID    PPID     ELAPSED STAT COMMAND
          1       0       00:00 Ss   codex-linux-sandbox --sandbox-policy-cwd /home/linfu/src/Test/ObjectConceptLearning/data --command-cwd /home/linfu/src/Test/ObjectConceptLearning/data --permission-profile {"type":"managed","file_system":{"type":"restricted","entries":[{"path":{"type":"special","value":{"kind":"root"}},"access":"read"},{"path":{"type":"path","path":"/home/linfu/src/Test/ObjectConceptLearning/data"},"access":"write"},{"path":{"type":"special","value":{"kind":"slash_tmp"}},"access":"write"},{"path":{"type":"special","value":{"kind":"tmpdir"}},"access":"write"},{"path":{"type":"path","path":"/home/linfu/src/Test/ObjectConceptLearning/data/.git"},"access":"read","missing_path_behavior":"skip"},{"path":{"type":"path","path":"/home/linfu/src/Test/ObjectConceptLearning/data/.agents"},"access":"read","missing_path_behavior":"skip"},{"path":{"type":"path","path":"/home/linfu/src/Test/ObjectConceptLearning/data/.codex"},"access":"read","missing_path_behavior":"skip"},{"path":{"type":"path","path":"/home/linfu/src/Test/ObjectConceptLearning/data/.aws"},"access":"read","missing_path_behavior":"skip"}]},"network":"restricted"} --apply-seccomp-then-exec -- /bin/bash -c __CODEX_SNAPSHOT_OVERRIDE_SET_0="${CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS+x}" __CODEX_SNAPSHOT_OVERRIDE_0="${CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS-}" __CODEX_SNAPSHOT_OVERRIDE_SET_1="${CODEX_PERMISSION_PROFILE+x}" __CODEX_SNAPSHOT_OVERRIDE_1="${CODEX_PERMISSION_PROFILE-}" __CODEX_SNAPSHOT_OVERRIDE_SET_2="${CODEX_PLUGIN_METRICS_OUTPUT+x}" __CODEX_SNAPSHOT_OVERRIDE_2="${CODEX_PLUGIN_METRICS_OUTPUT-}" __CODEX_SNAPSHOT_OVERRIDE_SET_3="${CODEX_SESSION_ID+x}" __CODEX_SNAPSHOT_OVERRIDE_3="${CODEX_SESSION_ID-}" __CODEX_SNAPSHOT_OVERRIDE_SET_4="${CODEX_THREAD_ID+x}" __CODEX_SNAPSHOT_OVERRIDE_4="${CODEX_THREAD_ID-}" __CODEX_SNAPSHOT_OVERRIDE_SET_5="${CODEX_TOOL_CALL_ID+x}" __CODEX_SNAPSHOT_OVERRIDE_5="${CODEX_TOOL_CALL_ID-}" __CODEX_SNAPSHOT_OVERRIDE_SET_6="${CODEX_VERSION+x}" __CODEX_SNAPSHOT_OVERRIDE_6="${CODEX_VERSION-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_0="${ALL_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_0="${ALL_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_1="${BUNDLE_HTTPS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_1="${BUNDLE_HTTPS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_2="${BUNDLE_HTTP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_2="${BUNDLE_HTTP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_3="${BUNDLE_NO_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_3="${BUNDLE_NO_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_4="${BUNDLE_SSL_CA_CERT+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_4="${BUNDLE_SSL_CA_CERT-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_5="${CARGO_HTTP_CAINFO+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_5="${CARGO_HTTP_CAINFO-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_6="${CODEX_CA_CERTIFICATE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_6="${CODEX_CA_CERTIFICATE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_7="${CODEX_NETWORK_ALLOW_LOCAL_BINDING+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_7="${CODEX_NETWORK_ALLOW_LOCAL_BINDING-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_8="${CODEX_NETWORK_PROXY_ACTIVE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_8="${CODEX_NETWORK_PROXY_ACTIVE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_9="${CODEX_NETWORK_PROXY_ATTRIBUTION+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_9="${CODEX_NETWORK_PROXY_ATTRIBUTION-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_10="${CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_10="${CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_11="${CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_11="${CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_12="${CURL_CA_BUNDLE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_12="${CURL_CA_BUNDLE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_13="${DOCKER_HTTPS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_13="${DOCKER_HTTPS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_14="${DOCKER_HTTP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_14="${DOCKER_HTTP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_15="${ELECTRON_GET_USE_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_15="${ELECTRON_GET_USE_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_16="${FTP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_16="${FTP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_17="${GIT_SSL_CAINFO+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_17="${GIT_SSL_CAINFO-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_18="${HTTPS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_18="${HTTPS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_19="${HTTP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_19="${HTTP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_20="${NODE_EXTRA_CA_CERTS+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_20="${NODE_EXTRA_CA_CERTS-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_21="${NODE_USE_ENV_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_21="${NODE_USE_ENV_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_22="${NO_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_22="${NO_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_23="${NPM_CONFIG_CAFILE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_23="${NPM_CONFIG_CAFILE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_24="${NPM_CONFIG_HTTPS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_24="${NPM_CONFIG_HTTPS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_25="${NPM_CONFIG_HTTP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_25="${NPM_CONFIG_HTTP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_26="${NPM_CONFIG_NOPROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_26="${NPM_CONFIG_NOPROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_27="${NPM_CONFIG_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_27="${NPM_CONFIG_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_28="${PIP_CERT+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_28="${PIP_CERT-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_29="${PIP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_29="${PIP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_30="${REQUESTS_CA_BUNDLE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_30="${REQUESTS_CA_BUNDLE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_31="${SSL_CERT_FILE+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_31="${SSL_CERT_FILE-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_32="${WSS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_32="${WSS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_33="${WS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_33="${WS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_34="${YARN_HTTPS_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_34="${YARN_HTTPS_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_35="${YARN_HTTP_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_35="${YARN_HTTP_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_36="${YARN_NO_PROXY+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_36="${YARN_NO_PROXY-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_37="${all_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_37="${all_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_38="${ftp_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_38="${ftp_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_39="${http_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_39="${http_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_40="${https_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_40="${https_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_41="${no_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_41="${no_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_42="${npm_config_cafile+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_42="${npm_config_cafile-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_43="${npm_config_http_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_43="${npm_config_http_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_44="${npm_config_https_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_44="${npm_config_https_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_45="${npm_config_noproxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_45="${npm_config_noproxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_46="${npm_config_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_46="${npm_config_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_47="${ws_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_47="${ws_proxy-}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_48="${wss_proxy+x}" __CODEX_SNAPSHOT_PROXY_OVERRIDE_48="${wss_proxy-}" __CODEX_SNAPSHOT_PROXY_ENV_SET="${CODEX_NETWORK_PROXY_ACTIVE+x}"  if . '/home/linfu/.codex/shell_snapshots/01a16408-07ca-7253-9fb9-101a2f9a5f6a.1792679610490438124.sh' >/dev/null 2>&1; then :; fi  if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_0}" ]; then   if [ -z "${CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS+x}" ] || [ "${CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS-}" != "${__CODEX_SNAPSHOT_OVERRIDE_0}" ]; then export CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS="${__CODEX_SNAPSHOT_OVERRIDE_0}"; else export CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS; fi else builtin unset CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS 2>/dev/null || command unset CODEX_APPLY_PATCH_PRESERVE_LINE_ENDINGS; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_0 __CODEX_SNAPSHOT_OVERRIDE_0 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_0 __CODEX_SNAPSHOT_OVERRIDE_0 if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_1}" ]; then   if [ -z "${CODEX_PERMISSION_PROFILE+x}" ] || [ "${CODEX_PERMISSION_PROFILE-}" != "${__CODEX_SNAPSHOT_OVERRIDE_1}" ]; then export CODEX_PERMISSION_PROFILE="${__CODEX_SNAPSHOT_OVERRIDE_1}"; else export CODEX_PERMISSION_PROFILE; fi else builtin unset CODEX_PERMISSION_PROFILE 2>/dev/null || command unset CODEX_PERMISSION_PROFILE; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_1 __CODEX_SNAPSHOT_OVERRIDE_1 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_1 __CODEX_SNAPSHOT_OVERRIDE_1 if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_2}" ]; then   if [ -z "${CODEX_PLUGIN_METRICS_OUTPUT+x}" ] || [ "${CODEX_PLUGIN_METRICS_OUTPUT-}" != "${__CODEX_SNAPSHOT_OVERRIDE_2}" ]; then export CODEX_PLUGIN_METRICS_OUTPUT="${__CODEX_SNAPSHOT_OVERRIDE_2}"; else export CODEX_PLUGIN_METRICS_OUTPUT; fi else builtin unset CODEX_PLUGIN_METRICS_OUTPUT 2>/dev/null || command unset CODEX_PLUGIN_METRICS_OUTPUT; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_2 __CODEX_SNAPSHOT_OVERRIDE_2 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_2 __CODEX_SNAPSHOT_OVERRIDE_2 if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_3}" ]; then   if [ -z "${CODEX_SESSION_ID+x}" ] || [ "${CODEX_SESSION_ID-}" != "${__CODEX_SNAPSHOT_OVERRIDE_3}" ]; then export CODEX_SESSION_ID="${__CODEX_SNAPSHOT_OVERRIDE_3}"; else export CODEX_SESSION_ID; fi else builtin unset CODEX_SESSION_ID 2>/dev/null || command unset CODEX_SESSION_ID; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_3 __CODEX_SNAPSHOT_OVERRIDE_3 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_3 __CODEX_SNAPSHOT_OVERRIDE_3 if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_4}" ]; then   if [ -z "${CODEX_THREAD_ID+x}" ] || [ "${CODEX_THREAD_ID-}" != "${__CODEX_SNAPSHOT_OVERRIDE_4}" ]; then export CODEX_THREAD_ID="${__CODEX_SNAPSHOT_OVERRIDE_4}"; else export CODEX_THREAD_ID; fi else builtin unset CODEX_THREAD_ID 2>/dev/null || command unset CODEX_THREAD_ID; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_4 __CODEX_SNAPSHOT_OVERRIDE_4 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_4 __CODEX_SNAPSHOT_OVERRIDE_4 if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_5}" ]; then   if [ -z "${CODEX_TOOL_CALL_ID+x}" ] || [ "${CODEX_TOOL_CALL_ID-}" != "${__CODEX_SNAPSHOT_OVERRIDE_5}" ]; then export CODEX_TOOL_CALL_ID="${__CODEX_SNAPSHOT_OVERRIDE_5}"; else export CODEX_TOOL_CALL_ID; fi else builtin unset CODEX_TOOL_CALL_ID 2>/dev/null || command unset CODEX_TOOL_CALL_ID; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_5 __CODEX_SNAPSHOT_OVERRIDE_5 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_5 __CODEX_SNAPSHOT_OVERRIDE_5 if [ -n "${__CODEX_SNAPSHOT_OVERRIDE_SET_6}" ]; then   if [ -z "${CODEX_VERSION+x}" ] || [ "${CODEX_VERSION-}" != "${__CODEX_SNAPSHOT_OVERRIDE_6}" ]; then export CODEX_VERSION="${__CODEX_SNAPSHOT_OVERRIDE_6}"; else export CODEX_VERSION; fi else builtin unset CODEX_VERSION 2>/dev/null || command unset CODEX_VERSION; fi builtin unset __CODEX_SNAPSHOT_OVERRIDE_SET_6 __CODEX_SNAPSHOT_OVERRIDE_6 2>/dev/null || command unset __CODEX_SNAPSHOT_OVERRIDE_SET_6 __CODEX_SNAPSHOT_OVERRIDE_6 if [ -n "$__CODEX_SNAPSHOT_PROXY_ENV_SET" ] || [ -n "${CODEX_NETWORK_PROXY_ACTIVE+x}" ]; then if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_0}" ]; then   if [ -z "${ALL_PROXY+x}" ] || [ "${ALL_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_0}" ]; then export ALL_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_0}"; else export ALL_PROXY; fi else builtin unset ALL_PROXY 2>/dev/null || command unset ALL_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_0 __CODEX_SNAPSHOT_PROXY_OVERRIDE_0 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_0 __CODEX_SNAPSHOT_PROXY_OVERRIDE_0 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_1}" ]; then   if [ -z "${BUNDLE_HTTPS_PROXY+x}" ] || [ "${BUNDLE_HTTPS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_1}" ]; then export BUNDLE_HTTPS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_1}"; else export BUNDLE_HTTPS_PROXY; fi else builtin unset BUNDLE_HTTPS_PROXY 2>/dev/null || command unset BUNDLE_HTTPS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_1 __CODEX_SNAPSHOT_PROXY_OVERRIDE_1 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_1 __CODEX_SNAPSHOT_PROXY_OVERRIDE_1 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_2}" ]; then   if [ -z "${BUNDLE_HTTP_PROXY+x}" ] || [ "${BUNDLE_HTTP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_2}" ]; then export BUNDLE_HTTP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_2}"; else export BUNDLE_HTTP_PROXY; fi else builtin unset BUNDLE_HTTP_PROXY 2>/dev/null || command unset BUNDLE_HTTP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_2 __CODEX_SNAPSHOT_PROXY_OVERRIDE_2 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_2 __CODEX_SNAPSHOT_PROXY_OVERRIDE_2 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_3}" ]; then   if [ -z "${BUNDLE_NO_PROXY+x}" ] || [ "${BUNDLE_NO_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_3}" ]; then export BUNDLE_NO_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_3}"; else export BUNDLE_NO_PROXY; fi else builtin unset BUNDLE_NO_PROXY 2>/dev/null || command unset BUNDLE_NO_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_3 __CODEX_SNAPSHOT_PROXY_OVERRIDE_3 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_3 __CODEX_SNAPSHOT_PROXY_OVERRIDE_3 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_4}" ]; then   if [ -z "${BUNDLE_SSL_CA_CERT+x}" ] || [ "${BUNDLE_SSL_CA_CERT-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_4}" ]; then export BUNDLE_SSL_CA_CERT="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_4}"; else export BUNDLE_SSL_CA_CERT; fi else builtin unset BUNDLE_SSL_CA_CERT 2>/dev/null || command unset BUNDLE_SSL_CA_CERT; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_4 __CODEX_SNAPSHOT_PROXY_OVERRIDE_4 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_4 __CODEX_SNAPSHOT_PROXY_OVERRIDE_4 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_5}" ]; then   if [ -z "${CARGO_HTTP_CAINFO+x}" ] || [ "${CARGO_HTTP_CAINFO-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_5}" ]; then export CARGO_HTTP_CAINFO="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_5}"; else export CARGO_HTTP_CAINFO; fi else builtin unset CARGO_HTTP_CAINFO 2>/dev/null || command unset CARGO_HTTP_CAINFO; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_5 __CODEX_SNAPSHOT_PROXY_OVERRIDE_5 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_5 __CODEX_SNAPSHOT_PROXY_OVERRIDE_5 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_6}" ]; then   if [ -z "${CODEX_CA_CERTIFICATE+x}" ] || [ "${CODEX_CA_CERTIFICATE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_6}" ]; then export CODEX_CA_CERTIFICATE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_6}"; else export CODEX_CA_CERTIFICATE; fi else builtin unset CODEX_CA_CERTIFICATE 2>/dev/null || command unset CODEX_CA_CERTIFICATE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_6 __CODEX_SNAPSHOT_PROXY_OVERRIDE_6 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_6 __CODEX_SNAPSHOT_PROXY_OVERRIDE_6 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_7}" ]; then   if [ -z "${CODEX_NETWORK_ALLOW_LOCAL_BINDING+x}" ] || [ "${CODEX_NETWORK_ALLOW_LOCAL_BINDING-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_7}" ]; then export CODEX_NETWORK_ALLOW_LOCAL_BINDING="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_7}"; else export CODEX_NETWORK_ALLOW_LOCAL_BINDING; fi else builtin unset CODEX_NETWORK_ALLOW_LOCAL_BINDING 2>/dev/null || command unset CODEX_NETWORK_ALLOW_LOCAL_BINDING; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_7 __CODEX_SNAPSHOT_PROXY_OVERRIDE_7 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_7 __CODEX_SNAPSHOT_PROXY_OVERRIDE_7 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_8}" ]; then   if [ -z "${CODEX_NETWORK_PROXY_ACTIVE+x}" ] || [ "${CODEX_NETWORK_PROXY_ACTIVE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_8}" ]; then export CODEX_NETWORK_PROXY_ACTIVE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_8}"; else export CODEX_NETWORK_PROXY_ACTIVE; fi else builtin unset CODEX_NETWORK_PROXY_ACTIVE 2>/dev/null || command unset CODEX_NETWORK_PROXY_ACTIVE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_8 __CODEX_SNAPSHOT_PROXY_OVERRIDE_8 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_8 __CODEX_SNAPSHOT_PROXY_OVERRIDE_8 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_9}" ]; then   if [ -z "${CODEX_NETWORK_PROXY_ATTRIBUTION+x}" ] || [ "${CODEX_NETWORK_PROXY_ATTRIBUTION-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_9}" ]; then export CODEX_NETWORK_PROXY_ATTRIBUTION="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_9}"; else export CODEX_NETWORK_PROXY_ATTRIBUTION; fi else builtin unset CODEX_NETWORK_PROXY_ATTRIBUTION 2>/dev/null || command unset CODEX_NETWORK_PROXY_ATTRIBUTION; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_9 __CODEX_SNAPSHOT_PROXY_OVERRIDE_9 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_9 __CODEX_SNAPSHOT_PROXY_OVERRIDE_9 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_10}" ]; then   if [ -z "${CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS+x}" ] || [ "${CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_10}" ]; then export CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_10}"; else export CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS; fi else builtin unset CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS 2>/dev/null || command unset CODEX_NETWORK_PROXY_BROKERED_CREDENTIALS; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_10 __CODEX_SNAPSHOT_PROXY_OVERRIDE_10 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_10 __CODEX_SNAPSHOT_PROXY_OVERRIDE_10 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_11}" ]; then   if [ -z "${CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE+x}" ] || [ "${CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_11}" ]; then export CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_11}"; else export CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE; fi else builtin unset CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE 2>/dev/null || command unset CODEX_NETWORK_PROXY_CREDENTIAL_BROKER_ACTIVE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_11 __CODEX_SNAPSHOT_PROXY_OVERRIDE_11 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_11 __CODEX_SNAPSHOT_PROXY_OVERRIDE_11 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_12}" ]; then   if [ -z "${CURL_CA_BUNDLE+x}" ] || [ "${CURL_CA_BUNDLE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_12}" ]; then export CURL_CA_BUNDLE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_12}"; else export CURL_CA_BUNDLE; fi else builtin unset CURL_CA_BUNDLE 2>/dev/null || command unset CURL_CA_BUNDLE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_12 __CODEX_SNAPSHOT_PROXY_OVERRIDE_12 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_12 __CODEX_SNAPSHOT_PROXY_OVERRIDE_12 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_13}" ]; then   if [ -z "${DOCKER_HTTPS_PROXY+x}" ] || [ "${DOCKER_HTTPS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_13}" ]; then export DOCKER_HTTPS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_13}"; else export DOCKER_HTTPS_PROXY; fi else builtin unset DOCKER_HTTPS_PROXY 2>/dev/null || command unset DOCKER_HTTPS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_13 __CODEX_SNAPSHOT_PROXY_OVERRIDE_13 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_13 __CODEX_SNAPSHOT_PROXY_OVERRIDE_13 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_14}" ]; then   if [ -z "${DOCKER_HTTP_PROXY+x}" ] || [ "${DOCKER_HTTP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_14}" ]; then export DOCKER_HTTP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_14}"; else export DOCKER_HTTP_PROXY; fi else builtin unset DOCKER_HTTP_PROXY 2>/dev/null || command unset DOCKER_HTTP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_14 __CODEX_SNAPSHOT_PROXY_OVERRIDE_14 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_14 __CODEX_SNAPSHOT_PROXY_OVERRIDE_14 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_15}" ]; then   if [ -z "${ELECTRON_GET_USE_PROXY+x}" ] || [ "${ELECTRON_GET_USE_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_15}" ]; then export ELECTRON_GET_USE_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_15}"; else export ELECTRON_GET_USE_PROXY; fi else builtin unset ELECTRON_GET_USE_PROXY 2>/dev/null || command unset ELECTRON_GET_USE_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_15 __CODEX_SNAPSHOT_PROXY_OVERRIDE_15 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_15 __CODEX_SNAPSHOT_PROXY_OVERRIDE_15 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_16}" ]; then   if [ -z "${FTP_PROXY+x}" ] || [ "${FTP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_16}" ]; then export FTP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_16}"; else export FTP_PROXY; fi else builtin unset FTP_PROXY 2>/dev/null || command unset FTP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_16 __CODEX_SNAPSHOT_PROXY_OVERRIDE_16 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_16 __CODEX_SNAPSHOT_PROXY_OVERRIDE_16 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_17}" ]; then   if [ -z "${GIT_SSL_CAINFO+x}" ] || [ "${GIT_SSL_CAINFO-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_17}" ]; then export GIT_SSL_CAINFO="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_17}"; else export GIT_SSL_CAINFO; fi else builtin unset GIT_SSL_CAINFO 2>/dev/null || command unset GIT_SSL_CAINFO; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_17 __CODEX_SNAPSHOT_PROXY_OVERRIDE_17 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_17 __CODEX_SNAPSHOT_PROXY_OVERRIDE_17 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_18}" ]; then   if [ -z "${HTTPS_PROXY+x}" ] || [ "${HTTPS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_18}" ]; then export HTTPS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_18}"; else export HTTPS_PROXY; fi else builtin unset HTTPS_PROXY 2>/dev/null || command unset HTTPS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_18 __CODEX_SNAPSHOT_PROXY_OVERRIDE_18 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_18 __CODEX_SNAPSHOT_PROXY_OVERRIDE_18 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_19}" ]; then   if [ -z "${HTTP_PROXY+x}" ] || [ "${HTTP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_19}" ]; then export HTTP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_19}"; else export HTTP_PROXY; fi else builtin unset HTTP_PROXY 2>/dev/null || command unset HTTP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_19 __CODEX_SNAPSHOT_PROXY_OVERRIDE_19 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_19 __CODEX_SNAPSHOT_PROXY_OVERRIDE_19 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_20}" ]; then   if [ -z "${NODE_EXTRA_CA_CERTS+x}" ] || [ "${NODE_EXTRA_CA_CERTS-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_20}" ]; then export NODE_EXTRA_CA_CERTS="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_20}"; else export NODE_EXTRA_CA_CERTS; fi else builtin unset NODE_EXTRA_CA_CERTS 2>/dev/null || command unset NODE_EXTRA_CA_CERTS; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_20 __CODEX_SNAPSHOT_PROXY_OVERRIDE_20 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_20 __CODEX_SNAPSHOT_PROXY_OVERRIDE_20 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_21}" ]; then   if [ -z "${NODE_USE_ENV_PROXY+x}" ] || [ "${NODE_USE_ENV_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_21}" ]; then export NODE_USE_ENV_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_21}"; else export NODE_USE_ENV_PROXY; fi else builtin unset NODE_USE_ENV_PROXY 2>/dev/null || command unset NODE_USE_ENV_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_21 __CODEX_SNAPSHOT_PROXY_OVERRIDE_21 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_21 __CODEX_SNAPSHOT_PROXY_OVERRIDE_21 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_22}" ]; then   if [ -z "${NO_PROXY+x}" ] || [ "${NO_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_22}" ]; then export NO_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_22}"; else export NO_PROXY; fi else builtin unset NO_PROXY 2>/dev/null || command unset NO_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_22 __CODEX_SNAPSHOT_PROXY_OVERRIDE_22 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_22 __CODEX_SNAPSHOT_PROXY_OVERRIDE_22 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_23}" ]; then   if [ -z "${NPM_CONFIG_CAFILE+x}" ] || [ "${NPM_CONFIG_CAFILE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_23}" ]; then export NPM_CONFIG_CAFILE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_23}"; else export NPM_CONFIG_CAFILE; fi else builtin unset NPM_CONFIG_CAFILE 2>/dev/null || command unset NPM_CONFIG_CAFILE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_23 __CODEX_SNAPSHOT_PROXY_OVERRIDE_23 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_23 __CODEX_SNAPSHOT_PROXY_OVERRIDE_23 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_24}" ]; then   if [ -z "${NPM_CONFIG_HTTPS_PROXY+x}" ] || [ "${NPM_CONFIG_HTTPS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_24}" ]; then export NPM_CONFIG_HTTPS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_24}"; else export NPM_CONFIG_HTTPS_PROXY; fi else builtin unset NPM_CONFIG_HTTPS_PROXY 2>/dev/null || command unset NPM_CONFIG_HTTPS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_24 __CODEX_SNAPSHOT_PROXY_OVERRIDE_24 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_24 __CODEX_SNAPSHOT_PROXY_OVERRIDE_24 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_25}" ]; then   if [ -z "${NPM_CONFIG_HTTP_PROXY+x}" ] || [ "${NPM_CONFIG_HTTP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_25}" ]; then export NPM_CONFIG_HTTP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_25}"; else export NPM_CONFIG_HTTP_PROXY; fi else builtin unset NPM_CONFIG_HTTP_PROXY 2>/dev/null || command unset NPM_CONFIG_HTTP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_25 __CODEX_SNAPSHOT_PROXY_OVERRIDE_25 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_25 __CODEX_SNAPSHOT_PROXY_OVERRIDE_25 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_26}" ]; then   if [ -z "${NPM_CONFIG_NOPROXY+x}" ] || [ "${NPM_CONFIG_NOPROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_26}" ]; then export NPM_CONFIG_NOPROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_26}"; else export NPM_CONFIG_NOPROXY; fi else builtin unset NPM_CONFIG_NOPROXY 2>/dev/null || command unset NPM_CONFIG_NOPROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_26 __CODEX_SNAPSHOT_PROXY_OVERRIDE_26 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_26 __CODEX_SNAPSHOT_PROXY_OVERRIDE_26 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_27}" ]; then   if [ -z "${NPM_CONFIG_PROXY+x}" ] || [ "${NPM_CONFIG_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_27}" ]; then export NPM_CONFIG_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_27}"; else export NPM_CONFIG_PROXY; fi else builtin unset NPM_CONFIG_PROXY 2>/dev/null || command unset NPM_CONFIG_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_27 __CODEX_SNAPSHOT_PROXY_OVERRIDE_27 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_27 __CODEX_SNAPSHOT_PROXY_OVERRIDE_27 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_28}" ]; then   if [ -z "${PIP_CERT+x}" ] || [ "${PIP_CERT-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_28}" ]; then export PIP_CERT="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_28}"; else export PIP_CERT; fi else builtin unset PIP_CERT 2>/dev/null || command unset PIP_CERT; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_28 __CODEX_SNAPSHOT_PROXY_OVERRIDE_28 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_28 __CODEX_SNAPSHOT_PROXY_OVERRIDE_28 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_29}" ]; then   if [ -z "${PIP_PROXY+x}" ] || [ "${PIP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_29}" ]; then export PIP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_29}"; else export PIP_PROXY; fi else builtin unset PIP_PROXY 2>/dev/null || command unset PIP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_29 __CODEX_SNAPSHOT_PROXY_OVERRIDE_29 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_29 __CODEX_SNAPSHOT_PROXY_OVERRIDE_29 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_30}" ]; then   if [ -z "${REQUESTS_CA_BUNDLE+x}" ] || [ "${REQUESTS_CA_BUNDLE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_30}" ]; then export REQUESTS_CA_BUNDLE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_30}"; else export REQUESTS_CA_BUNDLE; fi else builtin unset REQUESTS_CA_BUNDLE 2>/dev/null || command unset REQUESTS_CA_BUNDLE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_30 __CODEX_SNAPSHOT_PROXY_OVERRIDE_30 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_30 __CODEX_SNAPSHOT_PROXY_OVERRIDE_30 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_31}" ]; then   if [ -z "${SSL_CERT_FILE+x}" ] || [ "${SSL_CERT_FILE-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_31}" ]; then export SSL_CERT_FILE="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_31}"; else export SSL_CERT_FILE; fi else builtin unset SSL_CERT_FILE 2>/dev/null || command unset SSL_CERT_FILE; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_31 __CODEX_SNAPSHOT_PROXY_OVERRIDE_31 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_31 __CODEX_SNAPSHOT_PROXY_OVERRIDE_31 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_32}" ]; then   if [ -z "${WSS_PROXY+x}" ] || [ "${WSS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_32}" ]; then export WSS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_32}"; else export WSS_PROXY; fi else builtin unset WSS_PROXY 2>/dev/null || command unset WSS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_32 __CODEX_SNAPSHOT_PROXY_OVERRIDE_32 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_32 __CODEX_SNAPSHOT_PROXY_OVERRIDE_32 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_33}" ]; then   if [ -z "${WS_PROXY+x}" ] || [ "${WS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_33}" ]; then export WS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_33}"; else export WS_PROXY; fi else builtin unset WS_PROXY 2>/dev/null || command unset WS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_33 __CODEX_SNAPSHOT_PROXY_OVERRIDE_33 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_33 __CODEX_SNAPSHOT_PROXY_OVERRIDE_33 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_34}" ]; then   if [ -z "${YARN_HTTPS_PROXY+x}" ] || [ "${YARN_HTTPS_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_34}" ]; then export YARN_HTTPS_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_34}"; else export YARN_HTTPS_PROXY; fi else builtin unset YARN_HTTPS_PROXY 2>/dev/null || command unset YARN_HTTPS_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_34 __CODEX_SNAPSHOT_PROXY_OVERRIDE_34 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_34 __CODEX_SNAPSHOT_PROXY_OVERRIDE_34 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_35}" ]; then   if [ -z "${YARN_HTTP_PROXY+x}" ] || [ "${YARN_HTTP_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_35}" ]; then export YARN_HTTP_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_35}"; else export YARN_HTTP_PROXY; fi else builtin unset YARN_HTTP_PROXY 2>/dev/null || command unset YARN_HTTP_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_35 __CODEX_SNAPSHOT_PROXY_OVERRIDE_35 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_35 __CODEX_SNAPSHOT_PROXY_OVERRIDE_35 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_36}" ]; then   if [ -z "${YARN_NO_PROXY+x}" ] || [ "${YARN_NO_PROXY-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_36}" ]; then export YARN_NO_PROXY="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_36}"; else export YARN_NO_PROXY; fi else builtin unset YARN_NO_PROXY 2>/dev/null || command unset YARN_NO_PROXY; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_36 __CODEX_SNAPSHOT_PROXY_OVERRIDE_36 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_36 __CODEX_SNAPSHOT_PROXY_OVERRIDE_36 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_37}" ]; then   if [ -z "${all_proxy+x}" ] || [ "${all_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_37}" ]; then export all_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_37}"; else export all_proxy; fi else builtin unset all_proxy 2>/dev/null || command unset all_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_37 __CODEX_SNAPSHOT_PROXY_OVERRIDE_37 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_37 __CODEX_SNAPSHOT_PROXY_OVERRIDE_37 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_38}" ]; then   if [ -z "${ftp_proxy+x}" ] || [ "${ftp_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_38}" ]; then export ftp_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_38}"; else export ftp_proxy; fi else builtin unset ftp_proxy 2>/dev/null || command unset ftp_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_38 __CODEX_SNAPSHOT_PROXY_OVERRIDE_38 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_38 __CODEX_SNAPSHOT_PROXY_OVERRIDE_38 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_39}" ]; then   if [ -z "${http_proxy+x}" ] || [ "${http_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_39}" ]; then export http_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_39}"; else export http_proxy; fi else builtin unset http_proxy 2>/dev/null || command unset http_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_39 __CODEX_SNAPSHOT_PROXY_OVERRIDE_39 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_39 __CODEX_SNAPSHOT_PROXY_OVERRIDE_39 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_40}" ]; then   if [ -z "${https_proxy+x}" ] || [ "${https_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_40}" ]; then export https_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_40}"; else export https_proxy; fi else builtin unset https_proxy 2>/dev/null || command unset https_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_40 __CODEX_SNAPSHOT_PROXY_OVERRIDE_40 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_40 __CODEX_SNAPSHOT_PROXY_OVERRIDE_40 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_41}" ]; then   if [ -z "${no_proxy+x}" ] || [ "${no_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_41}" ]; then export no_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_41}"; else export no_proxy; fi else builtin unset no_proxy 2>/dev/null || command unset no_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_41 __CODEX_SNAPSHOT_PROXY_OVERRIDE_41 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_41 __CODEX_SNAPSHOT_PROXY_OVERRIDE_41 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_42}" ]; then   if [ -z "${npm_config_cafile+x}" ] || [ "${npm_config_cafile-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_42}" ]; then export npm_config_cafile="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_42}"; else export npm_config_cafile; fi else builtin unset npm_config_cafile 2>/dev/null || command unset npm_config_cafile; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_42 __CODEX_SNAPSHOT_PROXY_OVERRIDE_42 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_42 __CODEX_SNAPSHOT_PROXY_OVERRIDE_42 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_43}" ]; then   if [ -z "${npm_config_http_proxy+x}" ] || [ "${npm_config_http_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_43}" ]; then export npm_config_http_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_43}"; else export npm_config_http_proxy; fi else builtin unset npm_config_http_proxy 2>/dev/null || command unset npm_config_http_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_43 __CODEX_SNAPSHOT_PROXY_OVERRIDE_43 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_43 __CODEX_SNAPSHOT_PROXY_OVERRIDE_43 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_44}" ]; then   if [ -z "${npm_config_https_proxy+x}" ] || [ "${npm_config_https_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_44}" ]; then export npm_config_https_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_44}"; else export npm_config_https_proxy; fi else builtin unset npm_config_https_proxy 2>/dev/null || command unset npm_config_https_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_44 __CODEX_SNAPSHOT_PROXY_OVERRIDE_44 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_44 __CODEX_SNAPSHOT_PROXY_OVERRIDE_44 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_45}" ]; then   if [ -z "${npm_config_noproxy+x}" ] || [ "${npm_config_noproxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_45}" ]; then export npm_config_noproxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_45}"; else export npm_config_noproxy; fi else builtin unset npm_config_noproxy 2>/dev/null || command unset npm_config_noproxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_45 __CODEX_SNAPSHOT_PROXY_OVERRIDE_45 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_45 __CODEX_SNAPSHOT_PROXY_OVERRIDE_45 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_46}" ]; then   if [ -z "${npm_config_proxy+x}" ] || [ "${npm_config_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_46}" ]; then export npm_config_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_46}"; else export npm_config_proxy; fi else builtin unset npm_config_proxy 2>/dev/null || command unset npm_config_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_46 __CODEX_SNAPSHOT_PROXY_OVERRIDE_46 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_46 __CODEX_SNAPSHOT_PROXY_OVERRIDE_46 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_47}" ]; then   if [ -z "${ws_proxy+x}" ] || [ "${ws_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_47}" ]; then export ws_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_47}"; else export ws_proxy; fi else builtin unset ws_proxy 2>/dev/null || command unset ws_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_47 __CODEX_SNAPSHOT_PROXY_OVERRIDE_47 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_47 __CODEX_SNAPSHOT_PROXY_OVERRIDE_47 if [ -n "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_48}" ]; then   if [ -z "${wss_proxy+x}" ] || [ "${wss_proxy-}" != "${__CODEX_SNAPSHOT_PROXY_OVERRIDE_48}" ]; then export wss_proxy="${__CODEX_SNAPSHOT_PROXY_OVERRIDE_48}"; else export wss_proxy; fi else builtin unset wss_proxy 2>/dev/null || command unset wss_proxy; fi builtin unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_48 __CODEX_SNAPSHOT_PROXY_OVERRIDE_48 2>/dev/null || command unset __CODEX_SNAPSHOT_PROXY_OVERRIDE_SET_48 __CODEX_SNAPSHOT_PROXY_OVERRIDE_48 fi if [ -n "${PATH:-}" ]; then export PATH='/home/linfu/.codex/packages/app-server-daemon/releases/0.163.0-x86_64-unknown-linux-musl/codex-path':"$PATH"; else export PATH='/home/linfu/.codex/packages/app-server-daemon/releases/0.163.0-x86_64-unknown-linux-musl/codex-path'; fi  exec '/bin/bash' -c 'ps -eo pid,ppid,etime,stat,args'
          2       1       00:00 R    ps -eo pid,ppid,etime,stat,args
    ✓ • 51ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        root=Path('/home/linfu/src/Test/ObjectConceptLearning')
        for base in [Path('/'),Path('/home'),Path('/home/linfu'),Path('/home/linfu/src'),Path('/home/linfu/src/Test'),root,root/'data']:
            p=base/'AGENTS.md'
            if p.is_file(): print(p, p.read_text())
        for base in [root/'data',root/'data/imagenet_index',root/'data/imagenet_archives',root/'logs']:
            print('\nDIRECTORY',base,'exists',base.exists())
            if base.is_dir():
                for p in sorted(base.iterdir()):
                    if p.name in {'.git','.aws','.codex','.agents'}: continue
                    print(p.name, 'link='+str(p.readlink()) if p.is_symlink() else 'dir' if p.is_dir() else 'bytes='+str(p.stat().st_size))
        print('\nTEST REQUIREMENTS\n'+(root/'Test.md').read_text())
        PY
    
    DIRECTORY /home/linfu/src/Test/ObjectConceptLearning/data exists True
    COCO dir
    SUN dir
    __pycache__ dir
    aPY dir
    download_imagenet_subset.py bytes=17858
    download_web_images.py bytes=5226
    extract_imagenet_subset.py bytes=5904
    from_web dir
    from_web.tgz bytes=280569727
    from_web.tgz:Zone.Identifier bytes=25
    prepare_data.sh bytes=1090
    resources dir
    train2014 dir
    transfer_lists dir
    val2014 dir
    web_download_failures.json bytes=1441617
    数据集 dir
    
    DIRECTORY /home/linfu/src/Test/ObjectConceptLearning/data/imagenet_index exists False
    
    DIRECTORY /home/linfu/src/Test/ObjectConceptLearning/data/imagenet_archives exists False
    
    DIRECTORY /home/linfu/src/Test/ObjectConceptLearning/logs exists False
    
    TEST REQUIREMENTS
    # OCL
    
    Implement an OCL-based object category classification inference experiment.
    
    Set up your own Python environment by downloading and installing **Miniforge / uv / Python**, and then begin the experiment.
    
    ## References
    
    1. OCL paper: **Beyond Object Recognition: A New Benchmark towards Object Concept Learning**
    
    2. **OCL dataset preparation**
    
       - The official data preparation scripts are provided in the OCL GitHub repository: [https://github.com/silicx/ObjectConceptLearning/tree/main/data](https://github.com/silicx/ObjectConceptLearning/tree/main/data)
       - Please read and understand the provided scripts and dataset structure before implementing the DataLoader.
       - In particular, the repository provides `prepare_data.sh`, `download_web_images.py`, and the `resources` directory for dataset preparation.
       - After downloading the dataset, inspect the image data and annotation files carefully and understand how **category**, **attribute**, and **affordance** annotations are represented.
    
    3. Download and prepare the required test data using the scripts provided in the official OCL GitHub repository.
    
    4. CLIP paper/repository: **Contrastive Language-Image Pre-Training**
    
       [https://github.com/openai/CLIP](https://github.com/openai/CLIP)
    
    ## Step 1: Prepare the DataLoader
    
    1. Implement a custom dataset class by inheriting from PyTorch's native `Dataset`:
    
       - Load the dataset and corresponding annotations;
       - Filter the data by sorting category labels according to the number of samples, and keep only the **10 categories with the largest number of samples**;
       - Perform image preprocessing and text tokenization.
    
    2. Create a test data loader using PyTorch's native `DataLoader`:
    
       - Set `batch_size = 4`.
    
    ## Step 2: Prepare the CLIP Model
    
    1. Load a pretrained CLIP model using the available API.
    
    ## Step 3: Inference and Evaluation
    
    1. Instantiate the dataset and model, and move the model to GPU, including:
    
       - `load_dataset`
       - `load_model`
       - `model.to(device)`
    
    2. Set the model to inference mode and freeze all model parameters:
    
       - Iterate over all model parameters and set gradient computation to `False`.
    
    3. Iterate over the test set and perform inference:
    
       - Each image may contain multiple objects.
       - Compute the cosine similarity between each object and the candidate **category** labels.
       - Use the cosine similarity scores for ranking.
       - Compute the model's **Top-k accuracy**.
       - Perform forward inference batch by batch and report the average accuracy over the entire test set.
    
    4. Evaluate the prediction performance for **attribute** and **affordance** labels using the **mAP (mean Average Precision)** metric.
    
    ✓ • 159ms

## Activity

    $ rg --files -g '*.py' -g '*.json' -g '*.txt' -g '*.log' -g '*.part' -g 'AGENTS.md' -g '!resources/**' -g '!aPY/**' -g '!SUN/**' -g '!train2014/**' -g '!val2014/**' -g '!COCO/**' -g '!from_web/**' -g '!ImageNet/**' -g '!imagenet_archives/**' -g '!数据集/**'
    web_download_failures.json
    download_web_images.py
    extract_imagenet_subset.py
    download_imagenet_subset.py
    transfer_lists/imagenet_required.txt
    transfer_lists/selection.json
    transfer_lists/ocl_non_imagenet.txt
    ✓ • 602ms

## Activity

    $ cat download_web_images.py
    """Resume OCL web-image downloads and report unavailable images."""
    
    import argparse
    import json
    import tempfile
    import time
    from pathlib import Path
    
    import requests
    from PIL import Image
    from tqdm import tqdm
    
    
    IMAGE_ERRORS = (OSError, ValueError, SyntaxError, Image.DecompressionBombError)
    
    
    def validate_image(path):
        with Image.open(path) as image:
            image.load()
    
    
    def download_image(session, url, destination, timeout=20, retries=2):
        """Return a status and failed attempts, preserving existing files on failure."""
        destination = Path(destination)
        if destination.is_file():
            try:
                validate_image(destination)
                return "skipped", []
            except IMAGE_ERRORS:
                pass
    
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Many old HTTP image URLs now require HTTPS. Keep HTTP as a fallback.
        candidates = ["https://" + url[7:], url] if url.startswith("http://") else [url]
        errors = []
        for candidate in candidates:
            for attempt in range(retries + 1):
                temporary = None
                try:
                    with session.get(
                        candidate, stream=True, timeout=(min(10, timeout), timeout)
                    ) as response:
                        response.raise_for_status()
                        with tempfile.NamedTemporaryFile(
                            dir=destination.parent,
                            prefix="." + destination.name + ".",
                            suffix=".part",
                            delete=False,
                        ) as handle:
                            temporary = Path(handle.name)
                            for chunk in response.iter_content(chunk_size=65536):
                                handle.write(chunk)
                    validate_image(temporary)
                    # Publish only a complete, decodable image, on the same filesystem.
                    temporary.replace(destination)
                    return "downloaded", errors
                except (requests.RequestException,) + IMAGE_ERRORS as error:
                    errors.append(
                        {"url": candidate, "attempt": attempt + 1, "error": str(error)}
                    )
                    retryable = isinstance(error, requests.RequestException)
                    if isinstance(error, requests.HTTPError):
                        status = error.response.status_code
                        retryable = status in (408, 429) or 500 <= status < 600
                    if not retryable or attempt == retries:
                        break
                    time.sleep(min(2 ** attempt, 5))
                finally:
                    if temporary is not None:
                        temporary.unlink(missing_ok=True)
        return "failed", errors
    
    
    def main(argv=None):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument(
            "--data-root", type=Path, default=Path(__file__).resolve().parent
        )
        parser.add_argument("--timeout", type=float, default=20, help="Socket timeout in seconds")
        parser.add_argument("--retries", type=int, default=2, help="Extra attempts per URL")
        parser.add_argument("--limit", type=int, help="Process only the first N entries")
        args = parser.parse_args(argv)
        if args.timeout <= 0 or args.retries < 0 or (args.limit is not None and args.limit <= 0):
            parser.error("timeout and limit must be positive; retries must be non-negative")
    
        root = args.data_root.expanduser().resolve()
        with (root / "resources" / "url_to_filename.json").open(encoding="utf-8") as handle:
            entries = json.load(handle)
        entries = entries[:args.limit]
        counts = {"downloaded": 0, "skipped": 0, "failed": 0}
        failures = []
        interrupted = False
        with requests.Session() as session:
            session.headers.update(
                {"User-Agent": "Mozilla/5.0 (compatible; OCL-image-downloader/1.0)"}
            )
            try:
                with tqdm(entries, desc="Web images", unit="image", ncols=100) as progress:
                    for url, name in progress:
                        status, errors = download_image(
                            session, url, root / name, timeout=args.timeout, retries=args.retries
                        )
                        counts[status] += 1
                        if status == "failed":
                            failures.append({"url": url, "name": name, "attempts": errors})
                            tqdm.write("Failed {}: {}".format(name, errors[-1]["error"]))
                        progress.set_postfix(counts, refresh=False)
            except KeyboardInterrupt:
                interrupted = True
    
        report = {
            "requested": len(entries),
            **counts,
            "pending": len(entries) - sum(counts.values()),
            "interrupted": interrupted,
            "failures": failures,
        }
        report_path = root / "web_download_failures.json"
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(
            "Downloaded: {downloaded}; already valid: {skipped}; failed: {failed}; "
            "pending: {pending}.".format(**report)
        )
        print("Report: {}. Rerun to retry missing or invalid images.".format(report_path))
        return 130 if interrupted else (1 if failures else 0)
    
    
    if __name__ == "__main__":
        raise SystemExit(main())
    ✓ • 0ms

## Activity

    $ sed -n '145,360p' download_imagenet_subset.py
        if member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE):
            raise ValueError(f"Unsupported tar header type for {member.name!r}: {member.type!r}")
        return member
    
    
    def index_members(
        source: RemoteArchive,
        cache: Path,
        start: int,
        scan_end: int,
        data_end: int,
        kind: str,
        needed: set[str],
        scan_chunk_size: int,
    ) -> dict:
        signature = {
            "version": 1, "source": source.identity, "start": start,
            "scan_end": scan_end, "data_end": data_end, "kind": kind,
        }
        state = {}
        if cache.is_file():
            state = json.loads(cache.read_text(encoding="utf-8"))
        if state.get("signature") != signature:
            state = {"signature": signature, "cursor": start,
                     "complete": False, "members": {}}
        if needed.issubset(state["members"]) or state["complete"]:
            return state["members"]
        processed = 0
        last_saved = time.monotonic()
        try:
            while state["cursor"] + 512 <= scan_end:
                if source.client.stop.is_set():
                    raise InterruptedError("Indexing stopped")
                offset = state["cursor"]
                block_end = min(scan_end, offset + scan_chunk_size)
                block = source.read(offset, block_end - offset)
                relative = 0
                while relative + 512 <= len(block):
                    header = block[relative : relative + 512]
                    absolute = offset + relative
                    if header == bytes(512):
                        state["complete"] = True
                        state["cursor"] = scan_end
                        break
                    member = parse_header(header)
                    name = PurePosixPath(member.name).name
                    next_header = absolute + 512 + ((member.size + 511) // 512) * 512
                    if member.size < 0 or next_header > data_end:
                        raise ValueError(f"Tar member exceeds its archive: {member.name}")
                    if member.isfile() and PATTERNS[kind].fullmatch(name):
                        entry = {"offset": absolute + 512, "size": member.size}
                        if name in state["members"] and state["members"][name] != entry:
                            raise ValueError(f"Duplicate tar member name: {name}")
                        state["members"][name] = entry
                    processed += 1
                    # If the next header is outside this block, skip the unneeded
                    # image payload and request the next block at that exact header.
                    if next_header + 512 > block_end:
                        state["cursor"] = next_header
                        break
                    relative = next_header - offset
                    state["cursor"] = next_header
                    if needed.issubset(state["members"]):
                        break
                else:
                    state["cursor"] = block_end
                if state["complete"] or needed.issubset(state["members"]):
                    break
                if processed % 128 == 0 or time.monotonic() - last_saved >= 15:
                    atomic_write(cache, json.dumps(state).encode("utf-8"))
                    if kind == "classes":
                        print(f"Outer index: {len(state['members'])} classes cached; "
                              f"HTTP requests: {source.client.requests}", flush=True)
                    last_saved = time.monotonic()
            if state["cursor"] + 512 > scan_end:
                state["complete"] = True
        finally:
            atomic_write(cache, json.dumps(state).encode("utf-8"))
        return state["members"]
    
    
    def valid_image(path: Path, expected_size: int) -> bool:
        if not path.is_file() or path.stat().st_size != expected_size:
            return False
        try:
            with Image.open(path) as image:
                image.load()
            return True
        except (OSError, ValueError, Image.DecompressionBombError):
            return False
    
    
    def process_group(source, cache, start, end, data_end, kind, requested, args, scan_chunk_size):
        members = index_members(
            source, cache, start, end, data_end, kind, set(requested), scan_chunk_size
        )
        found = {}
        downloaded = existing = 0
        for name in sorted(set(requested).intersection(members)):
            relative = requested[name]
            entry = members[name]
            if not (0 < entry["size"] <= 128 * 1024 * 1024):
                raise ValueError(f"Unexpected image size for {relative}: {entry['size']}")
            found[relative] = entry["size"]
            if args.index_only:
                continue
            destination = args.output_dir / relative
            if valid_image(destination, entry["size"]):
                existing += 1
                continue
            content = source.read(entry["offset"], entry["size"])
            with Image.open(io.BytesIO(content)) as image:
                image.load()
            atomic_write(destination, content)
            downloaded += 1
        return found, downloaded, existing
    
    
    def run(args) -> int:
        names = load_manifest(args.manifest)
        if args.limit is not None:
            names = names[:args.limit]
        train = {}
        val = {}
        for name in names:
            parts = PurePosixPath(name).parts
            if parts[0] == "train":
                train.setdefault(parts[1] + ".tar", {})[parts[2]] = name
            else:
                val[parts[1]] = name
        client = RangeClient(args.timeout, args.retries)
        jobs = []
        if train:
            source = RemoteArchive(client, args.train_url)
            print(f"Indexing outer training tar for {len(train)} required classes...", flush=True)
            outer = index_members(
                source,
                args.index_dir / "train_outer.json",
                0,
                source.size,
                source.size,
                "classes",
                set(train),
                512,
            )
            missing_classes = sorted(set(train) - set(outer))
            if missing_classes:
                raise ValueError(f"Classes missing from training archive: {missing_classes}")
            class_bytes = sum(outer[name]["size"] for name in train)
            print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB.", flush=True)
            if args.header_only:
                print("Indexing headers only: low bandwidth, but many HTTP requests.", flush=True)
            else:
                print("Read-ahead indexing can transfer much of this data without storing it.", flush=True)
            for name, requested in sorted(train.items()):
                entry = outer[name]
                jobs.append((source, args.index_dir / "train" / f"{name}.json",
                             entry["offset"], entry["offset"] + entry["size"],
                             entry["offset"] + entry["size"], "train", requested, args,
                             512 if args.header_only else args.train_chunk_mib * 1024 * 1024))
        if val:
            source = RemoteArchive(client, args.val_url)
            jobs.append((source, args.index_dir / "val.json", 0, source.size, source.size,
                         "val", val, args,
                         512 if args.header_only else args.val_chunk_mib * 1024 * 1024))
        found = {}
        downloaded = existing = completed = 0
        errors = []
        executor = ThreadPoolExecutor(max_workers=args.workers)
        pending = {executor.submit(process_group, *job) for job in jobs}
        last_progress = time.monotonic()
        try:
            while pending:
                done, pending = wait(pending, timeout=10, return_when=FIRST_COMPLETED)
                for future in done:
                    completed += 1
                    try:
                        images, new, old = future.result()
                        if set(images).intersection(found):
                            raise ValueError("The same image appeared in more than one archive partition.")
                        found.update(images)
                        downloaded += new
                        existing += old
                    except Exception as error:
                        errors.append(str(error))
                        print(f"Group failed; rerun will reuse saved progress: {error}", file=sys.stderr, flush=True)
                if done or time.monotonic() - last_progress >= 20:
                    print(f"Groups {completed}/{len(jobs)}; images {len(found)}/{len(names)}; "
                          f"HTTP requests {client.requests}; received {client.bytes / 1024**2:.1f} MiB", flush=True)
                    last_progress = time.monotonic()
        except BaseException:
            client.stop.set()
            raise
        finally:
            executor.shutdown(wait=True, cancel_futures=True)
        missing = sorted(set(names) - set(found))
        report = {
            "mode": "index_only" if args.index_only else "download",
            "requested_images": len(names), "completed_images": len(found),
            "downloaded_images": downloaded, "existing_images": existing,
            "selected_image_bytes": sum(found.values()), "http_requests": client.requests,
            "received_bytes": client.bytes, "missing_images": missing, "errors": errors,
        }
        atomic_write(args.index_dir / "last_run.json", json.dumps(report, indent=2).encode("utf-8"))
        print(f"Selected image bytes: {sum(found.values()) / 1024**3:.3f} GiB")
        print(f"Report: {args.index_dir / 'last_run.json'}")
        if missing or errors:
            print(f"Incomplete: {len(missing)} images; first missing paths: {missing[:10]}", file=sys.stderr)
            return 1
        action = "indexed" if args.index_only else "downloaded or verified"
        print(f"Complete: {len(names)} images {action}.")
        return 0
    
    
    def main() -> int:
        data = Path(__file__).resolve().parent
    ✓ • 0ms

## Activity

    $ python - <<'PY'
        from pathlib import Path
        import json, tarfile
        from collections import Counter
        root=Path('.')
        needed=(root/'transfer_lists/ocl_non_imagenet.txt').read_text().splitlines()
        missing=[x for x in needed if not (root/x).is_file()]
        print('missing',dict(Counter(x.split('/')[0] for x in missing)))
        with tarfile.open('from_web.tgz') as t:
            files={m.name:m.size for m in t if m.isfile()}
        print('web_archive_count',len(files))
        print('web_archive_first',list(files.items())[:4])
        print('missing_in_archive',sum(x in files or './'+x in files for x in missing))
        urls=json.loads(Path('resources/url_to_filename.json').read_text())
        print('urls_type',type(urls).__name__,'count',len(urls))
        print('urls_example', list(urls.items())[:2])
        r=json.loads(Path('web_download_failures.json').read_text())
        print('previous_web_summary', {k:v for k,v in r.items() if not isinstance(v,list)})
        print('temporary_jobs',[(str(p),list(q.name for q in p.iterdir())[:8]) for p in Path('/tmp').glob('ocl-range-live-*') if p.is_dir()])
        PY
    missing {'from_web': 269}
    web_archive_count 1962
    web_archive_first [('from_web/train_0278.jpg', 41686), ('from_web/val_1386.jpg', 55278), ('from_web/train_1648.jpg', 14521), ('from_web/train_1147.jpg', 337701)]
    missing_in_archive 0
    urls_type list count 3422
    Traceback (most recent call last):
      File "<stdin>", line 15, in <module>
    AttributeError: 'list' object has no attribute 'items'
    ✗ (1) • 4.39s

## Activity

    $ ps -eo pid,ppid,etime,comm,args --width 200
        PID    PPID     ELAPSED COMMAND         COMMAND
          1       0  1-23:42:41 systemd         /sbin/init
          2       1  1-23:42:41 init-systemd(Ub /init
          8       2  1-23:42:41 init            plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
         59       1  1-23:42:40 systemd-journal /usr/lib/systemd/systemd-journald
        107       1  1-23:42:40 systemd-udevd   /usr/lib/systemd/systemd-udevd
        122       1  1-23:42:40 snapfuse        snapfuse /var/lib/snapd/snaps/astral-uv_1773.snap /snap/astral-uv/1773 -o ro,nodev,allow_other,suid
        123       1  1-23:42:40 snapfuse        snapfuse /var/lib/snapd/snaps/core24_1643.snap /snap/core24/1643 -o ro,nodev,allow_other,suid
        124       1  1-23:42:40 snapfuse        snapfuse /var/lib/snapd/snaps/astral-uv_1781.snap /snap/astral-uv/1781 -o ro,nodev,allow_other,suid
        133       1  1-23:42:40 snapfuse        snapfuse /var/lib/snapd/snaps/core24_2124.snap /snap/core24/2124 -o ro,nodev,allow_other,suid
        137       1  1-23:42:40 snapfuse        snapfuse /var/lib/snapd/snaps/snapd_27738.snap /snap/snapd/27738 -o ro,nodev,allow_other,suid
        142       1  1-23:42:40 snapfuse        snapfuse /var/lib/snapd/snaps/snapd_28254.snap /snap/snapd/28254 -o ro,nodev,allow_other,suid
        231       1  1-23:42:40 systemd-timesyn /usr/lib/systemd/systemd-timesyncd
        238       1  1-23:42:40 cron            /usr/sbin/cron -f -P
        239       1  1-23:42:40 dbus-daemon     @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
        245       1  1-23:42:40 snapd           /snap/snapd/current/usr/lib/snapd/snapd
        246       1  1-23:42:40 systemd-logind  /usr/lib/systemd/systemd-logind
        248       1  1-23:42:40 udisksd         /usr/libexec/udisks2/udisksd
        258       1  1-23:42:40 agetty          /sbin/agetty -o -p -- \u --noclear --keep-baud - 115200,38400,9600 vt220
        271       1  1-23:42:40 rsyslogd        /usr/sbin/rsyslogd -n -iNONE
        278       1  1-23:42:40 containerd      /usr/bin/containerd
        282       1  1-23:42:40 agetty          /sbin/agetty -o -p -- \u --noclear - linux
        288       1  1-23:42:40 unattended-upgr /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
        302       1  1-23:42:40 polkitd         /usr/lib/polkit-1/polkitd --no-debug
        340       1  1-23:42:39 dockerd         /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
        651       2  1-23:42:38 login           /bin/login -f
        696       1  1-23:42:37 systemd         /usr/lib/systemd/systemd --user
        697     696  1-23:42:37 (sd-pam)        (sd-pam)
        721     651  1-23:42:37 bash            -bash
        919       2  1-23:42:37 SessionLeader   /init
        920     919  1-23:42:37 Relay(926)      /init
        926     920  1-23:42:37 sh              sh -c "$VSCODE_WSL_EXT_LOCATION/scripts/wslServer.sh" 6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1 stable code-server .vscode-server --host=127.0.0.1 --port=0 -
        936     926  1-23:42:37 sh              sh /mnt/c/Users/ASUS/.vscode/extensions/ms-vscode-remote.remote-wsl-0.104.3/scripts/wslServer.sh 6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1 stable code-server
        957     936  1-23:42:37 sh              sh /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/bin/code-server --host=127.0.0.1 --port=0 --connection-token=3074471356-211409858
        962     957  1-23:42:37 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/ser
       1044     962  1-23:42:36 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/boo
       1316     962  1-23:42:33 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node --dns-result-order=ipv4first /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3
       1322     962  1-23:42:33 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/boo
       1347    1322  1-23:42:31 copilot-runtime /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node_modules/@github/copilot-sdk-linux-x64/prebuilds/linux-x64/copilot-runtime --hea
       1381     962  1-23:42:31 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/boo
       1682    1381  1-23:42:27 bash            /bin/bash --init-file /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/vs/workbench/contrib/terminal/common/scripts/shellIntegrat
      34222    1316  1-19:55:14 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/extensi
      34443     696  1-19:51:16 dbus-daemon     /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
      34446     696  1-19:51:16 xdg-desktop-por /usr/libexec/xdg-desktop-portal
      34457     696  1-19:51:16 xdg-document-po /usr/libexec/xdg-document-portal
      34466     696  1-19:51:16 xdg-permission- /usr/libexec/xdg-permission-store
      34475   34457  1-19:51:16 fusermount3     fusermount3 -o rw,nosuid,nodev,fsname=portal,auto_unmount,subtype=portal -- /run/user/1000/doc
      34486     696  1-19:51:15 at-spi-bus-laun /usr/libexec/at-spi-bus-launcher
      34493   34486  1-19:51:15 dbus-daemon     /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 11 --address=unix:path=/run/user/1000/at-spi/bus
      34494     696  1-19:51:15 gvfsd           /usr/libexec/gvfsd
      34506     696  1-19:51:15 at-spi2-registr /usr/libexec/at-spi2-registryd --use-gnome-session
      34569     920  1-19:51:10 codex           /home/linfu/.codex/packages/app-server-daemon/releases/0.163.0-x86_64-unknown-linux-musl/bin/codex app-server --listen unix:// --analytics-default-enabled -
      34679     920  1-19:51:09 codex           /home/linfu/.codex/packages/app-server-daemon/releases/0.163.0-x86_64-unknown-linux-musl/bin/codex app-server daemon pid-update-loop
      41239   34569  1-18:55:32 codex-code-mode /home/linfu/.codex/packages/app-server-daemon/releases/0.163.0-x86_64-unknown-linux-musl/bin/codex-code-mode-host
      52594    1316  1-18:18:26 pet             /home/linfu/.vscode-server/extensions/ms-python.vscode-python-envs-1.40.0-linux-x64/python-env-tools/bin/pet server
      52702    1381  1-18:18:25 bash            /bin/bash --init-file /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/vs/workbench/contrib/terminal/common/scripts/shellIntegrat
      53000    1316  1-18:18:19 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/extensions/ms-python.vscode-pylance-2026.4.1/dist/se
      53453    1316  1-18:10:58 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/extensi
     665735       1    15:09:15 tailscaled      /usr/sbin/tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/run/tailscale/tailscaled.sock --port=41641
     728934       1    12:33:19 Relay(728940)   /init
     728989       1    12:33:17 Relay(728990)   /init
     769238    1381    09:45:41 bash            /bin/bash --init-file /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/vs/workbench/contrib/terminal/common/scripts/shellIntegrat
     786264  769238    08:44:46 MainThread      node /home/linfu/.nvm/versions/node/v24.18.0/bin/codex
     786271  786264    08:44:46 codex           /home/linfu/.nvm/versions/node/v24.18.0/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex
     814178       2    04:14:59 SessionLeader   /init
     814180  814178    04:14:59 Relay(814184)   /init
     814184  814180    04:14:59 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node -e const net = require('net'); process.stdin.pause(); const client = net.create
     814193       2    04:14:54 SessionLeader   /init
     814195  814193    04:14:54 Relay(814196)   /init
     814196  814195    04:14:54 MainThread      /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/node -e const net = require('net'); process.stdin.pause(); const client = net.create
     824874    1682    02:41:03 MainThread      node /home/linfu/.nvm/versions/node/v24.18.0/bin/codex
     824881  824874    02:41:02 codex           /home/linfu/.nvm/versions/node/v24.18.0/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex
     840534  824881    01:52:13 cmd.exe         [cmd.exe] <defunct>
     840947    1381    01:50:56 bash            /bin/bash --init-file /home/linfu/.vscode-server/bin/6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1/out/vs/workbench/contrib/terminal/common/scripts/shellIntegrat
     854921  840947    01:11:02 MainThread      node /home/linfu/.nvm/versions/node/v24.18.0/bin/codex
     854938  854921    01:11:01 codex           /home/linfu/.nvm/versions/node/v24.18.0/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex
     865550       1       45:45 systemd-resolve /usr/lib/systemd/systemd-resolved
     877161       1       03:09 wsl-pro-service /usr/libexec/wsl-pro-service
     878185   34569       00:00 ps              ps -eo pid,ppid,etime,comm,args --width 200
    ✓ • 0ms

## Activity

    • Context compacted

## Assistant

我先核对已有图片、下载缓存和后台进程，再从缺失部分继续，避免重复下载；随后会按 `Test.md` 校验数据目录和图片完整性。

## Activity

    $ pwd
    /home/linfu/src/Test/ObjectConceptLearning/data
    ✓ • 16ms

## Activity

    $ git status --short
     M .gitignore
     M README.md
     M data/download_web_images.py
     M data/prepare_data.sh
    ?? Test.md
    ?? aPY/
    ?? clip_dataset.py
    ?? clip_inference.py
    ?? data/download_imagenet_subset.py
    ?? data/extract_imagenet_subset.py
    ?? data/from_web.tgz
    ?? data/from_web.tgz:Zone.Identifier
    ?? data/resources/OCL_annot_test.pkl
    ?? data/resources/OCL_annot_train.pkl
    ?? data/resources/OCL_annot_val.pkl
    ?? data/transfer_lists/
    ?? data/web_download_failures.json
    ?? docs/clip_inference.md
    ?? requirements-clip.txt
    ?? setup_clip_gpu.sh
    ?? tests/
    ✓ • 27ms

## Activity

    $ rg --files -g AGENTS.md -g Test.md -g test.md -g '*imagenet*' -g '*selection*' -g '*download*' -g '*audit*' . .. /tmp
    rg: /tmp/codex-daemon-1000: Permission denied (os error 13)
    rg: /tmp/systemd-private-3ac0315509744c32aee650f3963933e0-polkit.service-wQiJfV: Permission denied (os error 13)
    rg: /tmp/systemd-private-3ac0315509744c32aee650f3963933e0-systemd-timesyncd.service-Eb6Xj6: Permission denied (os error 13)
    rg: /tmp/systemd-private-3ac0315509744c32aee650f3963933e0-systemd-logind.service-4lJVuO: Permission denied (os error 13)
    rg: /tmp/systemd-private-3ac0315509744c32aee650f3963933e0-wsl-pro.service-69qeJQ: Permission denied (os error 13)
    rg: /tmp/snap-private-tmp: Permission denied (os error 13)
    rg: /tmp/systemd-private-3ac0315509744c32aee650f3963933e0-systemd-resolved.service-rkfWK3: Permission denied (os error 13)
    ../Test.md
    ../tests/test_download_web_images.py
    ../tests/test_clip_category_selection.py
    /tmp/ocl-imagenet-val-header-20261023.bin
    ../data/download_web_images.py
    ../data/web_download_failures.json
    ../data/extract_imagenet_subset.py
    ../data/__pycache__/download_web_images.cpython-312.pyc
    ../data/__pycache__/download_imagenet_subset.cpython-314.pyc
    ../data/__pycache__/extract_imagenet_subset.cpython-314.pyc
    ../data/__pycache__/extract_imagenet_subset.cpython-312.pyc
    ./extract_imagenet_subset.py
    ./__pycache__/download_web_images.cpython-312.pyc
    ./__pycache__/download_imagenet_subset.cpython-314.pyc
    ./__pycache__/extract_imagenet_subset.cpython-314.pyc
    ./__pycache__/extract_imagenet_subset.cpython-312.pyc
    ./download_web_images.py
    ../data/transfer_lists/imagenet_required.txt
    ../data/transfer_lists/selection.json
    ../data/transfer_lists/ocl_non_imagenet.txt
    ./download_imagenet_subset.py
    ./transfer_lists/imagenet_required.txt
    ./transfer_lists/selection.json
    ./transfer_lists/ocl_non_imagenet.txt
    ./web_download_failures.json
    ../data/download_imagenet_subset.py
    ✗ (2) • 438ms

## Activity

    $ sed -n '261,560p' download_imagenet_subset.py
    
    
    def run(args) -> int:
        names = load_manifest(args.manifest)
        if args.limit is not None:
            names = names[:args.limit]
        train = {}
        val = {}
        for name in names:
            parts = PurePosixPath(name).parts
            if parts[0] == "train":
                train.setdefault(parts[1] + ".tar", {})[parts[2]] = name
            else:
                val[parts[1]] = name
        client = RangeClient(args.timeout, args.retries)
        jobs = []
        if train:
            source = RemoteArchive(client, args.train_url)
            print(f"Indexing outer training tar for {len(train)} required classes...", flush=True)
            outer = index_members(
                source,
                args.index_dir / "train_outer.json",
                0,
                source.size,
                source.size,
                "classes",
                set(train),
                512,
            )
            missing_classes = sorted(set(train) - set(outer))
            if missing_classes:
                raise ValueError(f"Classes missing from training archive: {missing_classes}")
            class_bytes = sum(outer[name]["size"] for name in train)
            print(f"Required training class archives total {class_bytes / 1024**3:.2f} GiB.", flush=True)
            if args.header_only:
                print("Indexing headers only: low bandwidth, but many HTTP requests.", flush=True)
            else:
                print("Read-ahead indexing can transfer much of this data without storing it.", flush=True)
            for name, requested in sorted(train.items()):
                entry = outer[name]
                jobs.append((source, args.index_dir / "train" / f"{name}.json",
                             entry["offset"], entry["offset"] + entry["size"],
                             entry["offset"] + entry["size"], "train", requested, args,
                             512 if args.header_only else args.train_chunk_mib * 1024 * 1024))
        if val:
            source = RemoteArchive(client, args.val_url)
            jobs.append((source, args.index_dir / "val.json", 0, source.size, source.size,
                         "val", val, args,
                         512 if args.header_only else args.val_chunk_mib * 1024 * 1024))
        found = {}
        downloaded = existing = completed = 0
        errors = []
        executor = ThreadPoolExecutor(max_workers=args.workers)
        pending = {executor.submit(process_group, *job) for job in jobs}
        last_progress = time.monotonic()
        try:
            while pending:
                done, pending = wait(pending, timeout=10, return_when=FIRST_COMPLETED)
                for future in done:
                    completed += 1
                    try:
                        images, new, old = future.result()
                        if set(images).intersection(found):
                            raise ValueError("The same image appeared in more than one archive partition.")
                        found.update(images)
                        downloaded += new
                        existing += old
                    except Exception as error:
                        errors.append(str(error))
                        print(f"Group failed; rerun will reuse saved progress: {error}", file=sys.stderr, flush=True)
                if done or time.monotonic() - last_progress >= 20:
                    print(f"Groups {completed}/{len(jobs)}; images {len(found)}/{len(names)}; "
                          f"HTTP requests {client.requests}; received {client.bytes / 1024**2:.1f} MiB", flush=True)
                    last_progress = time.monotonic()
        except BaseException:
            client.stop.set()
            raise
        finally:
            executor.shutdown(wait=True, cancel_futures=True)
        missing = sorted(set(names) - set(found))
        report = {
            "mode": "index_only" if args.index_only else "download",
            "requested_images": len(names), "completed_images": len(found),
            "downloaded_images": downloaded, "existing_images": existing,
            "selected_image_bytes": sum(found.values()), "http_requests": client.requests,
            "received_bytes": client.bytes, "missing_images": missing, "errors": errors,
        }
        atomic_write(args.index_dir / "last_run.json", json.dumps(report, indent=2).encode("utf-8"))
        print(f"Selected image bytes: {sum(found.values()) / 1024**3:.3f} GiB")
        print(f"Report: {args.index_dir / 'last_run.json'}")
        if missing or errors:
            print(f"Incomplete: {len(missing)} images; first missing paths: {missing[:10]}", file=sys.stderr)
            return 1
        action = "indexed" if args.index_only else "downloaded or verified"
        print(f"Complete: {len(names)} images {action}.")
        return 0
    
    
    def main() -> int:
        data = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--manifest", type=Path, default=data / "transfer_lists" / "imagenet_required.txt")
        parser.add_argument("--output-dir", type=Path, default=data / "ImageNet")
        parser.add_argument("--index-dir", type=Path, default=data / "imagenet_index")
        parser.add_argument("--workers", type=int, default=8)
        parser.add_argument("--timeout", type=float, default=30)
        parser.add_argument("--retries", type=int, default=4)
        parser.add_argument("--train-chunk-mib", type=int, default=8)
        parser.add_argument("--val-chunk-mib", type=int, default=64)
        parser.add_argument("--limit", type=int, help="Use only the first N manifest entries for a smoke test")
        parser.add_argument("--index-only", action="store_true", help="Build reusable offsets without downloading images")
        parser.add_argument(
            "--header-only", action="store_true",
            help="Index with 512-byte header reads; less bandwidth, many more HTTP requests",
        )
        parser.add_argument("--train-url", default=f"{BASE_URL}/ILSVRC2012_img_train.tar")
        parser.add_argument("--val-url", default=f"{BASE_URL}/ILSVRC2012_img_val.tar")
        args = parser.parse_args()
        if (
            not 1 <= args.workers <= 64
            or args.timeout <= 0
            or args.retries < 0
            or args.train_chunk_mib < 1
            or args.val_chunk_mib < 1
        ):
            parser.error("Use 1..64 workers, a positive timeout/chunk size, and non-negative retries.")
        if args.limit is not None and args.limit < 1:
            parser.error("--limit must be positive")
        for name in ("manifest", "output_dir", "index_dir"):
            setattr(args, name, getattr(args, name).expanduser().resolve())
        return run(args)
    
    
    if __name__ == "__main__":
        try:
            raise SystemExit(main())
        except KeyboardInterrupt:
            print("Interrupted. Rerun the same command to reuse cached indexes and complete images.", file=sys.stderr)
            raise SystemExit(130)
        except (OSError, ValueError, RuntimeError, tarfile.TarError) as error:
            print(f"Error: {error}", file=sys.stderr)
            raise SystemExit(1)
    ✓ • 73ms

## Activity

    $ cat ../Test.md transfer_lists/selection.json ../clip_dataset.py
    # OCL
    
    Implement an OCL-based object category classification inference experiment.
    
    Set up your own Python environment by downloading and installing **Miniforge / uv / Python**, and then begin the experiment.
    
    ## References
    
    1. OCL paper: **Beyond Object Recognition: A New Benchmark towards Object Concept Learning**
    
    2. **OCL dataset preparation**
    
       - The official data preparation scripts are provided in the OCL GitHub repository: [https://github.com/silicx/ObjectConceptLearning/tree/main/data](https://github.com/silicx/ObjectConceptLearning/tree/main/data)
       - Please read and understand the provided scripts and dataset structure before implementing the DataLoader.
       - In particular, the repository provides `prepare_data.sh`, `download_web_images.py`, and the `resources` directory for dataset preparation.
       - After downloading the dataset, inspect the image data and annotation files carefully and understand how **category**, **attribute**, and **affordance** annotations are represented.
    
    3. Download and prepare the required test data using the scripts provided in the official OCL GitHub repository.
    
    4. CLIP paper/repository: **Contrastive Language-Image Pre-Training**
    
       [https://github.com/openai/CLIP](https://github.com/openai/CLIP)
    
    ## Step 1: Prepare the DataLoader
    
    1. Implement a custom dataset class by inheriting from PyTorch's native `Dataset`:
    
       - Load the dataset and corresponding annotations;
       - Filter the data by sorting category labels according to the number of samples, and keep only the **10 categories with the largest number of samples**;
       - Perform image preprocessing and text tokenization.
    
    2. Create a test data loader using PyTorch's native `DataLoader`:
    
       - Set `batch_size = 4`.
    
    ## Step 2: Prepare the CLIP Model
    
    1. Load a pretrained CLIP model using the available API.
    
    ## Step 3: Inference and Evaluation
    
    1. Instantiate the dataset and model, and move the model to GPU, including:
    
       - `load_dataset`
       - `load_model`
       - `model.to(device)`
    
    2. Set the model to inference mode and freeze all model parameters:
    
       - Iterate over all model parameters and set gradient computation to `False`.
    
    3. Iterate over the test set and perform inference:
    
       - Each image may contain multiple objects.
       - Compute the cosine similarity between each object and the candidate **category** labels.
       - Use the cosine similarity scores for ranking.
       - Compute the model's **Top-k accuracy**.
       - Perform forward inference batch by batch and report the average accuracy over the entire test set.
    
    4. Evaluate the prediction performance for **attribute** and **affordance** labels using the **mAP (mean Average Precision)** metric.
    {
      "selection_splits": [
        "train",
        "val",
        "test"
      ],
      "count_unit": "object_instance",
      "selected_categories": {
        "dog": 16171,
        "bird": 13961,
        "sheep": 13821,
        "car": 11511,
        "motorcycle": 8519,
        "apple": 8382,
        "cattle": 8379,
        "broccoli": 8333,
        "truck": 7769,
        "elephant": 7032
      },
      "num_selected_objects_before_box_filter": 103878,
      "num_selected_images": 35633,
      "images_by_source": {
        "COCO": 25067,
        "ImageNet": 7924,
        "aPY": 1168,
        "from_web": 1474
      },
      "manifest_roots": {
        "ocl_non_imagenet.txt": "data/",
        "imagenet_required.txt": "data/ImageNet/"
      },
      "note": "Manifests contain every selected image path, without filtering by local availability."
    }
    """Object crops and candidate-label tokens for the OCL CLIP experiment."""
    
    from __future__ import annotations
    
    import json
    import math
    import pickle
    from collections import Counter
    from dataclasses import dataclass
    from pathlib import Path
    from typing import TYPE_CHECKING
    
    import torch
    from PIL import Image
    from torch.utils.data import DataLoader, Dataset
    
    if TYPE_CHECKING:
        from transformers import CLIPProcessor
    
    
    NUM_CATEGORIES = 10
    BATCH_SIZE = 4
    
    
    @dataclass(frozen=True)
    class ObjectInstance:
        image_name: str
        object_index: int
        category_id: int
        box: tuple[float, float, float, float] | None
        attribute_ids: tuple[int, ...]
        affordance_ids: tuple[int, ...]
    
    
    class OCLClipDataset(Dataset):
        """One sample per annotated object in the ten most frequent categories."""
    
        def __init__(
            self,
            data_root: str | Path,
            processor: CLIPProcessor,
        ) -> None:
            self.data_root = Path(data_root).expanduser().resolve()
            self.image_processor = processor.image_processor
            resources = self.data_root / "resources"
    
            def load_classes(name: str) -> list:
                with (resources / f"OCL_class_{name}.json").open(encoding="utf-8") as handle:
                    return json.load(handle)
    
            object_classes = load_classes("object")
            self.attribute_classes = load_classes("attribute")
            self.affordance_classes = load_classes("affordance")
            annotations = []
            # Merge all supplied annotations into one evaluation dataset.
            for filename in ("OCL_annot_train.pkl", "OCL_annot_val.pkl", "OCL_annot_test.pkl"):
                annotation_path = resources / filename
                if not annotation_path.is_file():
                    raise FileNotFoundError(
                        f"Missing {annotation_path}. Extract data/resources/OCL_annot.tgz first."
                    )
                with annotation_path.open("rb") as handle:
                    annotations.extend(pickle.load(handle))
    
            counts = Counter(obj["obj"] for image in annotations for obj in image["objects"])
            unknown = set(counts) - set(object_classes)
            if unknown:
                raise ValueError(f"Categories missing from OCL_class_object.json: {sorted(unknown)}")
            if len(counts) < NUM_CATEGORIES:
                raise ValueError(f"Need {NUM_CATEGORIES} categories; found {len(counts)}.")
            # Alphabetical tie-breaking makes class IDs independent of annotation order.
            ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
            self.selection_category_counts = dict(ranked[:NUM_CATEGORIES])
            self.category_classes = list(self.selection_category_counts)
            category_to_id = {name: index for index, name in enumerate(self.category_classes)}
    
            self.instances = [
                ObjectInstance(
                    image_name=image["name"],
                    object_index=object_index,
                    category_id=category_to_id[obj["obj"]],
                    box=tuple(obj["box"]) if "box" in obj else None,
                    attribute_ids=tuple(obj["attr"]),
                    affordance_ids=tuple(obj["aff"]),
                )
                for image in annotations
                for object_index, obj in enumerate(image["objects"])
                if obj["obj"] in category_to_id
            ]
            self.num_selected_objects = len(self.instances)
            self.excluded_objects = []
            valid_instances = []
            for instance in self.instances:
                box = instance.box
                if box is not None and (
                    len(box) != 4
                    or not all(math.isfinite(value) for value in box)
                    or box[2] <= box[0]
                    or box[3] <= box[1]
                ):
                    self.excluded_objects.append(
                        {
                            "image_name": instance.image_name,
                            "object_index": instance.object_index,
                            "category": self.category_classes[instance.category_id],
                            "box": repr(box),
                            "reason": "non-finite, malformed or non-positive-area box",
                        }
                    )
                else:
                    valid_instances.append(instance)
            self.instances = valid_instances
            if not self.instances:
                raise ValueError("No usable objects from the selected categories.")
            evaluation_counts = Counter(instance.category_id for instance in self.instances)
            self.evaluation_category_counts = {
                name: evaluation_counts[index] for index, name in enumerate(self.category_classes)
            }
            self.num_images = len({instance.image_name for instance in self.instances})
    
            self.prompts = {
                "category": [f"a photo of a {name}." for name in self.category_classes],
                "attribute": [
                    f"a photo of an object that is {name}." for name in self.attribute_classes
                ],
                # Preserve original IDs: several affordances share a verb but differ in meaning.
                "affordance": [self._affordance_prompt(label) for label in self.affordance_classes],
            }
            self.text_inputs = {
                name: dict(
                    processor.tokenizer(
                        prompts,
                        padding=True,
                        truncation=True,
                        max_length=processor.tokenizer.model_max_length,
                        return_tensors="pt",
                    )
                )
                for name, prompts in self.prompts.items()
            }
    
        @staticmethod
        def _affordance_prompt(label: dict) -> str:
            action = label["word"][0]
            definition = " ".join(label["define"].split())
            prompt = f"an object that enables the action {action}"
            return f"{prompt}: {definition}." if definition else f"{prompt}."
    
        @staticmethod
        def _multi_hot(indices: tuple[int, ...], size: int) -> torch.Tensor:
            if any(index < 0 or index >= size for index in indices):
                raise ValueError(f"Label IDs outside [0, {size}): {indices}")
            target = torch.zeros(size, dtype=torch.float32)
            if indices:
                target[list(indices)] = 1.0
            return target
    
        @staticmethod
        def _crop_object(image: Image.Image, instance: ObjectInstance) -> Image.Image:
            width, height = image.size
            box = instance.box if instance.box is not None else (0, 0, width, height)
            if len(box) != 4 or not all(math.isfinite(value) for value in box):
                raise ValueError(
                    f"Invalid box in {instance.image_name}, object {instance.object_index}: {box}"
                )
            # OCL already stores xyxy coordinates, including for its COCO images.
            left, top, right, bottom = box
            left, top = max(0, left), max(0, top)
            right, bottom = min(width, right), min(height, bottom)
            if right <= left or bottom <= top:
                raise ValueError(
                    f"Empty box in {instance.image_name}, object {instance.object_index}: {box}"
                )
            crop_box = (math.floor(left), math.floor(top), math.ceil(right), math.ceil(bottom))
            return image.crop(crop_box).convert("RGB")
    
        def __len__(self) -> int:
            return len(self.instances)
    
        def __getitem__(self, index: int) -> dict:
            instance = self.instances[index]
            image_path = self.data_root / instance.image_name
            if not image_path.is_file():
                raise FileNotFoundError(f"Missing OCL image: {image_path}")
            with Image.open(image_path) as image:
                crop = self._crop_object(image, instance)
            pixel_values = self.image_processor(images=crop, return_tensors="pt")["pixel_values"][0]
            return {
                "pixel_values": pixel_values,
                "category_id": instance.category_id,
                "attributes": self._multi_hot(instance.attribute_ids, len(self.attribute_classes)),
                "affordances": self._multi_hot(instance.affordance_ids, len(self.affordance_classes)),
                "image_name": instance.image_name,
                "object_index": instance.object_index,
            }
    
    
    def load_dataset(
        data_root: str | Path,
        processor: CLIPProcessor,
        num_workers: int = 4,
        pin_memory: bool = True,
    ) -> tuple[OCLClipDataset, DataLoader]:
        if num_workers < 0:
            raise ValueError("num_workers must be non-negative")
        dataset = OCLClipDataset(data_root, processor)
        loader = DataLoader(
            dataset,
            batch_size=BATCH_SIZE,
            shuffle=False,
            drop_last=False,
            num_workers=num_workers,
            pin_memory=pin_memory,
            persistent_workers=num_workers > 0,
        )
        return dataset, loader
    ✓ • 92ms

## Activity

    $ cat download_web_images.py prepare_data.sh
    """Resume OCL web-image downloads and report unavailable images."""
    
    import argparse
    import json
    import tempfile
    import time
    from pathlib import Path
    
    import requests
    from PIL import Image
    from tqdm import tqdm
    
    
    IMAGE_ERRORS = (OSError, ValueError, SyntaxError, Image.DecompressionBombError)
    
    
    def validate_image(path):
        with Image.open(path) as image:
            image.load()
    
    
    def download_image(session, url, destination, timeout=20, retries=2):
        """Return a status and failed attempts, preserving existing files on failure."""
        destination = Path(destination)
        if destination.is_file():
            try:
                validate_image(destination)
                return "skipped", []
            except IMAGE_ERRORS:
                pass
    
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Many old HTTP image URLs now require HTTPS. Keep HTTP as a fallback.
        candidates = ["https://" + url[7:], url] if url.startswith("http://") else [url]
        errors = []
        for candidate in candidates:
            for attempt in range(retries + 1):
                temporary = None
                try:
                    with session.get(
                        candidate, stream=True, timeout=(min(10, timeout), timeout)
                    ) as response:
                        response.raise_for_status()
                        with tempfile.NamedTemporaryFile(
                            dir=destination.parent,
                            prefix="." + destination.name + ".",
                            suffix=".part",
                            delete=False,
                        ) as handle:
                            temporary = Path(handle.name)
                            for chunk in response.iter_content(chunk_size=65536):
                                handle.write(chunk)
                    validate_image(temporary)
                    # Publish only a complete, decodable image, on the same filesystem.
                    temporary.replace(destination)
                    return "downloaded", errors
                except (requests.RequestException,) + IMAGE_ERRORS as error:
                    errors.append(
                        {"url": candidate, "attempt": attempt + 1, "error": str(error)}
                    )
                    retryable = isinstance(error, requests.RequestException)
                    if isinstance(error, requests.HTTPError):
                        status = error.response.status_code
                        retryable = status in (408, 429) or 500 <= status < 600
                    if not retryable or attempt == retries:
                        break
                    time.sleep(min(2 ** attempt, 5))
                finally:
                    if temporary is not None:
                        temporary.unlink(missing_ok=True)
        return "failed", errors
    
    
    def main(argv=None):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument(
            "--data-root", type=Path, default=Path(__file__).resolve().parent
        )
        parser.add_argument("--timeout", type=float, default=20, help="Socket timeout in seconds")
        parser.add_argument("--retries", type=int, default=2, help="Extra attempts per URL")
        parser.add_argument("--limit", type=int, help="Process only the first N entries")
        args = parser.parse_args(argv)
        if args.timeout <= 0 or args.retries < 0 or (args.limit is not None and args.limit <= 0):
            parser.error("timeout and limit must be positive; retries must be non-negative")
    
        root = args.data_root.expanduser().resolve()
        with (root / "resources" / "url_to_filename.json").open(encoding="utf-8") as handle:
            entries = json.load(handle)
        entries = entries[:args.limit]
        counts = {"downloaded": 0, "skipped": 0, "failed": 0}
        failures = []
        interrupted = False
        with requests.Session() as session:
            session.headers.update(
                {"User-Agent": "Mozilla/5.0 (compatible; OCL-image-downloader/1.0)"}
            )
            try:
                with tqdm(entries, desc="Web images", unit="image", ncols=100) as progress:
                    for url, name in progress:
                        status, errors = download_image(
                            session, url, root / name, timeout=args.timeout, retries=args.retries
                        )
                        counts[status] += 1
                        if status == "failed":
                            failures.append({"url": url, "name": name, "attempts": errors})
                            tqdm.write("Failed {}: {}".format(name, errors[-1]["error"]))
                        progress.set_postfix(counts, refresh=False)
            except KeyboardInterrupt:
                interrupted = True
    
        report = {
            "requested": len(entries),
            **counts,
            "pending": len(entries) - sum(counts.values()),
            "interrupted": interrupted,
            "failures": failures,
        }
        report_path = root / "web_download_failures.json"
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(
            "Downloaded: {downloaded}; already valid: {skipped}; failed: {failed}; "
            "pending: {pending}.".format(**report)
        )
        print("Report: {}. Rerun to retry missing or invalid images.".format(report_path))
        return 130 if interrupted else (1 if failures else 0)
    
    
    if __name__ == "__main__":
        raise SystemExit(main())
    # Extract annotation files
    
    cd resources;
    tar -xzf OCL_annot.tgz;
    cd ..;
    
    
    
    # Download and extract image data
    
    echo "Downloading SUN-attribute";
    mkdir -p SUN;
    cd SUN;
    if [ ! -e "SUNAttributeDB_Images.tar.gz" ]; then
        wget https://cs.brown.edu/~gmpatter/Attributes/SUNAttributeDB_Images.tar.gz;
    fi
    if [ ! -e "images" ]; then
        tar -xzf SUNAttributeDB_Images.tar.gz;
    fi
    cd ..;
    
    
    echo "Downloading aPY";
    mkdir -p aPY;
    cd aPY;
    if [ ! -e "ayahoo_test_images.tar.gz" ]; then
        wget http://vision.cs.uiuc.edu/attributes/ayahoo_test_images.tar.gz;
    fi
    if [ ! -e "VOCtrainval_14-Jul-2008.tar" ]; then
        wget http://host.robots.ox.ac.uk/pascal/VOC/voc2008/VOCtrainval_14-Jul-2008.tar;
    fi
    if [ ! -e "ayahoo_test_images" ]; then
    tar -xzf ayahoo_test_images.tar.gz;
    tar -xf VOCtrainval_14-Jul-2008.tar;
    cd ..;
    fi
    
    echo "Downloading COCO";
    mkdir -p COCO;
    cd COCO;
    wget http://images.cocodataset.org/zips/train2014.zip;
    wget http://images.cocodataset.org/zips/val2014.zip;
    unzip train2014.zip;
    unzip val2014.zip;
    cd ..;
    
    
    # Prepare web image data
    tar -xf from_web.tgz
    python download_web_images.py
    ✓ • 85ms

## Activity

    $ sed -n '1,260p' download_imagenet_subset.py
    """Download selected ImageNet images using cached tar offsets and HTTP Range.
    
    The first index scan reads ahead to reduce request overhead. These temporary
    blocks can contain unselected images, but are never written to disk.
    """
    
    from __future__ import annotations
    
    import argparse
    from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
    import io
    import json
    import os
    from pathlib import Path, PurePosixPath
    import re
    import sys
    import tarfile
    import tempfile
    import threading
    import time
    
    import requests
    from PIL import Image
    
    from extract_imagenet_subset import load_manifest
    
    
    BASE_URL = "https://image-net.org/data/ILSVRC/2012"
    PATTERNS = {
        "classes": re.compile(r"n\d{8}\.tar"),
        "train": re.compile(r"n\d{8}_\d+\.JPEG"),
        "val": re.compile(r"ILSVRC2012_val_\d{8}\.JPEG"),
    }
    
    
    def atomic_write(path: Path, content: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=path.parent, prefix=f".{path.name}.", suffix=".part", delete=False
            ) as handle:
                temporary = Path(handle.name)
                handle.write(content)
            os.replace(temporary, path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    
    
    class RangeClient:
        def __init__(self, timeout: float, retries: int) -> None:
            self.timeout = timeout
            self.retries = retries
            self.local = threading.local()
            self.stop = threading.Event()
            self.lock = threading.Lock()
            self.requests = 0
            self.bytes = 0
    
        def fetch(self, url: str, start: int, end: int, identity: dict | None = None) -> tuple[bytes, dict]:
            if start < 0 or end < start:
                raise ValueError(f"Invalid byte range: {start}-{end}")
            if not hasattr(self.local, "session"):
                self.local.session = requests.Session()
            headers = {"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"}
            if identity:
                if identity.get("etag") and not identity["etag"].startswith("W/"):
                    headers["If-Match"] = identity["etag"]
                elif identity.get("last_modified"):
                    headers["If-Unmodified-Since"] = identity["last_modified"]
            for attempt in range(self.retries + 1):
                if self.stop.is_set():
                    raise InterruptedError("Download stopped")
                try:
                    with self.lock:
                        self.requests += 1
                    with self.local.session.get(
                        url, headers=headers, stream=True, timeout=(self.timeout, self.timeout)
                    ) as response:
                        if response.status_code == 429 or response.status_code >= 500:
                            response.raise_for_status()
                        if response.status_code != 206:
                            raise ValueError(
                                f"Expected HTTP 206 for {url}, got {response.status_code}. "
                                "Refusing a response that could download the entire archive."
                            )
                        match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", response.headers.get("Content-Range", ""))
                        if not match or (int(match[1]), int(match[2])) != (start, end):
                            raise ValueError("The server returned an incorrect Content-Range.")
                        metadata = {
                            "url": url,
                            "size": int(match[3]),
                            "etag": response.headers.get("ETag"),
                            "last_modified": response.headers.get("Last-Modified"),
                        }
                        if end >= metadata["size"]:
                            raise ValueError("The range extends beyond the archive.")
                        if identity and metadata != identity:
                            raise ValueError("The remote archive changed; rerun to rebuild its cached indexes.")
                        if response.headers.get("Content-Encoding", "identity") != "identity":
                            raise ValueError("Encoded HTTP responses cannot be used for tar offsets.")
                        chunks = []
                        received = 0
                        for chunk in response.iter_content(chunk_size=64 * 1024):
                            if self.stop.is_set():
                                raise InterruptedError("Download stopped")
                            received += len(chunk)
                            with self.lock:
                                self.bytes += len(chunk)
                            if received > end - start + 1:
                                raise ValueError("The server sent more bytes than requested.")
                            chunks.append(chunk)
                        if received != end - start + 1:
                            raise requests.exceptions.ChunkedEncodingError("Incomplete range response")
                        return b"".join(chunks), metadata
                except requests.RequestException as error:
                    if attempt == self.retries:
                        raise RuntimeError(f"Range request failed after retries: {error}") from error
                    if self.stop.wait(min(2 ** attempt, 8)):
                        raise InterruptedError("Download stopped") from error
            raise RuntimeError("Unreachable retry state")
    
    
    class RemoteArchive:
        def __init__(self, client: RangeClient, url: str) -> None:
            self.client = client
            self.first_header, self.identity = client.fetch(url, 0, 511)
            if not self.identity["etag"] and not self.identity["last_modified"]:
                raise ValueError("The archive needs an ETag or Last-Modified value for reliable cache reuse.")
            self.size = self.identity["size"]
    
        def read(self, offset: int, size: int) -> bytes:
            if size <= 0 or offset < 0 or offset + size > self.size:
                raise ValueError(f"Invalid archive read: offset={offset}, size={size}")
            if offset == 0 and size == 512:
                return self.first_header
            return self.client.fetch(
                self.identity["url"], offset, offset + size - 1, self.identity
            )[0]
    
    
    def parse_header(block: bytes) -> tarfile.TarInfo:
        member = tarfile.TarInfo.frombuf(block, "utf-8", "strict")
        if member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE, tarfile.DIRTYPE):
            raise ValueError(f"Unsupported tar header type for {member.name!r}: {member.type!r}")
        return member
    
    
    def index_members(
        source: RemoteArchive,
        cache: Path,
        start: int,
        scan_end: int,
        data_end: int,
        kind: str,
        needed: set[str],
        scan_chunk_size: int,
    ) -> dict:
        signature = {
            "version": 1, "source": source.identity, "start": start,
            "scan_end": scan_end, "data_end": data_end, "kind": kind,
        }
        state = {}
        if cache.is_file():
            state = json.loads(cache.read_text(encoding="utf-8"))
        if state.get("signature") != signature:
            state = {"signature": signature, "cursor": start,
                     "complete": False, "members": {}}
        if needed.issubset(state["members"]) or state["complete"]:
            return state["members"]
        processed = 0
        last_saved = time.monotonic()
        try:
            while state["cursor"] + 512 <= scan_end:
                if source.client.stop.is_set():
                    raise InterruptedError("Indexing stopped")
                offset = state["cursor"]
                block_end = min(scan_end, offset + scan_chunk_size)
                block = source.read(offset, block_end - offset)
                relative = 0
                while relative + 512 <= len(block):
                    header = block[relative : relative + 512]
                    absolute = offset + relative
                    if header == bytes(512):
                        state["complete"] = True
                        state["cursor"] = scan_end
                        break
                    member = parse_header(header)
                    name = PurePosixPath(member.name).name
                    next_header = absolute + 512 + ((member.size + 511) // 512) * 512
                    if member.size < 0 or next_header > data_end:
                        raise ValueError(f"Tar member exceeds its archive: {member.name}")
                    if member.isfile() and PATTERNS[kind].fullmatch(name):
                        entry = {"offset": absolute + 512, "size": member.size}
                        if name in state["members"] and state["members"][name] != entry:
                            raise ValueError(f"Duplicate tar member name: {name}")
                        state["members"][name] = entry
                    processed += 1
                    # If the next header is outside this block, skip the unneeded
                    # image payload and request the next block at that exact header.
                    if next_header + 512 > block_end:
                        state["cursor"] = next_header
                        break
                    relative = next_header - offset
                    state["cursor"] = next_header
                    if needed.issubset(state["members"]):
                        break
                else:
                    state["cursor"] = block_end
                if state["complete"] or needed.issubset(state["members"]):
                    break
                if processed % 128 == 0 or time.monotonic() - last_saved >= 15:
                    atomic_write(cache, json.dumps(state).encode("utf-8"))
                    if kind == "classes":
                        print(f"Outer index: {len(state['members'])} classes cached; "
                              f"HTTP requests: {source.client.requests}", flush=True)
                    last_saved = time.monotonic()
            if state["cursor"] + 512 > scan_end:
                state["complete"] = True
        finally:
            atomic_write(cache, json.dumps(state).encode("utf-8"))
        return state["members"]
    
    
    def valid_image(path: Path, expected_size: int) -> bool:
        if not path.is_file() or path.stat().st_size != expected_size:
            return False
        try:
            with Image.open(path) as image:
                image.load()
            return True
        except (OSError, ValueError, Image.DecompressionBombError):
            return False
    
    
    def process_group(source, cache, start, end, data_end, kind, requested, args, scan_chunk_size):
        members = index_members(
            source, cache, start, end, data_end, kind, set(requested), scan_chunk_size
        )
        found = {}
        downloaded = existing = 0
        for name in sorted(set(requested).intersection(members)):
            relative = requested[name]
            entry = members[name]
            if not (0 < entry["size"] <= 128 * 1024 * 1024):
                raise ValueError(f"Unexpected image size for {relative}: {entry['size']}")
            found[relative] = entry["size"]
            if args.index_only:
                continue
            destination = args.output_dir / relative
            if valid_image(destination, entry["size"]):
                existing += 1
                continue
            content = source.read(entry["offset"], entry["size"])
            with Image.open(io.BytesIO(content)) as image:
                image.load()
            atomic_write(destination, content)
            downloaded += 1
        return found, downloaded, existing
    ✓ • 93ms

## Activity

    $ for p in /AGENTS.md /home/AGENTS.md /home/linfu/AGENTS.md /home/linfu/src/AGENTS.md /home/linfu/src/Test/AGENTS.md /home/linfu/src/Test/ObjectConceptLearning/AGENTS.md /home/linfu/src/Test/ObjectConceptLearning/data/AGENTS.md; do if test -f "$p"; then cat "$p"; fi; done
    ✓ • 0ms

## Activity

    $ df -h . /tmp
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sdd       1007G   66G  890G   7% /home/linfu/src/Test/ObjectConceptLearning/data
    /dev/sdd       1007G   66G  890G   7% /tmp
    ✓ • 0ms

## Assistant

检查结果：没有遗留下载进程；COCO 和 aPY 所需文件都在。ImageNet 的 7,924 张目标图片尚未下载；网页来源还缺 269 张，现有 `from_web.tgz` 里也没有它们。我会保留已有数据，只补缺失文件，并保存续传索引。

## Activity

    $ cat ../README.md ../.gitignore
    # Object Concept Learning
    
    This the official repository of [Beyond Object Recognition: A New Benchmark towards Object Concept Learning](https://arxiv.org/abs/2212.02710) (ICCV 2023).
    
    
    We propose the challenging Object Concept Learning (OCL) task to push the envelope of object understanding, requiring machines to reason out affordances and simultaneously give the reason: what attributes make an object possess these affordances. To support OCL, we build a densely annotated knowledge base including extensive annotations for three levels of ob- ject concept (category, attribute, affordance), and the clear causal relations of three levels. This repo contains our **data and annotation**, and the **code implementation**.
    
    <p align="center"><img src='docs/task.png' width=600></p>
    
    
    
    ## Preparation
    
    ### Requirements
    
    See `requirements.txt`. Python 3.8 + PyTorch 1.8.1
    
    
    ### Datasets
    
    To prepare data, you should download ImageNet(2012) to `./data/ImageNet` and download the url-expired web images from [here](https://drive.google.com/drive/folders/1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF?usp=share_link) and put to `./data/from_web.tgz`. The folder structure should be like:
    ```
    ./data
    ├── from_web.tgz
    ├── ImageNet/
    │   ├── train/
    │   │   ├── n02133161/
    │   │   ├── n02514041/
    │   │   └── ......
    │   └── val
    │       ├── ILSVRC2012_val_00011812.JPEG
    │       ├── ILSVRC2012_val_00036760.JPEG
    │       └── ......
    ├── resources/
    ├── prepare_data.sh
    └── ...
    ```
    
    
    Then run the script to download and reorganize the rest datasets:
    ```
    cd ./data;
    sh prepare_data.sh;
    ```
    
    
    
    The annotation files have been put in `./data/resources`:
    
    - `OCL_class_*.pkl` contains the annotation of the three splits:
      - The pickle files are stored in binary, please use `"rb"` mode.
      - Each file is a list of image annotations. Each image has multiple object instances with bounding box, attributes, affordances, object category and causal rules (attribute->affordance).
      - Most files are from COCO, ImageNet-1K, aPY and SUN-attribute. Around 5K images are from the internet, whose urls are listed in `image_urls_from_web.json`. Please use the md5 (or file name) to match the files to the annotations.
    - `OCL_class_*.json` contains the list of classes.
    
    
    
    ## Pretrained model
    
    
    You may optionally download our pretrained OCRN model from [here](https://drive.google.com/drive/folders/1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF?usp=share_link).
    
    
    ## Usage
    
    For the standalone Hugging Face CLIP inference experiment in `Test.md`, see the
    [CLIP inference guide](docs/clip_inference.md). It selects the ten largest object
    categories by instance count across all annotation files, then evaluates all
    objects from those categories. It uses batches of four object crops
    and reports category Top-k accuracy plus attribute/affordance mAP. Run
    `bash setup_clip_gpu.sh` on the GPU server to install its dependencies.
    
    Extract feature and the object prior:
    ```
    python extract_feature.py --cfg config/Faster50Feature.yaml --splits train
    python extract_feature.py --cfg config/Faster50Feature.yaml --splits valtest
    
    python calc_dataset_prior.py --feature_dir features/OCL_faster50_pt_frz
    ```
    
    Train an OCRN (in three stages):
    
    ```
    python -m torch.distributed.launch --nproc_per_node=4 run_ocl.py --cfg config/OCRN_stage1.yaml
    
    python -m torch.distributed.launch --nproc_per_node=4 run_ocl.py --cfg config/OCRN_stage2.yaml --trained_weight ./logs/OCRN_stage1/checkpoint_ep170.pt --weight_type ocrn_attr
    
    python -m torch.distributed.launch --nproc_per_node=4 run_ocl.py --cfg config/OCRN_stage3.yaml --trained_weight ./logs/OCRN_stage2/checkpoint_ep20.pt --weight_type pretrain
    ```
    
    
    
    Test with GT boxes:
    ```
    python test_ocl.py --cfg config/OCRN_stage3.yaml --trained_weight ./logs/OCRN_stage3/checkpoint_ep10.pt
    ```
    
    
    Test on TDE metric:
    ```
    python test_tde.py --cfg config/OCRN_stage3.yaml --trained_weight ./logs/OCRN_stage3/checkpoint_ep10.pt
    ```
    
    
    
    
    ## Reference
    
    ```
    @inproceedings{li2023beyond,
      title={Beyond Object Recognition: A New Benchmark towards Object Concept Learning},
      author={Li, Yong-Lu and Xu, Yue and Xu, Xinyu and Mao, Xiaohan and Yao, Yuan and Liu, Siqi and Lu, Cewu},
      booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
      pages={20029--20040},
      year={2023}
    }
    ```
    
    
    ## Acknowledgement
    
    Our database is built upon [aPY](https://vision.cs.uiuc.edu/attributes/) (which also involves [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/index.html)), [SUN attribute](https://cs.brown.edu/~gmpatter/sunattributes.html), [MS-COCO](https://cocodataset.org) and [ImageNet](https://www.image-net.org) (and the [ImageNet-150K dataset](https://vipl.ict.ac.cn/en/resources/databases/201803/t20180316_34793.html)).
    Part of the images are collected via internet and we only provide URLs for redownloading due to licensing issues. Since some URLs have been expired or unreachable (~2K), we provide these images **for only non-commercial usage**.
    
    Some of the images are collected from the internet, and we only offer URLs for re-download due to licensing concerns. Since certain URLs having expired or become inaccessible (~2K), we provide these images **only for non-commercial and educational use**.
    # SymNet logs
    .vscode/
    .vscode/*
    .vscode/settings.json
    
    
    data/aPY
    data/SUN
    data/from_web
    data/ImageNet
    data/SUN
    logs
    weights
    features
    data_packed
    
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    *$py.class
    
    # C extensions
    *.so
    
    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    pip-wheel-metadata/
    share/python-wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST
    
    # PyInstaller
    #  Usually these files are written by a python script from a template
    #  before PyInstaller builds the exe, so as to inject date/other infos into it.
    *.manifest
    *.spec
    
    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt
    
    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    *.py,cover
    .hypothesis/
    .pytest_cache/
    
    # Translations
    *.mo
    *.pot
    
    # Django stuff:
    *.log
    local_settings.py
    db.sqlite3
    db.sqlite3-journal
    
    # Flask stuff:
    instance/
    .webassets-cache
    
    # Scrapy stuff:
    .scrapy
    
    # Sphinx documentation
    docs/_build/
    
    # PyBuilder
    target/
    
    # Jupyter Notebook
    .ipynb_checkpoints
    
    # IPython
    profile_default/
    ipython_config.py
    
    # pyenv
    .python-version
    
    # pipenv
    #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
    #   However, in case of collaboration, if having platform-specific dependencies or dependencies
    #   having no cross-platform support, pipenv may install dependencies that don't work, or not
    #   install all needed dependencies.
    #Pipfile.lock
    
    # PEP 582; used by e.g. github.com/David-OConnor/pyflow
    __pypackages__/
    
    # Celery stuff
    celerybeat-schedule
    celerybeat.pid
    
    # SageMath parsed files
    *.sage.py
    
    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/
    
    # Spyder project settings
    .spyderproject
    .spyproject
    
    # Rope project settings
    .ropeproject
    
    # mkdocs documentation
    /site
    
    # mypy
    .mypy_cache/
    .dmypy.json
    dmypy.json
    
    # Pyre type checker
    .pyre/
    data/SUN/.
    data/aPY/.
    data/train2014
    data/val2014
    data/数据集
    data/COCO
    
    ✓ • 0ms

## Activity

    $ cat extract_imagenet_subset.py
    """Extract the OCL image manifest without expanding the whole ImageNet dataset."""
    
    from __future__ import annotations
    
    import argparse
    import os
    from pathlib import Path, PurePosixPath
    import shutil
    import sys
    import tarfile
    import tempfile
    
    
    def load_manifest(path: Path) -> list[str]:
        names = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not names or len(names) != len(set(names)):
            raise ValueError("The image manifest must be non-empty and contain no duplicates.")
        for name in names:
            path_parts = PurePosixPath(name).parts
            if (
                PurePosixPath(name).is_absolute()
                or ".." in path_parts
                or not (
                    (len(path_parts) == 3 and path_parts[0] == "train")
                    or (len(path_parts) == 2 and path_parts[0] == "val")
                )
            ):
                raise ValueError(f"Unexpected ImageNet path: {name}")
        return names
    
    
    def copy_image(archive: tarfile.TarFile, member: tarfile.TarInfo, destination: Path) -> bool:
        if not member.isfile() or member.size <= 0:
            raise ValueError(f"Expected a non-empty image file: {member.name}")
        if destination.is_file() and destination.stat().st_size == member.size:
            return False
    
        destination.parent.mkdir(parents=True, exist_ok=True)
        source = archive.extractfile(member)
        if source is None:
            raise ValueError(f"Cannot read archive member: {member.name}")
    
        temporary = None
        try:
            # Publish only complete files so an interrupted extraction can be rerun.
            with source, tempfile.NamedTemporaryFile(
                dir=destination.parent, prefix=f".{destination.name}.", suffix=".part", delete=False
            ) as output:
                temporary = Path(output.name)
                shutil.copyfileobj(source, output, length=1024 * 1024)
            if temporary.stat().st_size != member.size:
                raise ValueError(f"Incomplete archive member: {member.name}")
            os.replace(temporary, destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return True
    
    
    def extract_images(
        archive: tarfile.TarFile,
        requested: dict[str, str],
        output_dir: Path,
        found: set[str],
    ) -> tuple[int, int]:
        remaining = dict(requested)
        copied = skipped = 0
        for member in archive:
            relative = remaining.pop(PurePosixPath(member.name).name, None)
            if relative is None:
                continue
            if copy_image(archive, member, output_dir / relative):
                copied += 1
            else:
                skipped += 1
            found.add(relative)
            if not remaining:
                break
        return copied, skipped
    
    
    def extract_subset(archive_dir: Path, output_dir: Path, names: list[str]) -> tuple[int, int]:
        train = {}
        val = {}
        for name in names:
            parts = PurePosixPath(name).parts
            if parts[0] == "train":
                train.setdefault(f"{parts[1]}.tar", {})[parts[2]] = name
            else:
                val[parts[1]] = name
    
        found = set()
        copied = skipped = 0
        if train:
            total_classes = len(train)
            completed_classes = 0
            with tarfile.open(archive_dir / "ILSVRC2012_img_train.tar", mode="r:") as outer:
                for member in outer:
                    requested = train.pop(PurePosixPath(member.name).name, None)
                    if requested is None:
                        continue
                    if not member.isfile():
                        raise ValueError(f"Expected a class archive: {member.name}")
                    class_file = outer.extractfile(member)
                    if class_file is None:
                        raise ValueError(f"Cannot read class archive: {member.name}")
                    # Uncompressed nested tar files support seeking; no class tar is written to disk.
                    with class_file, tarfile.open(fileobj=class_file, mode="r:") as inner:
                        new, existing = extract_images(inner, requested, output_dir, found)
                    copied += new
                    skipped += existing
                    completed_classes += 1
                    if completed_classes == 1 or completed_classes % 10 == 0 or not train:
                        print(
                            f"Train classes: {completed_classes}/{total_classes}; "
                            f"images copied: {copied}; size-matched existing images: {skipped}",
                            flush=True,
                        )
                    if not train:
                        break
    
        if val:
            with tarfile.open(archive_dir / "ILSVRC2012_img_val.tar", mode="r:") as archive:
                new, existing = extract_images(archive, val, output_dir, found)
            copied += new
            skipped += existing
    
        missing = sorted(set(names) - found)
        if missing:
            raise ValueError(
                f"{len(missing)} requested images were not found in the archives: {missing[:10]}"
            )
        print(f"Complete: {len(found)} images; copied={copied}; size-matched existing={skipped}.")
        print(f"Output directory: {output_dir.resolve()}")
        return copied, skipped
    
    
    def main() -> None:
        data_dir = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--archive-dir", type=Path, default=data_dir / "imagenet_archives")
        parser.add_argument("--output-dir", type=Path, default=data_dir / "ImageNet")
        parser.add_argument(
            "--manifest", type=Path, default=data_dir / "transfer_lists" / "imagenet_required.txt"
        )
        args = parser.parse_args()
        names = load_manifest(args.manifest.expanduser())
        extract_subset(args.archive_dir.expanduser(), args.output_dir.expanduser(), names)
    
    
    if __name__ == "__main__":
        try:
            main()
        except (OSError, ValueError, tarfile.TarError) as error:
            print(f"Error: {error}", file=sys.stderr)
            raise SystemExit(1)
    ✓ • 0ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        from urllib.parse import urlsplit
        import json
        root=Path('.')
        required=set((root/'transfer_lists/ocl_non_imagenet.txt').read_text().splitlines())
        missing={n for n in required if n.startswith('from_web/') and not (root/n).is_file()}
        urls=json.loads((root/'resources/url_to_filename.json').read_text())
        entries=[(u,n) for u,n in urls if n in missing]
        print('missing_web',len(missing),'mapped',len(entries))
        print('domains',Counter(urlsplit(u).netloc for u,n in entries).most_common(15))
        print('examples',entries[:12])
        f=json.loads((root/'web_download_failures.json').read_text())
        print('previous_report_counts',{k:v for k,v in f.items() if k!='failures'})
        for r in f.get('failures',[]):
         if r.get('name') in missing:
          print('previous_failure',r)
          if sum(1 for e in f['failures'][:f['failures'].index(r)+1] if e.get('name') in missing)>=3: break
        for p in sorted(root.iterdir()):
         if p.name not in ('train2014','val2014','from_web','SUN','aPY'):
          print('root_entry',p.name,'symlink' if p.is_symlink() else 'dir' if p.is_dir() else p.stat().st_size)
        PY
    missing_web 269 mapped 269
    domains [('images.freeimages.com', 35), ('hbimg.b0.upaiyun.com', 33), ('en.pimg.jp', 19), ('i.serengeseba.com', 15), ('dpic.tiankong.com', 12), ('hellorfimg.zcool.cn', 7), ('i2.wp.com', 6), ('img.qqzhi.com', 5), ('www.ecerimg.com', 5), ('n1.itc.cn', 5), ('www.eautobazaar.com', 4), ('img.everychina.com', 3), ('ec4.images-amazon.com', 3), ('www.chinadaily.com.cn', 3), ('images6.fanpop.com', 3)]
    examples [('http://img.qqzhi.com/upload/img_3_1674547204D2503538303_23.jpg', 'from_web/train_0477.jpg'), ('http://i.serengeseba.com/uploads/i_5_3142878201x3526148436_26.jpg', 'from_web/train_0482.jpg'), ('http://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'from_web/train_0485.jpg'), ('http://www.huanbohainews.com.cn/pic/0/12/12/95/12129542_913356.jpg', 'from_web/train_0524.jpg'), ('http://www.ecerimg.com/nimg/69/b3/69097cf062288457259ff7e38c7f/hansel_children_electric_prince_motorbike_ride_for_indoor_and_outdoor_remote.jpg', 'from_web/train_1015.jpg'), ('http://www.ecerimg.com/pic/z2e6179e/b_o_ride_on_motorbike.jpg', 'from_web/train_1020.jpg'), ('http://img.everychina.com/nimg/9c/32/b16ff4fa19c2820deb8ce4b82729-600x600-0/ride_on_electric_motorbike_for_kids_kids_motorcycle_bike_battery_bike_for_kids.jpg', 'from_web/train_1023.jpg'), ('http://n1.itc.cn/img8/wb/recom/2016/09/09/147336856483585219.JPEG', 'from_web/val_0003.jpeg'), ('http://file.youboy.com/a/39/59/33/5/17682375.jpg', 'from_web/val_0011.jpg'), ('http://i.serengeseba.com/uploads/i_0_3391044372x762695184_26.jpg', 'from_web/val_0052.jpg'), ('http://img.qqzhi.com/upload/img_5_3908073024D1370086755_23.jpg', 'from_web/val_0055.jpg'), ('http://i.serengeseba.com/uploads/i_5_1367647867x1710641272_26.jpg', 'from_web/val_0061.jpg')]
    previous_report_counts {'requested': 3422, 'downloaded': 2502, 'skipped': 0, 'failed': 920, 'pending': 0, 'interrupted': False}
    previous_failure {'url': 'http://img.qqzhi.com/upload/img_3_1674547204D2503538303_23.jpg', 'name': 'from_web/train_0477.jpg', 'attempts': [{'url': 'https://img.qqzhi.com/upload/img_3_1674547204D2503538303_23.jpg', 'attempt': 1, 'error': "HTTPSConnectionPool(host='img.qqzhi.com', port=443): Max retries exceeded with url: /upload/img_3_1674547204D2503538303_23.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://img.qqzhi.com/upload/img_3_1674547204D2503538303_23.jpg', 'attempt': 2, 'error': "HTTPSConnectionPool(host='img.qqzhi.com', port=443): Max retries exceeded with url: /upload/img_3_1674547204D2503538303_23.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://img.qqzhi.com/upload/img_3_1674547204D2503538303_23.jpg', 'attempt': 3, 'error': "HTTPSConnectionPool(host='img.qqzhi.com', port=443): Max retries exceeded with url: /upload/img_3_1674547204D2503538303_23.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'http://img.qqzhi.com/upload/img_3_1674547204D2503538303_23.jpg', 'attempt': 1, 'error': "cannot identify image file '/home/linfu/src/Test/ObjectConceptLearning/data/from_web/.train_0477.jpg.qughkhnh.part'"}]}
    previous_failure {'url': 'http://i.serengeseba.com/uploads/i_5_3142878201x3526148436_26.jpg', 'name': 'from_web/train_0482.jpg', 'attempts': [{'url': 'https://i.serengeseba.com/uploads/i_5_3142878201x3526148436_26.jpg', 'attempt': 1, 'error': "HTTPSConnectionPool(host='i.serengeseba.com', port=443): Read timed out. (read timeout=10)"}, {'url': 'https://i.serengeseba.com/uploads/i_5_3142878201x3526148436_26.jpg', 'attempt': 2, 'error': "HTTPSConnectionPool(host='i.serengeseba.com', port=443): Max retries exceeded with url: /uploads/i_5_3142878201x3526148436_26.jpg (Caused by SSLError(SSLError(1, '[SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1000)')))"}, {'url': 'https://i.serengeseba.com/uploads/i_5_3142878201x3526148436_26.jpg', 'attempt': 3, 'error': "HTTPSConnectionPool(host='i.serengeseba.com', port=443): Max retries exceeded with url: /uploads/i_5_3142878201x3526148436_26.jpg (Caused by SSLError(SSLError(1, '[SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1000)')))"}, {'url': 'http://i.serengeseba.com/uploads/i_5_3142878201x3526148436_26.jpg', 'attempt': 1, 'error': "cannot identify image file '/home/linfu/src/Test/ObjectConceptLearning/data/from_web/.train_0482.jpg.1kx1m40g.part'"}]}
    previous_failure {'url': 'http://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'name': 'from_web/train_0485.jpg', 'attempts': [{'url': 'https://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'attempt': 1, 'error': "HTTPSConnectionPool(host='dpic.tiankong.com', port=443): Max retries exceeded with url: /s1/eh/QJ6860106176.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'attempt': 2, 'error': "HTTPSConnectionPool(host='dpic.tiankong.com', port=443): Max retries exceeded with url: /s1/eh/QJ6860106176.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'attempt': 3, 'error': "HTTPSConnectionPool(host='dpic.tiankong.com', port=443): Max retries exceeded with url: /s1/eh/QJ6860106176.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'http://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'attempt': 1, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}, {'url': 'http://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'attempt': 2, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}, {'url': 'http://dpic.tiankong.com/s1/eh/QJ6860106176.jpg', 'attempt': 3, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}]}
    root_entry .agents dir
    root_entry .aws dir
    root_entry .codex dir
    root_entry .git dir
    root_entry COCO dir
    root_entry __pycache__ dir
    root_entry download_imagenet_subset.py 17858
    root_entry download_web_images.py 5226
    root_entry extract_imagenet_subset.py 5904
    root_entry from_web.tgz 280569727
    root_entry from_web.tgz:Zone.Identifier 25
    root_entry imagenet_index dir
    root_entry prepare_data.sh 1090
    root_entry resources dir
    root_entry transfer_lists dir
    root_entry web_download_failures.json 1441617
    root_entry 数据集 dir
    ✓ • 105ms

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/download_selected_web.py
    """Resume only the web images needed by the OCL top-ten evaluation."""
    
    from __future__ import annotations
    
    import argparse
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import fcntl
    import json
    from pathlib import Path
    import threading
    
    import requests
    
    from download_imagenet_subset import atomic_write
    from download_web_images import download_image
    
    
    def main() -> int:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--workers", type=int, default=12)
        parser.add_argument("--timeout", type=float, default=12)
        parser.add_argument("--retries", type=int, default=1)
        args = parser.parse_args()
        if not 1 <= args.workers <= 32 or args.timeout <= 0 or args.retries < 0:
            parser.error("Use 1..32 workers, a positive timeout, and non-negative retries.")
        root = Path(__file__).resolve().parent
        reports = root / "transfer_lists"
        with (reports / "web_download.lock").open("a+") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise SystemExit("A selected-web download is already running.")
            required = {
                name for name in (reports / "ocl_non_imagenet.txt").read_text().splitlines()
                if name.startswith("from_web/")
            }
            entries = json.loads((root / "resources/url_to_filename.json").read_text())
            urls = {name: url for url, name in entries}
            local = threading.local()
    
            def fetch(name):
                if name not in urls:
                    return name, "failed", [{"error": "No source URL in OCL metadata"}]
                if not hasattr(local, "session"):
                    local.session = requests.Session()
                    local.session.headers["User-Agent"] = "Mozilla/5.0 (compatible; OCL-image-downloader/1.0)"
                status, errors = download_image(
                    local.session, urls[name], root / name,
                    timeout=args.timeout, retries=args.retries,
                )
                return name, status, errors
    
            counts = {"downloaded": 0, "skipped": 0, "failed": 0}
            failures = []
            report = reports / "web_download_report.json"
    
            def save():
                result = {
                    "requested": len(required), **counts,
                    "pending": len(required) - sum(counts.values()),
                    "failures": sorted(failures, key=lambda item: item["name"]),
                }
                atomic_write(report, (json.dumps(result, indent=2) + "\n").encode())
    
            try:
                with ThreadPoolExecutor(max_workers=args.workers) as pool:
                    futures = [pool.submit(fetch, name) for name in sorted(required)]
                    for future in as_completed(futures):
                        name, status, errors = future.result()
                        counts[status] += 1
                        if status == "failed":
                            failures.append({"name": name, "url": urls.get(name), "attempts": errors})
                        completed = sum(counts.values())
                        if completed % 25 == 0 or completed == len(required):
                            save()
                            print(f"Web images {completed}/{len(required)}: {counts}", flush=True)
            finally:
                save()
            return 1 if failures else 0
    
    
    if __name__ == "__main__":
        raise SystemExit(main())

## Assistant

ImageNet 的索引扫描已开始，索引会定期保存，后续可接着跑。网页图片也在按原始 URL 重试；同时我会检查现有图片能否解码，以及标注框是否可用，避免只凭文件存在就判断数据齐全。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import json, time
        from pathlib import Path
        for p in sorted(Path('imagenet_index').rglob('*.json'))[:5]:
         d=json.loads(p.read_text()); print(p, 'members', len(d.get('members',{})), 'cursor', d.get('cursor'), 'age',round(time.time()-p.stat().st_mtime,1))
        PY
    imagenet_index/train/n01518878.tar.json members 1212 cursor 1574194688 age 2439.9
    imagenet_index/train/n01530575.tar.json members 1295 cursor 1707494400 age 2414.7
    imagenet_index/train/n01531178.tar.json members 1298 cursor 1854844416 age 2414.7
    imagenet_index/train/n01532829.tar.json members 1225 cursor 2007991808 age 2435.6
    imagenet_index/train/n01534433.tar.json members 1237 cursor 2170583040 age 2433.6
    ✓ • 249ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import json
        names=Path('transfer_lists/imagenet_required.txt').read_text().splitlines()
        missing=[n for n in names if not (Path('ImageNet')/n).is_file()]
        print('ImageNet existing',len(names)-len(missing),'missing',len(missing))
        print('missing_by_split',{s:sum(n.startswith(s+'/') for n in missing) for s in ['train','val']})
        p=Path('imagenet_index/val.json')
        if p.exists():
         d=json.loads(p.read_text()); targets={Path(n).name for n in names if n.startswith('val/')};print('val_index',len(d['members']),d['cursor'],'targets_found',len(targets & d['members'].keys()),'total_size',d['signature']['source']['size'])
        p=Path('transfer_lists/web_download_report.json')
        if p.exists():
         d=json.loads(p.read_text()); print('web_report',{k:v for k,v in d.items() if k!='failures'})
        print('web_now_missing',sum(not Path(n).is_file() for n in Path('transfer_lists/ocl_non_imagenet.txt').read_text().splitlines() if n.startswith('from_web/')))
        PY
    ImageNet existing 7702 missing 222
    missing_by_split {'train': 0, 'val': 222}
    val_index 1336 215621632 targets_found 8 total_size 6744924160
    web_report {'requested': 1474, 'downloaded': 31, 'skipped': 499, 'failed': 895, 'pending': 49}
    web_now_missing 234
    ✓ • 776ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B download_selected_web.py --workers 16 --timeout 12 --retries 1
    Web images 25/1474: {'downloaded': 0, 'skipped': 11, 'failed': 14}
    Web images 50/1474: {'downloaded': 0, 'skipped': 29, 'failed': 21}
    Web images 75/1474: {'downloaded': 0, 'skipped': 51, 'failed': 24}
    Web images 100/1474: {'downloaded': 0, 'skipped': 65, 'failed': 35}
    Web images 125/1474: {'downloaded': 0, 'skipped': 76, 'failed': 49}
    Web images 150/1474: {'downloaded': 0, 'skipped': 91, 'failed': 59}
    Web images 175/1474: {'downloaded': 0, 'skipped': 107, 'failed': 68}
    Web images 200/1474: {'downloaded': 1, 'skipped': 121, 'failed': 78}
    Web images 225/1474: {'downloaded': 1, 'skipped': 134, 'failed': 90}
    Web images 250/1474: {'downloaded': 1, 'skipped': 148, 'failed': 101}
    Web images 275/1474: {'downloaded': 1, 'skipped': 161, 'failed': 113}
    Web images 300/1474: {'downloaded': 1, 'skipped': 169, 'failed': 130}
    Web images 325/1474: {'downloaded': 1, 'skipped': 171, 'failed': 153}
    Web images 350/1474: {'downloaded': 1, 'skipped': 189, 'failed': 160}
    Web images 375/1474: {'downloaded': 1, 'skipped': 213, 'failed': 161}
    Web images 400/1474: {'downloaded': 1, 'skipped': 213, 'failed': 186}
    Web images 425/1474: {'downloaded': 1, 'skipped': 213, 'failed': 211}
    Web images 450/1474: {'downloaded': 1, 'skipped': 213, 'failed': 236}
    Web images 475/1474: {'downloaded': 1, 'skipped': 213, 'failed': 261}
    Web images 500/1474: {'downloaded': 1, 'skipped': 213, 'failed': 286}
    Web images 525/1474: {'downloaded': 1, 'skipped': 213, 'failed': 311}
    Web images 550/1474: {'downloaded': 1, 'skipped': 213, 'failed': 336}
    Web images 575/1474: {'downloaded': 1, 'skipped': 213, 'failed': 361}
    Web images 600/1474: {'downloaded': 1, 'skipped': 213, 'failed': 386}
    Web images 625/1474: {'downloaded': 1, 'skipped': 213, 'failed': 411}
    Web images 650/1474: {'downloaded': 1, 'skipped': 213, 'failed': 436}
    Web images 675/1474: {'downloaded': 1, 'skipped': 213, 'failed': 461}
    Web images 700/1474: {'downloaded': 1, 'skipped': 213, 'failed': 486}
    Web images 725/1474: {'downloaded': 1, 'skipped': 213, 'failed': 511}
    Web images 750/1474: {'downloaded': 1, 'skipped': 213, 'failed': 536}
    Web images 775/1474: {'downloaded': 1, 'skipped': 213, 'failed': 561}
    Web images 800/1474: {'downloaded': 1, 'skipped': 213, 'failed': 586}
    Web images 825/1474: {'downloaded': 1, 'skipped': 216, 'failed': 608}
    Web images 850/1474: {'downloaded': 2, 'skipped': 225, 'failed': 623}
    Web images 875/1474: {'downloaded': 2, 'skipped': 242, 'failed': 631}
    Web images 900/1474: {'downloaded': 2, 'skipped': 256, 'failed': 642}
    Web images 925/1474: {'downloaded': 2, 'skipped': 269, 'failed': 654}
    Web images 950/1474: {'downloaded': 2, 'skipped': 282, 'failed': 666}
    Web images 975/1474: {'downloaded': 2, 'skipped': 295, 'failed': 678}
    Web images 1000/1474: {'downloaded': 2, 'skipped': 309, 'failed': 689}
    Web images 1025/1474: {'downloaded': 2, 'skipped': 322, 'failed': 701}
    Web images 1050/1474: {'downloaded': 2, 'skipped': 335, 'failed': 713}
    Web images 1075/1474: {'downloaded': 2, 'skipped': 350, 'failed': 723}
    Web images 1100/1474: {'downloaded': 2, 'skipped': 367, 'failed': 731}
    Web images 1125/1474: {'downloaded': 2, 'skipped': 381, 'failed': 742}
    Web images 1150/1474: {'downloaded': 2, 'skipped': 391, 'failed': 757}
    Web images 1175/1474: {'downloaded': 2, 'skipped': 403, 'failed': 770}
    Web images 1200/1474: {'downloaded': 2, 'skipped': 414, 'failed': 784}
    Web images 1225/1474: {'downloaded': 2, 'skipped': 427, 'failed': 796}
    Web images 1250/1474: {'downloaded': 2, 'skipped': 442, 'failed': 806}
    Web images 1275/1474: {'downloaded': 2, 'skipped': 453, 'failed': 820}
    Web images 1300/1474: {'downloaded': 2, 'skipped': 467, 'failed': 831}
    Web images 1325/1474: {'downloaded': 2, 'skipped': 480, 'failed': 843}
    Web images 1350/1474: {'downloaded': 2, 'skipped': 494, 'failed': 854}
    Web images 1375/1474: {'downloaded': 2, 'skipped': 499, 'failed': 874}
    Web images 1400/1474: {'downloaded': 17, 'skipped': 499, 'failed': 884}
    Web images 1425/1474: {'downloaded': 31, 'skipped': 499, 'failed': 895}
    Web images 1450/1474: {'downloaded': 42, 'skipped': 499, 'failed': 909}
    Web images 1474/1474: {'downloaded': 54, 'skipped': 499, 'failed': 921}
    ✗ (1) • 1m 10s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B download_imagenet_subset.py --header-only --workers 24 --timeout 20 --retries 3
    Indexing outer training tar for 190 required classes...
    Outer index: 53 classes cached; HTTP requests: 53
    Outer index: 102 classes cached; HTTP requests: 102
    Outer index: 128 classes cached; HTTP requests: 128
    Outer index: 175 classes cached; HTTP requests: 175
    Outer index: 213 classes cached; HTTP requests: 213
    Outer index: 256 classes cached; HTTP requests: 256
    Outer index: 299 classes cached; HTTP requests: 299
    Outer index: 346 classes cached; HTTP requests: 346
    Outer index: 384 classes cached; HTTP requests: 384
    Outer index: 425 classes cached; HTTP requests: 425
    Outer index: 468 classes cached; HTTP requests: 468
    Outer index: 512 classes cached; HTTP requests: 512
    Outer index: 552 classes cached; HTTP requests: 552
    Outer index: 592 classes cached; HTTP requests: 592
    Outer index: 628 classes cached; HTTP requests: 628
    Outer index: 640 classes cached; HTTP requests: 640
    Outer index: 689 classes cached; HTTP requests: 689
    Outer index: 727 classes cached; HTTP requests: 727
    Outer index: 768 classes cached; HTTP requests: 768
    Outer index: 809 classes cached; HTTP requests: 809
    Outer index: 858 classes cached; HTTP requests: 858
    Outer index: 896 classes cached; HTTP requests: 896
    Outer index: 943 classes cached; HTTP requests: 943
    Required training class archives total 25.00 GiB.
    Indexing headers only: low bandwidth, but many HTTP requests.
    Groups 0/191; images 0/7924; HTTP requests 2370; received 1.1 MiB
    Groups 0/191; images 0/7924; HTTP requests 3932; received 1.9 MiB
    Groups 0/191; images 0/7924; HTTP requests 5562; received 2.7 MiB
    Groups 0/191; images 0/7924; HTTP requests 7124; received 3.5 MiB
    Groups 0/191; images 0/7924; HTTP requests 8689; received 4.2 MiB
    Groups 0/191; images 0/7924; HTTP requests 10319; received 5.0 MiB
    Groups 0/191; images 0/7924; HTTP requests 11879; received 5.8 MiB
    Groups 0/191; images 0/7924; HTTP requests 13436; received 6.5 MiB
    Groups 0/191; images 0/7924; HTTP requests 15067; received 7.3 MiB
    Groups 0/191; images 0/7924; HTTP requests 16589; received 8.1 MiB
    Groups 0/191; images 0/7924; HTTP requests 18017; received 8.8 MiB
    Groups 0/191; images 0/7924; HTTP requests 19561; received 9.5 MiB
    Groups 0/191; images 0/7924; HTTP requests 21128; received 10.3 MiB
    Groups 0/191; images 0/7924; HTTP requests 22735; received 11.1 MiB
    Groups 0/191; images 0/7924; HTTP requests 24330; received 11.9 MiB
    Groups 0/191; images 0/7924; HTTP requests 25900; received 12.6 MiB
    Groups 0/191; images 0/7924; HTTP requests 27524; received 13.4 MiB
    Groups 0/191; images 0/7924; HTTP requests 29111; received 14.2 MiB
    Groups 1/191; images 37/7924; HTTP requests 30077; received 25.0 MiB
    Groups 2/191; images 80/7924; HTTP requests 30502; received 32.2 MiB
    Groups 3/191; images 123/7924; HTTP requests 30847; received 39.6 MiB
    Groups 4/191; images 166/7924; HTTP requests 31013; received 43.8 MiB
    Groups 5/191; images 203/7924; HTTP requests 31123; received 46.4 MiB
    Groups 6/191; images 246/7924; HTTP requests 31444; received 54.8 MiB
    Groups 7/191; images 283/7924; HTTP requests 31660; received 60.4 MiB
    Groups 8/191; images 326/7924; HTTP requests 31852; received 67.3 MiB
    Groups 9/191; images 363/7924; HTTP requests 31853; received 67.4 MiB
    Groups 10/191; images 400/7924; HTTP requests 32061; received 79.2 MiB
    Groups 11/191; images 437/7924; HTTP requests 32427; received 103.3 MiB
    Groups 12/191; images 480/7924; HTTP requests 32575; received 112.8 MiB
    Groups 13/191; images 517/7924; HTTP requests 32615; received 115.0 MiB
    Groups 14/191; images 560/7924; HTTP requests 32693; received 118.6 MiB
    Groups 15/191; images 597/7924; HTTP requests 32701; received 118.9 MiB
    Groups 16/191; images 634/7924; HTTP requests 32799; received 123.0 MiB
    Groups 17/191; images 677/7924; HTTP requests 32863; received 125.3 MiB
    Groups 18/191; images 720/7924; HTTP requests 32889; received 126.5 MiB
    Groups 19/191; images 763/7924; HTTP requests 32903; received 126.9 MiB
    Groups 20/191; images 806/7924; HTTP requests 32967; received 128.7 MiB
    Groups 21/191; images 849/7924; HTTP requests 33021; received 129.7 MiB
    Groups 22/191; images 892/7924; HTTP requests 33033; received 129.9 MiB
    Groups 23/191; images 935/7924; HTTP requests 33044; received 129.9 MiB
    Groups 24/191; images 978/7924; HTTP requests 33098; received 130.4 MiB
    Groups 24/191; images 978/7924; HTTP requests 34728; received 131.2 MiB
    Groups 24/191; images 978/7924; HTTP requests 36307; received 131.9 MiB
    Groups 24/191; images 978/7924; HTTP requests 37877; received 132.7 MiB
    Groups 24/191; images 978/7924; HTTP requests 39509; received 133.5 MiB
    Groups 24/191; images 978/7924; HTTP requests 41085; received 134.3 MiB
    Groups 24/191; images 978/7924; HTTP requests 42656; received 135.0 MiB
    Groups 24/191; images 978/7924; HTTP requests 44289; received 135.8 MiB
    Groups 24/191; images 978/7924; HTTP requests 45914; received 136.6 MiB
    Groups 24/191; images 978/7924; HTTP requests 47747; received 137.5 MiB
    Groups 24/191; images 978/7924; HTTP requests 49594; received 138.4 MiB
    Groups 24/191; images 978/7924; HTTP requests 51487; received 139.3 MiB
    Groups 24/191; images 978/7924; HTTP requests 53316; received 140.2 MiB
    Groups 24/191; images 978/7924; HTTP requests 55153; received 141.1 MiB
    Groups 24/191; images 978/7924; HTTP requests 56992; received 142.0 MiB
    Groups 25/191; images 1021/7924; HTTP requests 58857; received 149.0 MiB
    Groups 26/191; images 1058/7924; HTTP requests 59645; received 153.2 MiB
    Groups 26/191; images 1058/7924; HTTP requests 61516; received 156.9 MiB
    Groups 27/191; images 1095/7924; HTTP requests 61785; received 159.1 MiB
    Groups 28/191; images 1132/7924; HTTP requests 62546; received 173.3 MiB
    Groups 29/191; images 1175/7924; HTTP requests 62703; received 176.6 MiB
    Groups 30/191; images 1218/7924; HTTP requests 63017; received 184.9 MiB
    Groups 31/191; images 1255/7924; HTTP requests 63083; received 187.5 MiB
    Groups 32/191; images 1298/7924; HTTP requests 63282; received 193.9 MiB
    Groups 33/191; images 1335/7924; HTTP requests 63299; received 194.5 MiB
    Groups 34/191; images 1372/7924; HTTP requests 63650; received 207.7 MiB
    Groups 35/191; images 1409/7924; HTTP requests 63765; received 215.2 MiB
    Groups 36/191; images 1452/7924; HTTP requests 63855; received 220.3 MiB
    Groups 37/191; images 1489/7924; HTTP requests 63942; received 224.1 MiB
    Groups 38/191; images 1526/7924; HTTP requests 64211; received 236.7 MiB
    Groups 39/191; images 1569/7924; HTTP requests 64418; received 246.6 MiB
    Groups 40/191; images 1606/7924; HTTP requests 64513; received 251.1 MiB
    Groups 41/191; images 1649/7924; HTTP requests 64636; received 255.6 MiB
    Groups 42/191; images 1692/7924; HTTP requests 64642; received 256.0 MiB
    Groups 43/191; images 1735/7924; HTTP requests 64661; received 256.4 MiB
    Groups 44/191; images 1778/7924; HTTP requests 64725; received 258.1 MiB
    Groups 45/191; images 1815/7924; HTTP requests 64752; received 258.5 MiB
    Groups 46/191; images 1858/7924; HTTP requests 65062; received 262.7 MiB
    Groups 47/191; images 1895/7924; HTTP requests 65142; received 263.6 MiB
    Groups 48/191; images 1938/7924; HTTP requests 65246; received 264.1 MiB
    Groups 48/191; images 1938/7924; HTTP requests 67084; received 265.0 MiB
    Groups 48/191; images 1938/7924; HTTP requests 68938; received 265.9 MiB
    Groups 48/191; images 1938/7924; HTTP requests 70822; received 266.9 MiB
    Groups 48/191; images 1938/7924; HTTP requests 72658; received 267.8 MiB
    Groups 48/191; images 1938/7924; HTTP requests 74494; received 268.7 MiB
    Groups 48/191; images 1938/7924; HTTP requests 76324; received 269.6 MiB
    Groups 49/191; images 1981/7924; HTTP requests 78096; received 271.9 MiB
    Groups 49/191; images 1981/7924; HTTP requests 79926; received 272.8 MiB
    Groups 49/191; images 1981/7924; HTTP requests 81757; received 273.8 MiB
    Groups 50/191; images 2018/7924; HTTP requests 82676; received 278.3 MiB
    Groups 51/191; images 2055/7924; HTTP requests 82776; received 278.8 MiB
    Groups 52/191; images 2098/7924; HTTP requests 84597; received 281.6 MiB
    Groups 52/191; images 2098/7924; HTTP requests 86425; received 282.5 MiB
    Groups 52/191; images 2098/7924; HTTP requests 88283; received 283.9 MiB
    Groups 53/191; images 2135/7924; HTTP requests 88919; received 286.3 MiB
    Groups 53/191; images 2135/7924; HTTP requests 90761; received 292.0 MiB
    Groups 54/191; images 2172/7924; HTTP requests 90911; received 293.5 MiB
    Groups 55/191; images 2215/7924; HTTP requests 91074; received 294.3 MiB
    Groups 55/191; images 2215/7924; HTTP requests 92947; received 302.3 MiB
    Groups 56/191; images 2252/7924; HTTP requests 92968; received 302.5 MiB
    Groups 57/191; images 2295/7924; HTTP requests 93235; received 306.1 MiB
    Groups 58/191; images 2338/7924; HTTP requests 93786; received 312.6 MiB
    Groups 59/191; images 2375/7924; HTTP requests 93867; received 313.4 MiB
    Groups 60/191; images 2418/7924; HTTP requests 94225; received 319.0 MiB
    Groups 61/191; images 2455/7924; HTTP requests 94458; received 323.9 MiB
    Groups 62/191; images 2492/7924; HTTP requests 94754; received 331.8 MiB
    Groups 63/191; images 2535/7924; HTTP requests 94933; received 335.9 MiB
    Groups 64/191; images 2572/7924; HTTP requests 94976; received 336.7 MiB
    Groups 65/191; images 2609/7924; HTTP requests 95133; received 339.9 MiB
    Groups 66/191; images 2646/7924; HTTP requests 95451; received 345.3 MiB
    Groups 67/191; images 2683/7924; HTTP requests 95462; received 345.5 MiB
    Groups 68/191; images 2720/7924; HTTP requests 95483; received 345.6 MiB
    Groups 69/191; images 2757/7924; HTTP requests 95719; received 347.7 MiB
    Groups 70/191; images 2794/7924; HTTP requests 96237; received 356.2 MiB
    Groups 71/191; images 2831/7924; HTTP requests 96596; received 359.7 MiB
    Groups 72/191; images 2868/7924; HTTP requests 96647; received 359.9 MiB
    Groups 73/191; images 2905/7924; HTTP requests 96728; received 360.5 MiB
    Groups 73/191; images 2905/7924; HTTP requests 98539; received 361.4 MiB
    Groups 73/191; images 2905/7924; HTTP requests 100404; received 362.3 MiB
    Groups 73/191; images 2905/7924; HTTP requests 102286; received 363.2 MiB
    Groups 73/191; images 2905/7924; HTTP requests 104127; received 364.1 MiB
    Groups 73/191; images 2905/7924; HTTP requests 105968; received 365.0 MiB
    Groups 73/191; images 2905/7924; HTTP requests 107820; received 365.9 MiB
    Groups 73/191; images 2905/7924; HTTP requests 109718; received 366.8 MiB
    Groups 73/191; images 2905/7924; HTTP requests 111553; received 371.2 MiB
    Groups 74/191; images 2942/7924; HTTP requests 111602; received 371.6 MiB
    Groups 75/191; images 2979/7924; HTTP requests 112585; received 374.8 MiB
    Groups 75/191; images 2979/7924; HTTP requests 114477; received 375.7 MiB
    Groups 75/191; images 2979/7924; HTTP requests 116309; received 379.8 MiB
    Groups 76/191; images 3016/7924; HTTP requests 116591; received 382.2 MiB
    Groups 77/191; images 3053/7924; HTTP requests 116972; received 383.0 MiB
    Groups 78/191; images 3096/7924; HTTP requests 118663; received 385.9 MiB
    Groups 79/191; images 3133/7924; HTTP requests 120345; received 390.6 MiB
    Groups 80/191; images 3176/7924; HTTP requests 121935; received 395.8 MiB
    Groups 81/191; images 3219/7924; HTTP requests 122552; received 397.9 MiB
    Groups 82/191; images 3256/7924; HTTP requests 124139; received 402.4 MiB
    Groups 83/191; images 3299/7924; HTTP requests 124700; received 407.9 MiB
    Groups 84/191; images 3342/7924; HTTP requests 125160; received 414.1 MiB
    Groups 85/191; images 3385/7924; HTTP requests 125266; received 415.7 MiB
    Groups 86/191; images 3422/7924; HTTP requests 125539; received 419.3 MiB
    Groups 87/191; images 3465/7924; HTTP requests 126140; received 426.7 MiB
    Groups 88/191; images 3508/7924; HTTP requests 126184; received 427.5 MiB
    Groups 89/191; images 3545/7924; HTTP requests 126267; received 428.0 MiB
    Groups 90/191; images 3588/7924; HTTP requests 127050; received 435.7 MiB
    Groups 91/191; images 3631/7924; HTTP requests 127604; received 447.5 MiB
    Groups 92/191; images 3674/7924; HTTP requests 127863; received 452.4 MiB
    Groups 93/191; images 3717/7924; HTTP requests 128146; received 456.8 MiB
    Groups 94/191; images 3754/7924; HTTP requests 128400; received 460.2 MiB
    Groups 95/191; images 3791/7924; HTTP requests 128426; received 460.3 MiB
    Groups 96/191; images 3834/7924; HTTP requests 128456; received 460.6 MiB
    Groups 97/191; images 3871/7924; HTTP requests 128559; received 461.2 MiB
    Groups 97/191; images 3871/7924; HTTP requests 130407; received 462.1 MiB
    Groups 97/191; images 3871/7924; HTTP requests 132249; received 463.0 MiB
    Groups 97/191; images 3871/7924; HTTP requests 134131; received 463.9 MiB
    Groups 97/191; images 3871/7924; HTTP requests 135983; received 464.8 MiB
    Groups 97/191; images 3871/7924; HTTP requests 137823; received 465.7 MiB
    Groups 97/191; images 3871/7924; HTTP requests 139669; received 466.6 MiB
    Groups 97/191; images 3871/7924; HTTP requests 141534; received 467.5 MiB
    Groups 98/191; images 3914/7924; HTTP requests 143047; received 471.9 MiB
    Groups 99/191; images 3957/7924; HTTP requests 144585; received 477.9 MiB
    Groups 99/191; images 3957/7924; HTTP requests 146433; received 478.8 MiB
    Groups 99/191; images 3957/7924; HTTP requests 148291; received 483.2 MiB
    Groups 100/191; images 4000/7924; HTTP requests 148695; received 485.2 MiB
    Groups 101/191; images 4043/7924; HTTP requests 150216; received 492.1 MiB
    Groups 102/191; images 4080/7924; HTTP requests 150662; received 492.9 MiB
    Groups 103/191; images 4117/7924; HTTP requests 151862; received 500.2 MiB
    Groups 104/191; images 4154/7924; HTTP requests 152178; received 502.1 MiB
    Groups 105/191; images 4197/7924; HTTP requests 152916; received 505.7 MiB
    Groups 106/191; images 4240/7924; HTTP requests 153468; received 507.3 MiB
    Groups 107/191; images 4277/7924; HTTP requests 154908; received 513.9 MiB
    Groups 108/191; images 4314/7924; HTTP requests 155697; received 527.7 MiB
    Groups 109/191; images 4357/7924; HTTP requests 155741; received 528.9 MiB
    Groups 110/191; images 4400/7924; HTTP requests 155881; received 531.1 MiB
    Groups 111/191; images 4437/7924; HTTP requests 156425; received 537.1 MiB
    Groups 112/191; images 4480/7924; HTTP requests 156553; received 538.6 MiB
    Groups 113/191; images 4523/7924; HTTP requests 156693; received 540.0 MiB
    Groups 114/191; images 4566/7924; HTTP requests 157320; received 544.9 MiB
    Groups 115/191; images 4603/7924; HTTP requests 157906; received 548.6 MiB
    Groups 116/191; images 4646/7924; HTTP requests 158124; received 549.5 MiB
    Groups 117/191; images 4683/7924; HTTP requests 159086; received 562.6 MiB
    Groups 118/191; images 4726/7924; HTTP requests 159197; received 564.1 MiB
    Groups 119/191; images 4769/7924; HTTP requests 159516; received 567.2 MiB
    Groups 120/191; images 4812/7924; HTTP requests 159937; received 570.6 MiB
    Groups 121/191; images 4855/7924; HTTP requests 160088; received 571.2 MiB
    Groups 121/191; images 4855/7924; HTTP requests 161920; received 572.1 MiB
    Groups 121/191; images 4855/7924; HTTP requests 163756; received 573.0 MiB
    Groups 121/191; images 4855/7924; HTTP requests 165624; received 573.9 MiB
    Groups 121/191; images 4855/7924; HTTP requests 167503; received 574.8 MiB
    Groups 121/191; images 4855/7924; HTTP requests 169352; received 575.7 MiB
    Groups 121/191; images 4855/7924; HTTP requests 171188; received 576.6 MiB
    Groups 121/191; images 4855/7924; HTTP requests 173062; received 577.5 MiB
    Groups 122/191; images 4898/7924; HTTP requests 174717; received 582.1 MiB
    Groups 123/191; images 4941/7924; HTTP requests 176381; received 591.3 MiB
    Groups 123/191; images 4941/7924; HTTP requests 178220; received 592.2 MiB
    Groups 123/191; images 4941/7924; HTTP requests 180097; received 595.3 MiB
    Groups 124/191; images 4984/7924; HTTP requests 180769; received 599.9 MiB
    Groups 125/191; images 5027/7924; HTTP requests 181058; received 601.7 MiB
    Groups 126/191; images 5070/7924; HTTP requests 181662; received 605.1 MiB
    Groups 127/191; images 5113/7924; HTTP requests 183015; received 613.7 MiB
    Groups 128/191; images 5156/7924; HTTP requests 183090; received 614.0 MiB
    Groups 129/191; images 5199/7924; HTTP requests 184494; received 620.6 MiB
    Groups 130/191; images 5236/7924; HTTP requests 184885; received 622.1 MiB
    Groups 131/191; images 5279/7924; HTTP requests 186711; received 633.4 MiB
    Groups 132/191; images 5322/7924; HTTP requests 186816; received 635.1 MiB
    Groups 133/191; images 5365/7924; HTTP requests 187433; received 642.5 MiB
    Groups 134/191; images 5408/7924; HTTP requests 188043; received 655.6 MiB
    Groups 135/191; images 5451/7924; HTTP requests 188194; received 658.6 MiB
    Groups 136/191; images 5494/7924; HTTP requests 188241; received 659.1 MiB
    Groups 137/191; images 5531/7924; HTTP requests 188541; received 662.1 MiB
    Groups 138/191; images 5568/7924; HTTP requests 188726; received 663.6 MiB
    Groups 139/191; images 5611/7924; HTTP requests 189192; received 666.6 MiB
    Groups 140/191; images 5648/7924; HTTP requests 189781; received 672.3 MiB
    Groups 141/191; images 5691/7924; HTTP requests 190419; received 678.0 MiB
    Groups 142/191; images 5734/7924; HTTP requests 190754; received 682.5 MiB
    Groups 143/191; images 5771/7924; HTTP requests 190908; received 684.5 MiB
    Groups 144/191; images 5814/7924; HTTP requests 191434; received 689.0 MiB
    Groups 145/191; images 5857/7924; HTTP requests 191811; received 690.3 MiB
    Groups 145/191; images 5857/7924; HTTP requests 193636; received 691.2 MiB
    Groups 145/191; images 5857/7924; HTTP requests 195483; received 692.1 MiB
    Groups 145/191; images 5857/7924; HTTP requests 197359; received 693.0 MiB
    Groups 145/191; images 5857/7924; HTTP requests 199225; received 693.9 MiB
    Groups 145/191; images 5857/7924; HTTP requests 201064; received 694.8 MiB
    Groups 146/191; images 5900/7924; HTTP requests 202807; received 698.7 MiB
    Groups 146/191; images 5900/7924; HTTP requests 204686; received 699.6 MiB
    Groups 147/191; images 5937/7924; HTTP requests 205968; received 703.1 MiB
    Groups 148/191; images 5974/7924; HTTP requests 207542; received 707.5 MiB
    Groups 149/191; images 6017/7924; HTTP requests 209174; received 711.6 MiB
    Groups 149/191; images 6017/7924; HTTP requests 211033; received 712.5 MiB
    Groups 150/191; images 6054/7924; HTTP requests 212221; received 720.4 MiB
    Groups 151/191; images 6097/7924; HTTP requests 212954; received 727.4 MiB
    Groups 152/191; images 6140/7924; HTTP requests 212974; received 727.5 MiB
    Groups 153/191; images 6177/7924; HTTP requests 214412; received 732.6 MiB
    Groups 154/191; images 6220/7924; HTTP requests 214879; received 734.1 MiB
    Groups 155/191; images 6257/7924; HTTP requests 215932; received 739.5 MiB
    Groups 156/191; images 6300/7924; HTTP requests 216828; received 744.5 MiB
    Groups 157/191; images 6343/7924; HTTP requests 217701; received 751.6 MiB
    Groups 158/191; images 6386/7924; HTTP requests 218316; received 757.1 MiB
    Groups 159/191; images 6429/7924; HTTP requests 218366; received 757.4 MiB
    Groups 160/191; images 6472/7924; HTTP requests 219133; received 761.0 MiB
    Groups 161/191; images 6509/7924; HTTP requests 220053; received 775.3 MiB
    Groups 162/191; images 6552/7924; HTTP requests 220135; received 776.7 MiB
    Groups 163/191; images 6589/7924; HTTP requests 220221; received 778.3 MiB
    Groups 164/191; images 6632/7924; HTTP requests 220296; received 779.7 MiB
    Groups 165/191; images 6669/7924; HTTP requests 220898; received 787.9 MiB
    Groups 166/191; images 6712/7924; HTTP requests 221200; received 790.8 MiB
    Groups 167/191; images 6749/7924; HTTP requests 221420; received 791.6 MiB
    Groups 168/191; images 6786/7924; HTTP requests 222564; received 799.4 MiB
    Groups 169/191; images 6823/7924; HTTP requests 222911; received 802.0 MiB
    Groups 169/191; images 6823/7924; HTTP requests 224606; received 802.8 MiB
    Groups 169/191; images 6823/7924; HTTP requests 226297; received 803.7 MiB
    Groups 169/191; images 6823/7924; HTTP requests 228010; received 804.5 MiB
    Groups 169/191; images 6823/7924; HTTP requests 229709; received 805.3 MiB
    Groups 169/191; images 6823/7924; HTTP requests 231391; received 806.2 MiB
    Groups 169/191; images 6823/7924; HTTP requests 233084; received 808.3 MiB
    Groups 170/191; images 6860/7924; HTTP requests 233708; received 811.3 MiB
    Groups 170/191; images 6860/7924; HTTP requests 235319; received 816.3 MiB
    Groups 171/191; images 6897/7924; HTTP requests 235488; received 817.1 MiB
    Groups 171/191; images 6897/7924; HTTP requests 237036; received 817.9 MiB
    Groups 172/191; images 6934/7924; HTTP requests 237863; received 823.9 MiB
    Groups 172/191; images 6934/7924; HTTP requests 239309; received 829.3 MiB
    Groups 173/191; images 6982/7924; HTTP requests 239694; received 833.5 MiB
    Groups 174/191; images 7030/7924; HTTP requests 240316; received 838.2 MiB
    Groups 174/191; images 7030/7924; HTTP requests 241576; received 854.3 MiB
    Groups 175/191; images 7078/7924; HTTP requests 241784; received 858.9 MiB
    Groups 176/191; images 7126/7924; HTTP requests 241794; received 859.2 MiB
    Groups 177/191; images 7174/7924; HTTP requests 242079; received 865.3 MiB
    Groups 178/191; images 7222/7924; HTTP requests 242421; received 870.0 MiB
    Groups 179/191; images 7270/7924; HTTP requests 242710; received 875.9 MiB
    Groups 180/191; images 7277/7924; HTTP requests 242933; received 879.4 MiB
    Groups 181/191; images 7325/7924; HTTP requests 243082; received 881.2 MiB
    Groups 181/191; images 7325/7924; HTTP requests 243849; received 881.6 MiB
    Groups 182/191; images 7373/7924; HTTP requests 244455; received 900.1 MiB
    Groups 183/191; images 7414/7924; HTTP requests 244493; received 902.4 MiB
    Groups 184/191; images 7462/7924; HTTP requests 244493; received 902.5 MiB
    Groups 185/191; images 7469/7924; HTTP requests 244554; received 904.3 MiB
    Groups 186/191; images 7517/7924; HTTP requests 244653; received 907.9 MiB
    Groups 187/191; images 7565/7924; HTTP requests 244804; received 920.0 MiB
    Groups 188/191; images 7613/7924; HTTP requests 244832; received 922.4 MiB
    Groups 189/191; images 7661/7924; HTTP requests 244877; received 926.6 MiB
    Groups 190/191; images 7702/7924; HTTP requests 244882; received 927.1 MiB
    Groups 190/191; images 7702/7924; HTTP requests 244961; received 927.2 MiB
    Interrupted. Rerun the same command to reuse cached indexes and complete images.
    ✗ (130) • 53m 03s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import json
        p=Path('transfer_lists/web_download_report.json')
        d=json.loads(p.read_text())
        print('missing_URL_errors',sum(x['attempts'][0].get('error')=='No source URL in OCL metadata' for x in d['failures']))
        print('recent_failures',d['failures'][-2:])
        PY
    missing_URL_errors 706
    recent_failures [{'name': 'from_web/val_2499.jpg', 'url': 'http://www.mormonmissionprep.com/wp-content/uploads/2011/05/sheep-eating-from-hand-of-stranger.jpg', 'attempts': [{'url': 'https://www.mormonmissionprep.com/wp-content/uploads/2011/05/sheep-eating-from-hand-of-stranger.jpg', 'attempt': 1, 'error': '403 Client Error: Forbidden for url: https://www.mormonmissionprep.com/wp-content/uploads/2011/05/sheep-eating-from-hand-of-stranger.jpg'}, {'url': 'http://www.mormonmissionprep.com/wp-content/uploads/2011/05/sheep-eating-from-hand-of-stranger.jpg', 'attempt': 1, 'error': '403 Client Error: Forbidden for url: http://www.mormonmissionprep.com/wp-content/uploads/2011/05/sheep-eating-from-hand-of-stranger.jpg'}]}, {'name': 'from_web/val_2503.jpg', 'url': None, 'attempts': [{'error': 'No source URL in OCL metadata'}]}]
    ✓ • 29ms

## Assistant

ImageNet 训练部分所需的 7,702 张原图已全部下载，累计接收约 927 MiB。还剩验证部分的 222 张；逐个读取其索引较慢，我正在改为分段并行扫描，继续复用已保存的进度。网页原图也已恢复了一部分。

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/download_selected_web.py
    @@ -14,3 +14,3 @@
     from download_imagenet_subset import atomic_write
    -from download_web_images import download_image
    +from download_web_images import IMAGE_ERRORS, download_image, validate_image
     
    @@ -41,2 +41,8 @@
             def fetch(name):
    +            if (root / name).is_file():
    +                try:
    +                    validate_image(root / name)
    +                    return name, "skipped", []
    +                except IMAGE_ERRORS:
    +                    pass
                 if name not in urls:

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/download_imagenet_subset.py
    @@ -10,2 +10,3 @@
     from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
    +import fcntl
     import io
    @@ -262,2 +263,80 @@
     
    +def process_val_partition(source, cache, start, end, requested, args):
    +    """Locate a checked tar header after a byte boundary, then scan this part."""
    +    first_header = None
    +    if cache.is_file():
    +        state = json.loads(cache.read_text(encoding="utf-8"))
    +        signature = state.get("signature", {})
    +        if (
    +            signature.get("source") == source.identity
    +            and signature.get("kind") == "val"
    +            and signature.get("scan_end") == end
    +            and start <= signature.get("start", -1) <= end
    +        ):
    +            first_header = signature["start"]
    +    if first_header is None:
    +        cursor = start
    +        while cursor + 512 <= end and first_header is None:
    +            block = source.read(cursor, min(256 * 1024, end - cursor))
    +            for relative in range(0, len(block) - 511, 512):
    +                header = block[relative:relative + 512]
    +                try:
    +                    member = parse_header(header)
    +                except (tarfile.TarError, ValueError, UnicodeError):
    +                    continue
    +                following = cursor + relative + 512 + ((member.size + 511) // 512) * 512
    +                if (
    +                    member.isfile() and PATTERNS["val"].fullmatch(member.name)
    +                    and 0 < member.size <= 128 * 1024 * 1024
    +                    and following + 512 <= source.size
    +                ):
    +                    # A checksum and the following header rule out JPEG payload
    +                    # bytes accidentally resembling a tar member at a boundary.
    +                    next_block = source.read(following, 512)
    +                    try:
    +                        next_member = None if next_block == bytes(512) else parse_header(next_block)
    +                    except (tarfile.TarError, ValueError, UnicodeError):
    +                        continue
    +                    if next_member is None or PATTERNS["val"].fullmatch(next_member.name):
    +                        first_header = cursor + relative
    +                        break
    +            cursor += len(block)
    +        if first_header is None:
    +            first_header = end
    +    return process_group(
    +        source, cache, first_header, end, source.size, "val", requested, args,
    +        512 if args.header_only else args.val_chunk_mib * 1024 * 1024,
    +    )
    +
    +
    +def val_jobs(source, requested, args):
    +    cache = args.index_dir / "val.json"
    +    legacy = json.loads(cache.read_text(encoding="utf-8")) if cache.is_file() else {}
    +    expected_signature = {
    +        "version": 1, "source": source.identity, "start": 0,
    +        "scan_end": source.size, "data_end": source.size, "kind": "val",
    +    }
    +    if legacy.get("signature") != expected_signature:
    +        legacy = {"cursor": 0, "members": {}, "complete": False}
    +    known = {name: path for name, path in requested.items() if name in legacy["members"]}
    +    jobs = []
    +    if known:
    +        jobs.append((process_group, source, cache, 0, source.size, source.size,
    +                     "val", known, args, 512))
    +    remaining = {name: path for name, path in requested.items() if name not in known}
    +    if remaining and not legacy["complete"]:
    +        start = legacy["cursor"]
    +        blocks = (source.size - start) // 512
    +        boundaries = [start + (blocks * part // args.val_parts) * 512
    +                      for part in range(args.val_parts + 1)]
    +        print(f"Validation: {len(known)} target offsets cached; "
    +              f"scanning the remainder in {args.val_parts} parts.", flush=True)
    +        for begin, end in zip(boundaries, boundaries[1:]):
    +            if begin < end:
    +                jobs.append((process_val_partition, source,
    +                             args.index_dir / "val_parts" / f"{begin}-{end}.json",
    +                             begin, end, remaining, args))
    +    return jobs
    +
    +
     def run(args) -> int:
    @@ -300,3 +379,3 @@
                 entry = outer[name]
    -            jobs.append((source, args.index_dir / "train" / f"{name}.json",
    +            jobs.append((process_group, source, args.index_dir / "train" / f"{name}.json",
                              entry["offset"], entry["offset"] + entry["size"],
    @@ -306,5 +385,3 @@
             source = RemoteArchive(client, args.val_url)
    -        jobs.append((source, args.index_dir / "val.json", 0, source.size, source.size,
    -                     "val", val, args,
    -                     512 if args.header_only else args.val_chunk_mib * 1024 * 1024))
    +        jobs.extend(val_jobs(source, val, args))
         found = {}
    @@ -313,3 +390,3 @@
         executor = ThreadPoolExecutor(max_workers=args.workers)
    -    pending = {executor.submit(process_group, *job) for job in jobs}
    +    pending = {executor.submit(job[0], *job[1:]) for job in jobs}
         last_progress = time.monotonic()
    @@ -369,2 +446,3 @@
         parser.add_argument("--val-chunk-mib", type=int, default=64)
    +    parser.add_argument("--val-parts", type=int, default=32)
         parser.add_argument("--limit", type=int, help="Use only the first N manifest entries for a smoke test")
    @@ -384,2 +462,3 @@
             or args.val_chunk_mib < 1
    +        or not 1 <= args.val_parts <= 128
         ):
    @@ -390,3 +469,9 @@
             setattr(args, name, getattr(args, name).expanduser().resolve())
    -    return run(args)
    +    args.index_dir.mkdir(parents=True, exist_ok=True)
    +    with (args.index_dir / "download.lock").open("a+") as lock:
    +        try:
    +            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    +        except BlockingIOError:
    +            raise ValueError("Another download is already using this index directory.")
    +        return run(args)
     

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import io,json,random,tarfile,tempfile,threading
        from pathlib import Path
        from types import SimpleNamespace
        from PIL import Image
        from download_imagenet_subset import val_jobs,parse_header
        rng=random.Random(8)
        items={}
        stream=io.BytesIO()
        with tarfile.open(fileobj=stream,mode='w') as tar:
         for i in range(47):
          pixels=rng.randbytes((32+i%9)*37*3)
          image=Image.frombytes('RGB',(32+i%9,37),pixels)
          out=io.BytesIO(); image.save(out,format='JPEG')
          name=f'ILSVRC2012_val_{i+1:08d}.JPEG'; items[name]=out.getvalue()
          member=tarfile.TarInfo(name);member.size=len(items[name]);tar.addfile(member,io.BytesIO(items[name]))
        class FakeSource:
         def __init__(self):
          self.content=stream.getvalue();self.size=len(self.content);self.identity={'url':'fixture','size':self.size,'etag':'fixture','last_modified':None};self.client=SimpleNamespace(stop=threading.Event());self.reads=0
         def read(self,offset,size):
          self.reads+=1
          assert 0<=offset<self.size and offset+size<=self.size
          return self.content[offset:offset+size]
        source=FakeSource()
        with tempfile.TemporaryDirectory(prefix='ocl-val-test-') as tmp:
         root=Path(tmp)
         args=SimpleNamespace(index_dir=root/'index',output_dir=root/'images',val_parts=16,header_only=True,val_chunk_mib=1,index_only=False)
         args.index_dir.mkdir()
         cursor=0;cached={}
         for i in range(8):
          member=parse_header(source.read(cursor,512));cached[member.name]={'offset':cursor+512,'size':member.size};cursor+=512+((member.size+511)//512)*512
         signature={'version':1,'source':source.identity,'start':0,'scan_end':source.size,'data_end':source.size,'kind':'val'}
         (args.index_dir/'val.json').write_text(json.dumps({'signature':signature,'cursor':cursor,'complete':False,'members':cached}))
         targets={n:'val/'+n for i,n in enumerate(items) if i%3==0}
         for iteration in range(2):
          seen={};new=old=0;before=source.reads
          for fn,*job_args in val_jobs(source,targets,args):
           found,n,o=fn(*job_args);assert not set(seen)&found.keys();seen.update(found);new+=n;old+=o
          assert seen.keys()==set(targets.values())
          assert all((args.output_dir/path).read_bytes()==items[name] for name,path in targets.items())
          if iteration==1: assert new==0 and old==len(targets) and source.reads==before
          print('partition_check',iteration,'selected',len(seen),'new',new,'existing',old,'reads',source.reads-before)
         damaged=args.output_dir/next(iter(targets.values()));damaged.write_bytes(b'x'*damaged.stat().st_size)
         for fn,*job_args in val_jobs(source,targets,args):fn(*job_args)
         assert damaged.read_bytes()==items[damaged.name]
         print('same_size_corruption_repaired')
        PY
    Validation: 3 target offsets cached; scanning the remainder in 16 parts.
    partition_check 0 selected 16 new 16 existing 0 reads 86
    Validation: 3 target offsets cached; scanning the remainder in 16 parts.
    partition_check 1 selected 16 new 0 existing 16 reads 0
    Validation: 3 target offsets cached; scanning the remainder in 16 parts.
    same_size_corruption_repaired
    ✓ • 519ms

## Activity

    $ rg --files resources
    resources/OCL_annot_val.pkl
    resources/OCL_class_object.json
    resources/OCL_annot_test.pkl
    resources/OCL_annot.tgz
    resources/category_aff_matrix.json
    resources/OCL_annot_train.pkl
    resources/causal_many_shot300.json
    resources/OCL_category_annot.json
    resources/OCL_class_affordance.json
    resources/OCL_class_attribute.json
    resources/OCL_weight.json
    resources/url_to_filename.json
    ✓ • 0ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        from urllib.parse import urlsplit
        import json
        r=json.loads(Path('transfer_lists/web_download_report.json').read_text())
        actual=[x for x in r['failures'] if x['url'] is not None]
        print('unresolved_web',len(actual))
        print('failed_domains',Counter(urlsplit(x['url']).netloc for x in actual).most_common(30))
        for x in actual[:14]: print(x['name'],x['url'],x['attempts'][-1]['error'][:180])
        for p in Path('resources').glob('*web*'):
         d=json.loads(p.read_text()); print('metadata',p,type(d).__name__,len(d));print(str(d)[:400])
        PY
    unresolved_web 215
    failed_domains [('images.freeimages.com', 35), ('hbimg.b0.upaiyun.com', 33), ('i.serengeseba.com', 15), ('dpic.tiankong.com', 12), ('i2.wp.com', 6), ('www.ecerimg.com', 5), ('img.qqzhi.com', 5), ('n1.itc.cn', 5), ('www.eautobazaar.com', 4), ('www.chinadaily.com.cn', 3), ('img.everychina.com', 3), ('ec4.images-amazon.com', 3), ('file.youboy.com', 2), ('up.deskbizhi.com', 2), ('en.pimg.jp', 2), ('img2.everychina.com', 2), ('up.36992.com', 2), ('d1yn1kh78jj1rr.cloudfront.net', 2), ('www.gannett-cdn.com', 2), ('img3.stockfresh.com', 2), ('api.meisupic.com', 2), ('img.zcool.cn', 2), ('media.buzzle.com', 2), ('www.cqjhqbfqc.com', 1), ('www.cn357.com', 1), ('ww4.sinaimg.cn', 1), ('bbsfiles.vivo.com.cn', 1), ('sm.fjsen.com', 1), ('images.takungpao.com', 1), ('www.petmrs.com', 1)]
    from_web/test_0004.jpg http://file.youboy.com/a/78/95/25/9/8688209s.jpg 404 Client Error: Not Found for url: http://file.youboy.com/a/78/95/25/9/8688209s.jpg
    from_web/test_0008.jpg http://www.cqjhqbfqc.com/data/images/product/thumb_20180423174300_297.jpg ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
    from_web/test_0014.jpg http://www.cn357.com/upload/article/images/3%28139%29.jpg ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
    from_web/test_0023.jpg http://ww4.sinaimg.cn/mw1024/a8ef5277jw1evyj5ij8uyj20c80icdgi.jpg 403 Client Error: Forbidden for url: http://ww4.sinaimg.cn/mw1024/a8ef5277jw1evyj5ij8uyj20c80icdgi.jpg
    from_web/test_0028.jpg http://dpic.tiankong.com/x3/hr/QJ8704927006.jpg ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
    from_web/test_0043.jpg http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201501/06/132053shdlga00hgd5zzhg.jpg 404 Client Error: Not Found for url: http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201501/06/132053shdlga00hgd5zzhg.jpg
    from_web/test_0051.jpg http://sm.fjsen.com/images/attachement/jpg/site2/20160201/1c6f65ee7f521819606d0a.JPG 404 Client Error: Not Found for url: http://sm.fjsen.com/images/attachement/jpg/site2/20160201/1c6f65ee7f521819606d0a.JPG
    from_web/test_0089.jpg http://images.takungpao.com/2016/0503/20160503025114758.jpg ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
    from_web/test_0145.jpg http://up.deskbizhi.com/pic_360/bf/d7/a2/bfd7a2367324fda3e1267f1342c4fd99.jpg 400 Client Error: Bad Request for url: https://up.deskbizhi.com/pic_360/bf/d7/a2/bfd7a2367324fda3e1267f1342c4fd99.jpg
    from_web/test_0155.jpg http://dpic.tiankong.com/d2/dx/QJ6914251622.jpg ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
    from_web/test_0159.jpg http://www.petmrs.com/uploads/allimg/140712/7-140G2115503101.JPG 404 Client Error: Not Found for url: http://www.pet501.com/uploads/allimg/140712/7-140G2115503101.JPG
    from_web/test_0164.jpg http://i.serengeseba.com/uploads/i_2_2424381015x2708060919_26.jpg cannot identify image file '/home/linfu/src/Test/ObjectConceptLearning/data/from_web/.test_0164.jpg.99dkvuhw.part'
    from_web/test_0235.jpg http://www.ecerimg.com/nimg/84/56/6389f24e922af0051c94c33cc855.jpg 404 Client Error: Not Found for url: http://www.ecerimg.com/nimg/84/56/6389f24e922af0051c94c33cc855.jpg
    from_web/test_0236.jpg http://www.chinadaily.com.cn/china/images/attachement/jpg/site1/20101214/002170196e1c0e7176dc1d.jpg 404 Client Error: Not Found for url: http://www.chinadaily.com.cn/china/images/attachement/jpg/site1/20101214/002170196e1c0e7176dc1d.jpg
    ✓ • 0ms

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/audit_test_data.py
    """Validate all OCL top-ten test images and create a minimal transfer manifest."""
    
    from __future__ import annotations
    
    import argparse
    from collections import Counter, defaultdict
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from datetime import datetime, timezone
    import hashlib
    import io
    import json
    import math
    from pathlib import Path, PurePosixPath
    import pickle
    import tempfile
    
    from PIL import Image
    
    
    def save(path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as handle:
            handle.write(text)
            temporary = Path(handle.name)
        temporary.replace(path)
    
    
    def audit(root: Path, workers: int) -> dict:
        resources = root / "resources"
        vocabulary = {
            kind: json.loads((resources / f"OCL_class_{kind}.json").read_text())
            for kind in ("object", "attribute", "affordance")
        }
        annotations = []
        for split in ("train", "val", "test"):
            with (resources / f"OCL_annot_{split}.pkl").open("rb") as handle:
                annotations.extend(pickle.load(handle))
        counts = Counter(obj["obj"] for row in annotations for obj in row["objects"])
        selected = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:10])
        if len(selected) != 10 or not set(selected).issubset(vocabulary["object"]):
            raise ValueError("Invalid category vocabulary or fewer than ten categories")
        objects = defaultdict(list)
        excluded = []
        label_errors = []
        selected_count = 0
        for row in annotations:
            name = row["name"]
            parts = PurePosixPath(name)
            if parts.is_absolute() or ".." in parts.parts or "\n" in name:
                raise ValueError(f"Unsafe image path: {name!r}")
            for index, obj in enumerate(row["objects"]):
                if obj["obj"] not in selected:
                    continue
                selected_count += 1
                objects[name]
                box = obj.get("box")
                if box is not None and (
                    len(box) != 4 or not all(math.isfinite(value) for value in box)
                    or box[2] <= box[0] or box[3] <= box[1]
                ):
                    excluded.append({"image_name": name, "object_index": index,
                                     "category": obj["obj"], "box": list(box)})
                    continue
                for field, kind in (("attr", "attribute"), ("aff", "affordance")):
                    if any(not isinstance(i, int) or not 0 <= i < len(vocabulary[kind])
                           for i in obj[field]):
                        label_errors.append({"image_name": name, "object_index": index,
                                             "field": field, "ids": obj[field]})
                objects[name].append((index, obj))
        names = sorted(objects)
        reports = root / "transfer_lists"
        expected = set((reports / "ocl_non_imagenet.txt").read_text().splitlines())
        expected.update("ImageNet/" + name for name in
                        (reports / "imagenet_required.txt").read_text().splitlines())
        if expected != set(names):
            raise ValueError("Existing transfer manifests disagree with the annotation selection")
    
        def inspect(name):
            path = root / name
            result = {"name": name}
            if not path.is_file():
                return {**result, "status": "missing"}
            try:
                content = path.read_bytes()
                with Image.open(io.BytesIO(content)) as image:
                    image.load()
                    width, height = image.size
                    image.convert("RGB")
                result.update(size_bytes=len(content), width=width, height=height,
                              sha256=hashlib.sha256(content).hexdigest())
                crop_errors = []
                for index, obj in objects[name]:
                    box = obj.get("box", (0, 0, width, height))
                    left, top, right, bottom = box
                    if min(width, right) <= max(0, left) or min(height, bottom) <= max(0, top):
                        crop_errors.append({"object_index": index, "box": list(box),
                                            "category": obj["obj"]})
                return {**result, "status": "valid", "crop_errors": crop_errors}
            except (OSError, ValueError, SyntaxError, Image.DecompressionBombError) as error:
                return {**result, "status": "corrupt", "error": str(error)}
    
        results = {}
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(inspect, name) for name in names]
            for future in as_completed(futures):
                result = future.result()
                results[result["name"]] = result
                if len(results) % 5000 == 0:
                    print(f"Validated {len(results)}/{len(names)} images", flush=True)
        ordered = [results[name] for name in names]
        missing = [r["name"] for r in ordered if r["status"] == "missing"]
        corrupt = [r for r in ordered if r["status"] == "corrupt"]
        crop_errors = [{"image_name": r["name"], **error}
                       for r in ordered for error in r.get("crop_errors", [])]
        by_source = {}
        for source in sorted({name.split("/")[0] for name in names}):
            rows = [r for r in ordered if r["name"].startswith(source + "/")]
            by_source[source] = dict(Counter(r["status"] for r in rows))
            by_source[source]["required"] = len(rows)
        ready = not (missing or corrupt or crop_errors or label_errors)
        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "ready_for_full_evaluation": ready,
            "selection_splits": ["train", "val", "test"],
            "count_unit": "object_instance", "selected_categories": selected,
            "selected_objects": selected_count,
            "expected_evaluation_objects": selected_count - len(excluded),
            "objects_blocked_by_missing_or_corrupt_images": sum(
                len(objects[r["name"]]) for r in ordered if r["status"] != "valid"
            ),
            "required_images": len(names), "sources": by_source,
            "valid_image_bytes": sum(r.get("size_bytes", 0) for r in ordered if r["status"] == "valid"),
            "vocabulary_sizes": {key: len(value) for key, value in vocabulary.items()},
            "excluded_invalid_boxes": excluded,
            "missing_images": missing, "corrupt_images": corrupt,
            "crop_errors": crop_errors, "label_errors": label_errors,
            "transfer_manifest_keeps_missing_paths": True,
        }
        metadata = ["resources/OCL_annot_" + split + ".pkl" for split in ("train", "val", "test")]
        metadata += ["resources/OCL_class_" + kind + ".json" for kind in vocabulary]
        metadata += ["resources/url_to_filename.json"]
        save(reports / "test_images.txt", "\n".join(names) + "\n")
        save(reports / "test_data.txt", "\n".join(sorted(names + metadata)) + "\n")
        save(reports / "missing_images.txt", "".join(name + "\n" for name in missing))
        save(reports / "test_image_integrity.jsonl", "".join(json.dumps(r) + "\n" for r in ordered))
        checksums = [f"{r['sha256']}  {r['name']}\n" for r in ordered if r["status"] == "valid"]
        checksums += [f"{hashlib.sha256((root / name).read_bytes()).hexdigest()}  {name}\n"
                      for name in metadata]
        save(reports / "available_files.sha256", "".join(checksums))
        save(reports / "data_audit.json", json.dumps(report, indent=2) + "\n")
        print(json.dumps({key: value for key, value in report.items()
                          if key not in ("missing_images", "corrupt_images")}, indent=2))
        print(f"Report: {reports / 'data_audit.json'}")
        return report
    
    
    def main() -> int:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--data-root", type=Path, default=Path(__file__).resolve().parent)
        parser.add_argument("--workers", type=int, default=8)
        args = parser.parse_args()
        if not 1 <= args.workers <= 32:
            parser.error("Use 1..32 workers")
        report = audit(args.data_root.resolve(), args.workers)
        return 0 if report["ready_for_full_evaluation"] else 1
    
    
    if __name__ == "__main__":
        raise SystemExit(main())

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://huggingface.co/api/datasets?search=ObjectConceptLearning&limit=20'
    []
    ✓ • 626ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://drive.google.com/drive/folders/1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF' -o /tmp/ocl-official-drive.html
    ✓ • 961ms

## Assistant

已恢复 54 张缺失的网页原图，仍有 215 张下载失败，原因包括链接失效、403/404 和连接错误。我在查官方备份是否还有可用原图；完整测试清单会保留这些缺失项，校验报告也会明确标出它们对测试的影响。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import re
        s=Path('/tmp/ocl-official-drive.html').read_text()
        for term in ['from_web', 'tgz', 'OCL', '280569727']:
         matches=list(re.finditer(re.escape(term),s))
         print('term',term,'count',len(matches))
         for m in matches[:3]: print(s[max(0,m.start()-180):m.end()+180])
        PY
    term from_web count 8
     17.5523 14.5523 18 14 18H12V16Z" fill="white"/></g></svg></div></div></div></div></div><div class="rxUYqf" jsaction="error:piPPke" jsname="XJXImb"><div class="JxSEve" aria-label="from_web.tgz Compressed archive Shared" data-handled-by-drag-and-drop="true" ssk='5:auSv138:1TMAAvgRh7EmNvQu40lRIVD594LcDH2zy-0-16'><i role="presentation" class="cUCuw   upeNge vA3Shd" ssk
    ='6:by9fbe38:1TMAAvgRh7EmNvQu40lRIVD594LcDH2zy-0-16' data-id="1TMAAvgRh7EmNvQu40lRIVD594LcDH2zy" jsname="vtaz5c" data-tooltip-class="cAHxfe" data-tooltip-delay="500" data-tooltip="from_web.tgz Compressed archive"><span class="WQJtxb" ssk='5:xyMN01#0'><strong class="DNoYtb">from_web.tgz</strong></span></div><div data-title-inline="badges" class="egymZe"><div class="e
    y" jsname="vtaz5c" data-tooltip-class="cAHxfe" data-tooltip-delay="500" data-tooltip="from_web.tgz Compressed archive"><span class="WQJtxb" ssk='5:xyMN01#0'><strong class="DNoYtb">from_web.tgz</strong></span></div><div data-title-inline="badges" class="egymZe"><div class="eIs6Bc JCGPoc" jscontroller="YlnYEb" jsaction="click:FemtBc(preventDefault=true|x3ZoRb); keydow
    term tgz count 11
    14.5523 18 14 18H12V16Z" fill="white"/></g></svg></div></div></div></div></div><div class="rxUYqf" jsaction="error:piPPke" jsname="XJXImb"><div class="JxSEve" aria-label="from_web.tgz Compressed archive Shared" data-handled-by-drag-and-drop="true" ssk='5:auSv138:1TMAAvgRh7EmNvQu40lRIVD594LcDH2zy-0-16'><i role="presentation" class="cUCuw   upeNge vA3Shd" ssk='6:
    e38:1TMAAvgRh7EmNvQu40lRIVD594LcDH2zy-0-16' data-id="1TMAAvgRh7EmNvQu40lRIVD594LcDH2zy" jsname="vtaz5c" data-tooltip-class="cAHxfe" data-tooltip-delay="500" data-tooltip="from_web.tgz Compressed archive"><span class="WQJtxb" ssk='5:xyMN01#0'><strong class="DNoYtb">from_web.tgz</strong></span></div><div data-title-inline="badges" class="egymZe"><div class="eIs6B
    ="vtaz5c" data-tooltip-class="cAHxfe" data-tooltip-delay="500" data-tooltip="from_web.tgz Compressed archive"><span class="WQJtxb" ssk='5:xyMN01#0'><strong class="DNoYtb">from_web.tgz</strong></span></div><div data-title-inline="badges" class="egymZe"><div class="eIs6Bc JCGPoc" jscontroller="YlnYEb" jsaction="click:FemtBc(preventDefault=true|x3ZoRb); keydown:Fe
    term OCL count 2
    ent="telephone=no"><meta name="google" value="notranslate"><meta property="og:site_name" content="Google Drive"><meta name="viewport" content="width=1000, user-scalable=no"><title>OCL – Google Drive</title><script nonce="c4tgVMUGWT_XfxlNwvck5Q">
        var _DRIVE_numDumpException = 0;
        var _B_err = _DumpException = function(e) {
          _DRIVE_numDumpException++;
    tgVMUGWT_XfxlNwvck5Q">AF_initDataCallback({key: 'ds:0', hash: '1', data:["driveweb;Rtk8Cd;RxoWDf[\"1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF\"]",["1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF",null,"OCL","application/vnd.google-apps.folder",0,null,0,0,0,1699359515838,1699360209537,null,null,null,[[1,"17775965257817424521",null,null,null,null,0,null,null,null,"11264578587402587485
    term 280569727 count 2
    h7EmNvQu40lRIVD594LcDH2zy\x22,\x5b\x221MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF\x22\x5d,\x22from_web.tgz\x22,\x22application\/x-gzip\x22,0,null,0,0,0,1699360157647,1699359575000,null,null,280569727,\x5b\x5b1,\x2217775965257817424521\x22,null,null,null,null,0,null,null,null,\x22112645785874025874853\x22\x5d\x5d,null,\x5b1,\x2217775965257817424521\x22,null,null,null,null,0,nul
    785874025874853\x22\x5d\x5d,null,\x5b1,\x2217775965257817424521\x22,null,null,null,null,0,null,null,null,\x22112645785874025874853\x22\x5d,null,null,null,null,1,null,null,2,0,null,280569727,null,null,0,null,null,null,null,0,null,null,null,null,null,\x22DriveSdkV2\x22,null,0,\x22tgz\x22,null,null,null,null,null,null,null,null,null,null,null,null,null,null,\x5b\x5b1\x5
    ✓ • 198ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from concurrent.futures import ThreadPoolExecutor
        import json
        from PIL import Image
        p=Path('transfer_lists/web_download_report.json');d=json.loads(p.read_text())
        def check(entry):
         if entry['url'] is not None: return False
         try:
          with Image.open(entry['name']) as image:image.load()
          return True
         except Exception:return False
        with ThreadPoolExecutor(max_workers=8) as pool:flags=list(pool.map(check,d['failures']))
        recovered=sum(flags)
        d['skipped']+=recovered;d['failed']-=recovered;d['failures']=[x for x,valid in zip(d['failures'],flags) if not valid]
        d['note']='Existing archive-provided images have no URL; they were decoded and counted as skipped.'
        p.write_text(json.dumps(d,indent=2)+'\n')
        print({k:v for k,v in d.items() if k!='failures'})
        PY
    {'requested': 1474, 'downloaded': 54, 'skipped': 1205, 'failed': 215, 'pending': 0, 'note': 'Existing archive-provided images have no URL; they were decoded and counted as skipped.'}
    ✓ • 2.19s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B audit_test_data.py --workers 12
    Validated 5000/35633 images
    Validated 10000/35633 images
    Validated 15000/35633 images
    Validated 20000/35633 images
    Validated 25000/35633 images
    Validated 30000/35633 images
    Validated 35000/35633 images
    {
      "generated_at": "2026-10-22T18:28:14.319305+00:00",
      "ready_for_full_evaluation": false,
      "selection_splits": [
        "train",
        "val",
        "test"
      ],
      "count_unit": "object_instance",
      "selected_categories": {
        "dog": 16171,
        "bird": 13961,
        "sheep": 13821,
        "car": 11511,
        "motorcycle": 8519,
        "apple": 8382,
        "cattle": 8379,
        "broccoli": 8333,
        "truck": 7769,
        "elephant": 7032
      },
      "selected_objects": 103878,
      "expected_evaluation_objects": 103877,
      "objects_blocked_by_missing_or_corrupt_images": 559,
      "required_images": 35633,
      "sources": {
        "COCO": {
          "valid": 25067,
          "required": 25067
        },
        "ImageNet": {
          "valid": 7710,
          "missing": 214,
          "required": 7924
        },
        "aPY": {
          "valid": 1168,
          "required": 1168
        },
        "from_web": {
          "valid": 1259,
          "missing": 215,
          "required": 1474
        }
      },
      "valid_image_bytes": 5738617324,
      "vocabulary_sizes": {
        "object": 381,
        "attribute": 114,
        "affordance": 170
      },
      "excluded_invalid_boxes": [
        {
          "image_name": "COCO/val2014/COCO_val2014_000000315601.jpg",
          "object_index": 12,
          "category": "car",
          "box": [
            0,
            266,
            4,
            266
          ]
        }
      ],
      "crop_errors": [
        {
          "image_name": "ImageNet/train/n02089078/n02089078_178.JPEG",
          "object_index": 0,
          "box": [
            0.0,
            194.51502990722656,
            64.61176300048828,
            255.5253448486328
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02095314/n02095314_6284.JPEG",
          "object_index": 2,
          "box": [
            149,
            93,
            235,
            202
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02100735/n02100735_1090.JPEG",
          "object_index": 0,
          "box": [
            99,
            160,
            170,
            255
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02108000/n02108000_3426.JPEG",
          "object_index": 1,
          "box": [
            123.6557388305664,
            84.18275451660156,
            225.13156127929688,
            205.0046844482422
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n03796401/n03796401_5457.JPEG",
          "object_index": 1,
          "box": [
            90.1938247680664,
            167.32815551757812,
            199.00621032714844,
            251.77113342285156
          ],
          "category": "truck"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 2,
          "box": [
            183.3660888671875,
            214.6282196044922,
            246.3701171875,
            254.4662322998047
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 7,
          "box": [
            162.5959014892578,
            51.40813446044922,
            244.72694396972656,
            104.85037231445312
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 13,
          "box": [
            215.67884826660156,
            63.491458892822266,
            256.0,
            123.73628997802734
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 16,
          "box": [
            207.257080078125,
            173.25148010253906,
            256.0,
            254.88124084472656
          ],
          "category": "broccoli"
        },
        {
          "image_name": "from_web/val_2026.jpg",
          "object_index": 0,
          "box": [
            297,
            44,
            528,
            346
          ],
          "category": "elephant"
        }
      ],
      "label_errors": [],
      "transfer_manifest_keeps_missing_paths": true
    }
    Report: /home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/data_audit.json
    ✗ (1) • 1m 21s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import json
        from pathlib import Path
        from urllib.parse import urlsplit
        r=json.loads(Path('transfer_lists/web_download_report.json').read_text())
        for host in ['images.freeimages.com','hbimg.b0.upaiyun.com','i2.wp.com','ec4.images-amazon.com','en.pimg.jp','www.gannett-cdn.com']:
         for x in r['failures']:
          if urlsplit(x['url']).netloc==host:
           print(host, x);break
        PY
    images.freeimages.com {'name': 'from_web/test_0245.jpg', 'url': 'http://images.freeimages.com/images/premium/previews/2680/26808215-damaged-off-road-car.jpg', 'attempts': [{'url': 'https://images.freeimages.com/images/premium/previews/2680/26808215-damaged-off-road-car.jpg', 'attempt': 1, 'error': "HTTPSConnectionPool(host='images.freeimages.com', port=443): Max retries exceeded with url: /images/premium/previews/2680/26808215-damaged-off-road-car.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://images.freeimages.com/images/premium/previews/2680/26808215-damaged-off-road-car.jpg', 'attempt': 2, 'error': "HTTPSConnectionPool(host='images.freeimages.com', port=443): Max retries exceeded with url: /images/premium/previews/2680/26808215-damaged-off-road-car.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'http://images.freeimages.com/images/premium/previews/2680/26808215-damaged-off-road-car.jpg', 'attempt': 1, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}, {'url': 'http://images.freeimages.com/images/premium/previews/2680/26808215-damaged-off-road-car.jpg', 'attempt': 2, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}]}
    hbimg.b0.upaiyun.com {'name': 'from_web/test_0276.png', 'url': 'http://hbimg.b0.upaiyun.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658', 'attempts': [{'url': 'https://hbimg.b0.upaiyun.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658', 'attempt': 1, 'error': "HTTPSConnectionPool(host='hbimg.b0.upaiyun.com', port=443): Max retries exceeded with url: /daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://hbimg.b0.upaiyun.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658', 'attempt': 2, 'error': '405 Client Error: Not Allowed for url: https://hbimg.b0.upaiyun.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658'}, {'url': 'http://hbimg.b0.upaiyun.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658', 'attempt': 1, 'error': '405 Client Error: Not Allowed for url: http://hbimg.b0.upaiyun.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658'}]}
    i2.wp.com {'name': 'from_web/test_0286.png', 'url': 'http://i2.wp.com/braincharm.com/wp-content/uploads/2018/06/afadfafafaffafafafafaf.png?fit=751%2C422&ssl=1', 'attempts': [{'url': 'https://i2.wp.com/braincharm.com/wp-content/uploads/2018/06/afadfafafaffafafafafaf.png?fit=751%2C422&ssl=1', 'attempt': 1, 'error': '400 Client Error: Bad Request for url: https://i2.wp.com/braincharm.com/wp-content/uploads/2018/06/afadfafafaffafafafafaf.png?fit=751%2C422&ssl=1'}, {'url': 'http://i2.wp.com/braincharm.com/wp-content/uploads/2018/06/afadfafafaffafafafafaf.png?fit=751%2C422&ssl=1', 'attempt': 1, 'error': '400 Client Error: Bad Request for url: http://i2.wp.com/braincharm.com/wp-content/uploads/2018/06/afadfafafaffafafafafaf.png?fit=751%2C422&ssl=1'}]}
    ec4.images-amazon.com {'name': 'from_web/val_0750.jpg', 'url': 'http://ec4.images-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg', 'attempts': [{'url': 'https://ec4.images-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg', 'attempt': 1, 'error': "HTTPSConnectionPool(host='ec4.images-amazon.com', port=443): Max retries exceeded with url: /images/I/619cXR-XnyL._SL1004_.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'https://ec4.images-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg', 'attempt': 2, 'error': "HTTPSConnectionPool(host='ec4.images-amazon.com', port=443): Max retries exceeded with url: /images/I/619cXR-XnyL._SL1004_.jpg (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)')))"}, {'url': 'http://ec4.images-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg', 'attempt': 1, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}, {'url': 'http://ec4.images-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg', 'attempt': 2, 'error': "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"}]}
    en.pimg.jp {'name': 'from_web/test_0304.jpg', 'url': 'http://en.pimg.jp/025/639/868/1/25639868.jpg', 'attempts': [{'url': 'https://en.pimg.jp/025/639/868/1/25639868.jpg', 'attempt': 1, 'error': '403 Client Error: Forbidden for url: https://en.pimg.jp/025/639/868/1/25639868.jpg'}, {'url': 'http://en.pimg.jp/025/639/868/1/25639868.jpg', 'attempt': 1, 'error': '403 Client Error: Forbidden for url: http://en.pimg.jp/025/639/868/1/25639868.jpg'}]}
    www.gannett-cdn.com {'name': 'from_web/val_0781.png', 'url': 'http://www.gannett-cdn.com/presto/2019/03/13/PDTF/ba9b2dbb-f60b-4249-8fb5-cc9098c6a240-hsus_photo_466322.PNG', 'attempts': [{'url': 'https://www.gannett-cdn.com/presto/2019/03/13/PDTF/ba9b2dbb-f60b-4249-8fb5-cc9098c6a240-hsus_photo_466322.PNG', 'attempt': 1, 'error': '406 Client Error: Not Acceptable for url: https://www.gannett-cdn.com/presto/2019/03/13/PDTF/ba9b2dbb-f60b-4249-8fb5-cc9098c6a240-hsus_photo_466322.PNG'}, {'url': 'http://www.gannett-cdn.com/presto/2019/03/13/PDTF/ba9b2dbb-f60b-4249-8fb5-cc9098c6a240-hsus_photo_466322.PNG', 'attempt': 1, 'error': '406 Client Error: Not Acceptable for url: https://www.gannett-cdn.com/presto/2019/03/13/PDTF/ba9b2dbb-f60b-4249-8fb5-cc9098c6a240-hsus_photo_466322.PNG'}]}
    ✓ • 38ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://huggingface.co/api/datasets?search=object%20concept&limit=20'
    []
    ✓ • 349ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://archive.org/wayback/available?url=http%3A%2F%2Ffile.youboy.com%2Fa%2F78%2F95%2F25%2F9%2F8688209s.jpg&timestamp=20220101'
    {"url": "http://file.youboy.com/a/78/95/25/9/8688209s.jpg", "archived_snapshots": {}, "timestamp": "20220101"}
    ✓ • 2.79s

## Activity

    $ rg -n 'ImageNet|resize|box|image_size|im_size' ../dataset* ../datasets ../utils ../config ../extract_feature.py
    rg: ../dataset*: No such file or directory (os error 2)
    rg: ../datasets: No such file or directory (os error 2)
    ../extract_feature.py:34:            box_name = osp.splitext(osp.basename(args.box_file))[0]
    ../extract_feature.py:35:            feature_dir = f"features/OCL_{args.backbone_type}_{box_name}/"
    ../extract_feature.py:101:            "main_bbox": batch["main_bbox"],
    ../extract_feature.py:104:        if feed_batch["main_bbox"][0].size(0) > 0:
    ../extract_feature.py:105:            # print(feed_batch["main_bbox"][0].size(0), feed_batch["image"][0].size())
    ../extract_feature.py:136:            "main_bbox": batch["main_bbox"],
    ../extract_feature.py:139:        if feed_batch["main_bbox"][0].size(0) > 0:
    ../extract_feature.py:140:            # print(feed_batch["main_bbox"][0].size(0), feed_batch["image"][0].size())
    ../utils/utils.py:211:    parser.add_argument("--box_file", type=str,
    ../config/BaseConfig.yaml:4:box_file: null
    ../utils/dataset/OCL_dataset.py:79:        gt_box = []
    ../utils/dataset/OCL_dataset.py:89:            x = obj.get('box', [0, 0, image_width, image_height])
    ../utils/dataset/OCL_dataset.py:90:            gt_box.append(x)
    ../utils/dataset/OCL_dataset.py:98:            resize_trans = torchvision.transforms.Resize((image_width, image_height))
    ../utils/dataset/OCL_dataset.py:99:            image = resize_trans(image)
    ../utils/dataset/OCL_dataset.py:100:            gt_box = [(x[0] // 2, x[1] // 2, x[2] // 2, x[3] // 2) for x in gt_box]
    ../utils/dataset/OCL_dataset.py:107:            "gt_bbox": np.array(gt_box, dtype=np.float32),
    ../utils/dataset/OCL_dataset.py:114:        sample["main_bbox"] = sample["gt_bbox"]
    ✗ (2) • 0ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        import pickle,json
        from PIL import Image
        r=json.loads(Path('transfer_lists/data_audit.json').read_text());bad={x['image_name'] for x in r['crop_errors']}
        for sp in ['train','val','test']:
         with (Path('resources')/f'OCL_annot_{sp}.pkl').open('rb') as f:rows=pickle.load(f)
         for row in rows:
          if row['name'] in bad:
           with Image.open(row['name']) as im: print('IMAGE',row['name'],im.size,'metadata',{k:v for k,v in row.items() if k!='objects'},'boxes',[x.get('box') for x in row['objects'][:3]])
        print('url_bad_web',[(u,n) for u,n in json.loads(Path('resources/url_to_filename.json').read_text()) if n=='from_web/val_2026.jpg'])
        PY
    IMAGE ImageNet/train/n03796401/n03796401_5457.JPEG (150, 105) metadata {'name': 'ImageNet/train/n03796401/n03796401_5457.JPEG', 'source': 'ImageNet'} boxes [[42.82715606689453, 0.0, 254.22364044189453, 256.0], [90.1938247680664, 167.32815551757812, 199.00621032714844, 251.77113342285156]]
    IMAGE ImageNet/train/n02089078/n02089078_178.JPEG (150, 150) metadata {'name': 'ImageNet/train/n02089078/n02089078_178.JPEG', 'source': 'ImageNet'} boxes [[0.0, 194.51502990722656, 64.61176300048828, 255.5253448486328], [3.178721184866803, 5.714354147995902, 252.9336429163747, 245.79613602377094]]
    IMAGE ImageNet/train/n02108000/n02108000_3426.JPEG (89, 89) metadata {'name': 'ImageNet/train/n02108000/n02108000_3426.JPEG', 'source': 'ImageNet'} boxes [[0.0, 3.3160839080810547, 253.7186737060547, 255.99999809265137], [123.6557388305664, 84.18275451660156, 225.13156127929688, 205.0046844482422], [78.35487365722656, 27.581867218017578, 129.8728790283203, 93.8974494934082]]
    IMAGE ImageNet/train/n07715103/n07715103_12246.JPEG (158, 210) metadata {'name': 'ImageNet/train/n07715103/n07715103_12246.JPEG', 'source': 'ImageNet'} boxes [[0.0, 0.10208984464406967, 256.0, 255.99999328702688], [64.41463470458984, 207.3221893310547, 136.43153381347656, 254.8384246826172], [183.3660888671875, 214.6282196044922, 246.3701171875, 254.4662322998047]]
    IMAGE ImageNet/train/n02095314/n02095314_6284.JPEG (140, 140) metadata {'name': 'ImageNet/train/n02095314/n02095314_6284.JPEG', 'source': 'ImageNet'} boxes [[33, 88, 92, 193], [93, 95, 149, 203], [149, 93, 235, 202]]
    IMAGE from_web/val_2026.jpg (24, 24) metadata {'source': 'from_web', 'name': 'from_web/val_2026.jpg'} boxes [[297, 44, 528, 346]]
    IMAGE ImageNet/train/n02100735/n02100735_1090.JPEG (129, 97) metadata {'name': 'ImageNet/train/n02100735/n02100735_1090.JPEG', 'source': 'ImageNet'} boxes [[99, 160, 170, 255]]
    url_bad_web [('http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg', 'from_web/val_2026.jpg')]
    ✓ • 2.35s

## Activity

    $ cat ../utils/dataset/OCL_dataset.py
    from functools import lru_cache
    import sys
    import pickle
    
    assert sys.version.startswith('3'), "Python version >= 3.8"
    from PIL import Image
    import numpy as np
    import os, json
    import logging
    
    import torch, torchvision
    import torch.utils.data as tdata
    
    from . import data_utils
    
    class ImageDataset(tdata.Dataset):
        def __init__(self, phase):
            super(ImageDataset, self).__init__()
            self.logger = logging.getLogger(f"Dataset OCL")
            self.phase = phase
            self.transform = data_utils.imagenet_transform(phase)
    
            # reading annotation pickle
            pkl_dir = "data/resources"
    
            def load_pickle_and_assign_split(split):
                pkl_path = os.path.join(pkl_dir, f"OCL_annot_{split}.pkl")
                with open(pkl_path, 'rb') as fp:
                    pkl = pickle.load(fp)
                for x in pkl:
                    x['split'] = split
                return pkl
    
            if phase == "train":
                self.pkl_data = load_pickle_and_assign_split("train")
            else:
                self.pkl_data = load_pickle_and_assign_split("val") + \
                        load_pickle_and_assign_split("test")
    
            self.instance_indices = [(i, j) for i, img in enumerate(self.pkl_data) for j in range(len(img['objects']))]
            self.logger.info(f"{len(self.instance_indices)} instances")
    
            # construct attr/aff/obj list/matrix
            def load_class_json(name):
                with open(os.path.join(pkl_dir, f"OCL_class_{name}.json"), "r") as fp:
                    return json.load(fp)
    
            self.attrs = load_class_json("attribute")
            self.objs = load_class_json("object")
            self.affs = load_class_json("affordance")
            self.obj2id = {x: i for i, x in enumerate(self.objs)}
    
            with open('data/resources/category_aff_matrix.json', "r") as fp:
                aff_matrix_file = json.load(fp)
                assert self.objs == aff_matrix_file['objs']
                self.aff_matrix = np.array(aff_matrix_file["aff_matrix"])
    
            self.num_aff = self.aff_matrix.shape[1]
            self.num_attr = len(self.attrs)
            self.num_obj = len(self.objs)
    
            logging.info("#obj %d, #attr %d, #aff %d" % (
                self.num_obj, self.num_attr, self.num_aff))
    
    
        def __len__(self):
            return len(self.pkl_data)
    
        def __getitem__(self, index):
            info = self.pkl_data[index]
            objects = info["objects"]
            file_name = info["name"]
            file_path = os.path.join("data", file_name)
            image = Image.open(file_path).convert('RGB')
            image_width, image_height = image.size
    
            attr = []
            aff = []
            gt_box = []
            for obj in objects:
                a = torch.zeros([self.num_attr]).float()
                a[obj['attr']] = 1
                attr.append(a)
    
                b = torch.zeros([self.num_aff]).float()
                b[obj['aff']] = 1
                aff.append(b)
    
                x = obj.get('box', [0, 0, image_width, image_height])
                gt_box.append(x)
    
            attr = torch.stack(attr, 0)
            aff = torch.stack(aff, 0)
    
    
            if max(image_width, image_height) > 1800:
                image_width, image_height = image_width // 2, image_height // 2
                resize_trans = torchvision.transforms.Resize((image_width, image_height))
                image = resize_trans(image)
                gt_box = [(x[0] // 2, x[1] // 2, x[2] // 2, x[3] // 2) for x in gt_box]
            image = self.transform(image)
    
    
            sample = {
                "image": image,
                "file_name": file_name,
                "gt_bbox": np.array(gt_box, dtype=np.float32),
                'gt_aff': aff,
                "gt_attr": attr,
                'gt_obj_id': np.array([self.obj2id[obj['obj']] for obj in objects]),
                'val_mask': np.array([info['split'] == 'val' for _ in objects])
            }
    
            sample["main_bbox"] = sample["gt_bbox"]
    
            return sample
    
    
    
    class FeatureDataset(ImageDataset):
        def __init__(self, phase, feature_dir):
            super(FeatureDataset, self).__init__(phase)
    
            # reading feature .t7
            feature_path = os.path.join(feature_dir, f"{phase}.t7")
            logging.info("reading " + feature_path)
    
            # load features into memory
            self.features_list, self.feature_dim = data_utils.features_loader(feature_path, self.pkl_data)
    
        def __len__(self):
            return len(self.instance_indices)
    
        @lru_cache(maxsize=None)
        def __getitem__(self, index):
            imgId, instId = self.instance_indices[index]
            img = self.pkl_data[imgId]
            obj = img['objects'][instId]
    
            feature = self.features_list[imgId][instId, ...]
    
            obj_id = self.obj2id[obj['obj']]
    
            attr = torch.zeros([self.num_attr]).float()
            attr[obj['attr']] = 1
    
            aff = torch.zeros([self.num_aff]).float()
            aff[obj['aff']] = 1
    
    
            sample = {
                "image": feature,
                "gt_attr": attr,
                'gt_obj_id': np.array(obj_id, dtype=int),
                'gt_aff': aff,
            }
    
            # add val/test mask
            if 'split' in img:
                sample['val_mask'] = np.array(img['split'] == "val")
            sample['gt_causal'] = np.array(obj['causal'],dtype=int) if 'causal' in obj else []
    
            return sample
    ✓ • 0ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter,defaultdict
        import pickle
        stats=defaultdict(Counter);examples=defaultdict(list)
        for sp in ['train','val','test']:
         for row in pickle.load((Path('resources')/f'OCL_annot_{sp}.pkl').open('rb')):
          source=row['name'].split('/')[0]
          for obj in row['objects']:
           b=obj.get('box')
           if b:
            stats[source]['total']+=1;stats[source]['exceeds256']+=max(b)>256.001;stats[source]['equals256']+=abs(max(b)-256)<.01
        print(dict(stats))
        PY
    {'COCO': Counter({'total': 123863, 'exceeds256': 114311, 'equals256': 22}), 'ImageNet': Counter({'total': 38830, 'equals256': 17380, 'exceeds256': 231}), 'SUN': Counter({'total': 383, 'exceeds256': 382, 'equals256': 0}), 'aPY': Counter({'total': 6942, 'exceeds256': 5900, 'equals256': 10}), 'from_web': Counter({'total': 16636, 'exceeds256': 8486, 'equals256': 18})}
    ✓ • 2.32s

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://api.github.com/repos/silicx/ObjectConceptLearning/issues?state=all&per_page=100' -o /tmp/ocl-github-issues.json
    ✓ • 460ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import json, pickle
        from pathlib import Path
        from collections import Counter
        stats=Counter();examples=[]
        for sp in ['train','val','test']:
         for row in pickle.load((Path('resources')/f'OCL_annot_{sp}.pkl').open('rb')):
          if row['name'].startswith('ImageNet/'):
           kind=row['name'].split('/')[1]
           stats[kind+' images']+=1
           exceed=[o['box'] for o in row['objects'] if 'box' in o and max(o['box'])>256.001]
           if exceed:
            stats[kind+' images exceeds256']+=1
            if len(examples)<12: examples.append((row['name'],exceed[:2]))
        print(stats);print(examples)
        PY
    Counter({'train images': 27586, 'val images': 1000, 'train images exceeds256': 170, 'val images exceeds256': 51})
    [('ImageNet/train/n02412080/n02412080_14393.JPEG', [[4.0, 73.0, 222.0, 257.0], [90.0, 12.0, 257.0, 211.0]]), ('ImageNet/train/n02412080/n02412080_2918.JPEG', [[129.0, 186.0, 203.0, 257.0], [241.0, 187.0, 257.0, 254.0]]), ('ImageNet/train/n04507155/n04507155_16896.JPEG', [[186.0, 128.0, 257.0, 191.0], [139.0, 72.0, 257.0, 122.0]]), ('ImageNet/train/n04554684/n04554684_691.JPEG', [[181.0, 38.0, 257.0, 234.0]]), ('ImageNet/train/n07717410/n07717410_526.JPEG', [[114.0, 4.0, 260.0, 116.0]]), ('ImageNet/val/ILSVRC2012_val_00007569.JPEG', [[45, 44, 258, 254]]), ('ImageNet/val/ILSVRC2012_val_00022941.JPEG', [[6, 24, 257, 243]]), ('ImageNet/train/n01981276/n01981276_1907.JPEG', [[67, 123, 232, 257]]), ('ImageNet/train/n02256656/n02256656_14430.JPEG', [[4, 18, 237, 257]]), ('ImageNet/train/n02256656/n02256656_2804.JPEG', [[77, 2, 197, 257]]), ('ImageNet/train/n02403003/n02403003_8442.JPEG', [[20, 2, 233, 257]]), ('ImageNet/train/n02823428/n02823428_10847.JPEG', [[78, 13, 141, 257]])]
    ✓ • 6.03s

## Assistant

现有图片已完成首轮解码检查。还发现一个会影响测试的问题：部分 ImageNet 标注框超出原图尺寸，直接裁剪会报错；另有一张网页链接返回了 24×24 的小图，与标注明显不符。我正在核对官方记录并尝试恢复对应原图。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import json
        from pathlib import Path
        rows=json.loads(Path('/tmp/ocl-github-issues.json').read_text())
        for r in rows:
         print(r['number'],r['title'],r['comments_url'],r['comments'])
         if any(w in (r['title']+' '+(r['body'] or '')).lower() for w in ['imagenet','resize','bounding','256','image','data']):
          print((r['body'] or '')[:6500])
        PY
    3 f_oi https://api.github.com/repos/silicx/ObjectConceptLearning/issues/3/comments 3
    2 checkpoint choose https://api.github.com/repos/silicx/ObjectConceptLearning/issues/2/comments 4
    Dear Authors,
    
    Thanks for your reply! I have ignored the images whose contents are empty. However, I am uncertain about how to choose the appropriate checkpoint after completing phase 1 training. Could you please guide me on selecting between affordance mAP value and attribute mAP value? Additionally, can you explain the purpose of each of the three stages of training?
    
    
    The following is the result chart after I completed the first stage of training. Can you tell me how to select checkpoint? Thanks a lot!
    
    
    ![屏幕截图 2024-01-15 095832](https://github.com/silicx/ObjectConceptLearning/assets/103943036/3bf16418-beec-4510-b83d-ec3ba35ca861)
    
    1 Training Time https://api.github.com/repos/silicx/ObjectConceptLearning/issues/1/comments 7
    ✓ • 0ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://gd-hbimg.huaban.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658' -o /tmp/ocl-huaban-original-check
    curl: (22) The requested URL returned error: 403
    ✗ (22) • 27ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://m.media-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg' -o /tmp/ocl-amazon-original-check.jpg
    ✓ • 176ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://api.github.com/repos/silicx/ObjectConceptLearning/issues/1/comments' -o /tmp/ocl-issue1-comments.json
    ✓ • 358ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import json
        from pathlib import Path
        for r in json.loads(Path('/tmp/ocl-issue1-comments.json').read_text()):
         print('AUTHOR',r['user']['login'],'DATE',r['created_at']);print(r['body'])
        PY
    AUTHOR silicx DATE 2023-12-30T12:06:47Z
    Hi! The three-stage training takes ~13h with 4 TITAN Xp GPUs.
    AUTHOR yihang-xdu DATE 2024-01-02T09:30:16Z
    Dear Authors,
    
    Thanks for your reply! However, when I try to download images from the web, I've noticed that some images in the 'resources/url_to_filename.json' file have expired. Could you please provide the downloaded dataset ?
    
    AUTHOR silicx DATE 2024-01-03T08:20:27Z
    Hi, these images have been packed and available [here](https://drive.google.com/drive/folders/1MDBiw45vN4qvjOA8ZuGmJmFhjMVoSBnF?usp=share_link) (see Readme-Datasets). We have recently verified the remaining urls, though some images should be accessible via proper **network proxy**. Feel free to send us the failed urls if you still meet some network problems.
    AUTHOR yihang-xdu DATE 2024-01-04T11:02:07Z
    Dear Authors,
    
    Thanks for your reply! I still can't solve the download problem with some images. I have sent the failed urls to your email silicxuyue@sjtu.edu.cn. Thanks a lot!
    AUTHOR silicx DATE 2024-01-04T14:24:10Z
    I have sent these images and please check your inbox.
    AUTHOR yihang-xdu DATE 2024-01-04T23:32:20Z
    Dear Authors,
    
    Thanks for your help! I have received these pictures and checked them. Thanks again!
    AUTHOR yihang-xdu DATE 2024-01-11T07:28:17Z
    Dear Authors,
    
    I'm so sorry to bother you again. I found some problems with the downloaded pictures, so I sent an email to your mailbox, hoping to get your help. Thanks a lot!
    ✓ • 74ms

## Activity

    $ command -v pdftotext
    ✗ (1) • 59ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://hbimg.huaban.com/daf7f72d6a982baa2c1e3a6a01e34b39d52468a7de21-3sI1U6_fw658' -o /tmp/ocl-huaban-original-check
    curl: (22) The requested URL returned error: 403
    ✗ (22) • 78ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://arxiv.org/pdf/2212.02710' -o /tmp/ocl-paper.pdf
    ✓ • 1.09s

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/recover_web_images.py
    """Recover missing OCL web originals from their CDN alias or public archives."""
    
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import fcntl
    import io
    import json
    from pathlib import Path
    import pickle
    import threading
    from urllib.parse import urlsplit, urlunsplit
    
    from PIL import Image
    import requests
    
    from download_imagenet_subset import atomic_write
    
    
    def main():
        root = Path(__file__).resolve().parent
        reports = root / "transfer_lists"
        wanted = {n for n in (reports / "ocl_non_imagenet.txt").read_text().splitlines()
                  if n.startswith("from_web/")}
        categories = set(json.loads((reports / "selection.json").read_text())["selected_categories"])
        boxes = {}
        for split in ("train", "val", "test"):
            with (root / "resources" / f"OCL_annot_{split}.pkl").open("rb") as handle:
                for row in pickle.load(handle):
                    if row["name"] in wanted:
                        boxes.setdefault(row["name"], []).extend(
                            obj["box"] for obj in row["objects"]
                            if obj["obj"] in categories and "box" in obj
                        )
        urls = {name: url for url, name in
                json.loads((root / "resources/url_to_filename.json").read_text())}
    
        def validate(content, name):
            with Image.open(io.BytesIO(content)) as image:
                image.load()
                width, height = image.size
                for left, top, right, bottom in boxes.get(name, []):
                    if right > left and bottom > top and (
                        min(width, right) <= max(0, left) or min(height, bottom) <= max(0, top)
                    ):
                        raise ValueError("Image dimensions cannot contain an annotated object")
    
        pending = []
        for name in sorted(wanted):
            try:
                validate((root / name).read_bytes(), name)
            except (OSError, ValueError, SyntaxError, Image.DecompressionBombError):
                pending.append(name)
        local = threading.local()
    
        def recover(name):
            result = {"name": name, "original_url": urls.get(name), "attempts": []}
            if name not in urls:
                return {**result, "status": "unavailable", "error": "No URL in official mapping"}
            if not hasattr(local, "session"):
                local.session = requests.Session()
                local.session.headers["User-Agent"] = "Mozilla/5.0 (compatible; OCL-image-recovery/1.0)"
            session = local.session
    
            def fetch_image(url):
                try:
                    with session.get(url, stream=True, timeout=(8, 15)) as response:
                        response.raise_for_status()
                        content = bytearray()
                        for block in response.iter_content(65536):
                            content.extend(block)
                            if len(content) > 32 * 1024 * 1024:
                                raise ValueError("Image response exceeds 32 MiB")
                    validate(content, name)
                    atomic_write(root / name, content)
                    result.update(status="recovered", recovered_from=url, size_bytes=len(content))
                    return True
                except (requests.RequestException, OSError, ValueError, SyntaxError,
                        Image.DecompressionBombError) as error:
                    result["attempts"].append({"url": url, "error": str(error)})
                    return False
    
            parts = urlsplit(urls[name])
            if parts.netloc.endswith(".images-amazon.com"):
                alias = urlunsplit(("https", "m.media-amazon.com", parts.path, parts.query, ""))
                if fetch_image(alias):
                    return result
            # Request an archived copy of this exact original URL, preserving the
            # annotated image identity rather than substituting a similar photo.
            try:
                response = session.get("https://archive.org/wayback/available",
                                       params={"url": urls[name], "timestamp": "20220101"},
                                       timeout=(8, 15))
                response.raise_for_status()
                snapshot = response.json().get("archived_snapshots", {}).get("closest")
                if snapshot and snapshot.get("available") and str(snapshot.get("status")) == "200":
                    stamp = snapshot["timestamp"]
                    if not stamp.isdigit():
                        raise ValueError("Invalid archive timestamp")
                    archived = f"https://web.archive.org/web/{stamp}id_/{urls[name]}"
                    result["snapshot"] = snapshot
                    if fetch_image(archived):
                        return result
                else:
                    result["attempts"].append({"source": "Internet Archive", "error": "No snapshot available"})
            except (requests.RequestException, ValueError) as error:
                result["attempts"].append({"source": "Internet Archive", "error": str(error)})
            return {**result, "status": "unavailable"}
    
        with (reports / "web_download.lock").open("a+") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise SystemExit("Another selected-web download is running")
            results = []
            with ThreadPoolExecutor(max_workers=6) as pool:
                futures = [pool.submit(recover, name) for name in pending]
                for future in as_completed(futures):
                    results.append(future.result())
                    report = {"requested": len(pending),
                              "recovered": sum(r["status"] == "recovered" for r in results),
                              "pending": len(pending) - len(results),
                              "results": sorted(results, key=lambda r: r["name"])}
                    atomic_write(reports / "web_recovery_report.json",
                                 (json.dumps(report, indent=2) + "\n").encode())
                    if len(results) % 10 == 0 or len(results) == len(pending):
                        print(f"Recovery {len(results)}/{len(pending)}; recovered {report['recovered']}", flush=True)
            return 1 if any(r["status"] == "unavailable" for r in results) else 0
    
    
    if __name__ == "__main__":
        raise SystemExit(main())

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B download_imagenet_subset.py --header-only --workers 32 --val-parts 32 --timeout 20 --retries 3
    Indexing outer training tar for 190 required classes...
    Required training class archives total 25.00 GiB.
    Indexing headers only: low bandwidth, but many HTTP requests.
    Validation: 8 target offsets cached; scanning the remainder in 32 parts.
    Groups 1/223; images 37/7924; HTTP requests 2; received 0.0 MiB
    Groups 2/223; images 74/7924; HTTP requests 2; received 0.0 MiB
    Groups 4/223; images 154/7924; HTTP requests 2; received 0.0 MiB
    Groups 5/223; images 191/7924; HTTP requests 2; received 0.0 MiB
    Groups 6/223; images 228/7924; HTTP requests 2; received 0.0 MiB
    Groups 7/223; images 265/7924; HTTP requests 2; received 0.0 MiB
    Groups 8/223; images 302/7924; HTTP requests 2; received 0.0 MiB
    Groups 9/223; images 339/7924; HTTP requests 2; received 0.0 MiB
    Groups 10/223; images 382/7924; HTTP requests 2; received 0.0 MiB
    Groups 11/223; images 419/7924; HTTP requests 2; received 0.0 MiB
    Groups 13/223; images 493/7924; HTTP requests 2; received 0.0 MiB
    Groups 15/223; images 573/7924; HTTP requests 2; received 0.0 MiB
    Groups 16/223; images 616/7924; HTTP requests 2; received 0.0 MiB
    Groups 17/223; images 659/7924; HTTP requests 2; received 0.0 MiB
    Groups 18/223; images 696/7924; HTTP requests 2; received 0.0 MiB
    Groups 19/223; images 739/7924; HTTP requests 2; received 0.0 MiB
    Groups 20/223; images 782/7924; HTTP requests 2; received 0.0 MiB
    Groups 21/223; images 825/7924; HTTP requests 2; received 0.0 MiB
    Groups 22/223; images 868/7924; HTTP requests 2; received 0.0 MiB
    Groups 23/223; images 911/7924; HTTP requests 2; received 0.0 MiB
    Groups 24/223; images 954/7924; HTTP requests 2; received 0.0 MiB
    Groups 26/223; images 1040/7924; HTTP requests 2; received 0.0 MiB
    Groups 27/223; images 1083/7924; HTTP requests 2; received 0.0 MiB
    Groups 28/223; images 1126/7924; HTTP requests 2; received 0.0 MiB
    Groups 29/223; images 1169/7924; HTTP requests 2; received 0.0 MiB
    Groups 30/223; images 1212/7924; HTTP requests 2; received 0.0 MiB
    Groups 32/223; images 1298/7924; HTTP requests 2; received 0.0 MiB
    Groups 33/223; images 1335/7924; HTTP requests 2; received 0.0 MiB
    Groups 34/223; images 1378/7924; HTTP requests 2; received 0.0 MiB
    Groups 35/223; images 1415/7924; HTTP requests 2; received 0.0 MiB
    Groups 36/223; images 1452/7924; HTTP requests 2; received 0.0 MiB
    Groups 37/223; images 1489/7924; HTTP requests 2; received 0.0 MiB
    Groups 39/223; images 1563/7924; HTTP requests 2; received 0.0 MiB
    Groups 40/223; images 1606/7924; HTTP requests 2; received 0.0 MiB
    Groups 41/223; images 1643/7924; HTTP requests 2; received 0.0 MiB
    Groups 42/223; images 1680/7924; HTTP requests 2; received 0.0 MiB
    Groups 43/223; images 1723/7924; HTTP requests 2; received 0.0 MiB
    Groups 45/223; images 1797/7924; HTTP requests 2; received 0.0 MiB
    Groups 46/223; images 1840/7924; HTTP requests 2; received 0.0 MiB
    Groups 47/223; images 1877/7924; HTTP requests 2; received 0.0 MiB
    Groups 48/223; images 1920/7924; HTTP requests 2; received 0.0 MiB
    Groups 49/223; images 1957/7924; HTTP requests 2; received 0.0 MiB
    Groups 50/223; images 1994/7924; HTTP requests 2; received 0.0 MiB
    Groups 52/223; images 2068/7924; HTTP requests 2; received 0.0 MiB
    Groups 53/223; images 2111/7924; HTTP requests 2; received 0.0 MiB
    Groups 54/223; images 2154/7924; HTTP requests 2; received 0.0 MiB
    Groups 55/223; images 2197/7924; HTTP requests 2; received 0.0 MiB
    Groups 56/223; images 2234/7924; HTTP requests 2; received 0.0 MiB
    Groups 57/223; images 2277/7924; HTTP requests 2; received 0.0 MiB
    Groups 58/223; images 2320/7924; HTTP requests 2; received 0.0 MiB
    Groups 59/223; images 2363/7924; HTTP requests 2; received 0.0 MiB
    Groups 61/223; images 2443/7924; HTTP requests 2; received 0.0 MiB
    Groups 62/223; images 2486/7924; HTTP requests 2; received 0.0 MiB
    Groups 63/223; images 2529/7924; HTTP requests 2; received 0.0 MiB
    Groups 64/223; images 2572/7924; HTTP requests 2; received 0.0 MiB
    Groups 65/223; images 2609/7924; HTTP requests 2; received 0.0 MiB
    Groups 66/223; images 2646/7924; HTTP requests 2; received 0.0 MiB
    Groups 67/223; images 2683/7924; HTTP requests 2; received 0.0 MiB
    Groups 68/223; images 2720/7924; HTTP requests 2; received 0.0 MiB
    Groups 69/223; images 2757/7924; HTTP requests 2; received 0.0 MiB
    Groups 70/223; images 2794/7924; HTTP requests 2; received 0.0 MiB
    Groups 71/223; images 2831/7924; HTTP requests 2; received 0.0 MiB
    Groups 73/223; images 2905/7924; HTTP requests 2; received 0.0 MiB
    Groups 74/223; images 2942/7924; HTTP requests 2; received 0.0 MiB
    Groups 75/223; images 2985/7924; HTTP requests 2; received 0.0 MiB
    Groups 76/223; images 3022/7924; HTTP requests 2; received 0.0 MiB
    Groups 77/223; images 3059/7924; HTTP requests 2; received 0.0 MiB
    Groups 79/223; images 3133/7924; HTTP requests 2; received 0.0 MiB
    Groups 80/223; images 3176/7924; HTTP requests 2; received 0.0 MiB
    Groups 81/223; images 3213/7924; HTTP requests 2; received 0.0 MiB
    Groups 83/223; images 3293/7924; HTTP requests 2; received 0.0 MiB
    Groups 84/223; images 3330/7924; HTTP requests 2; received 0.0 MiB
    Groups 85/223; images 3367/7924; HTTP requests 2; received 0.0 MiB
    Groups 86/223; images 3404/7924; HTTP requests 2; received 0.0 MiB
    Groups 88/223; images 3490/7924; HTTP requests 2; received 0.0 MiB
    Groups 89/223; images 3533/7924; HTTP requests 2; received 0.0 MiB
    Groups 90/223; images 3576/7924; HTTP requests 2; received 0.0 MiB
    Groups 91/223; images 3619/7924; HTTP requests 2; received 0.0 MiB
    Groups 92/223; images 3662/7924; HTTP requests 2; received 0.0 MiB
    Groups 93/223; images 3705/7924; HTTP requests 2; received 0.0 MiB
    Groups 94/223; images 3748/7924; HTTP requests 2; received 0.0 MiB
    Groups 95/223; images 3791/7924; HTTP requests 2; received 0.0 MiB
    Groups 96/223; images 3828/7924; HTTP requests 2; received 0.0 MiB
    Groups 97/223; images 3871/7924; HTTP requests 2; received 0.0 MiB
    Groups 98/223; images 3908/7924; HTTP requests 2; received 0.0 MiB
    Groups 99/223; images 3951/7924; HTTP requests 2; received 0.0 MiB
    Groups 100/223; images 3988/7924; HTTP requests 2; received 0.0 MiB
    Groups 102/223; images 4062/7924; HTTP requests 2; received 0.0 MiB
    Groups 103/223; images 4105/7924; HTTP requests 2; received 0.0 MiB
    Groups 104/223; images 4142/7924; HTTP requests 2; received 0.0 MiB
    Groups 106/223; images 4222/7924; HTTP requests 2; received 0.0 MiB
    Groups 107/223; images 4265/7924; HTTP requests 2; received 0.0 MiB
    Groups 108/223; images 4302/7924; HTTP requests 2; received 0.0 MiB
    Groups 109/223; images 4339/7924; HTTP requests 2; received 0.0 MiB
    Groups 110/223; images 4382/7924; HTTP requests 2; received 0.0 MiB
    Groups 111/223; images 4425/7924; HTTP requests 2; received 0.0 MiB
    Groups 112/223; images 4468/7924; HTTP requests 2; received 0.0 MiB
    Groups 113/223; images 4511/7924; HTTP requests 2; received 0.0 MiB
    Groups 115/223; images 4597/7924; HTTP requests 2; received 0.0 MiB
    Groups 116/223; images 4640/7924; HTTP requests 2; received 0.0 MiB
    Groups 117/223; images 4683/7924; HTTP requests 2; received 0.0 MiB
    Groups 118/223; images 4726/7924; HTTP requests 2; received 0.0 MiB
    Groups 119/223; images 4769/7924; HTTP requests 2; received 0.0 MiB
    Groups 120/223; images 4812/7924; HTTP requests 2; received 0.0 MiB
    Groups 121/223; images 4855/7924; HTTP requests 2; received 0.0 MiB
    Groups 122/223; images 4898/7924; HTTP requests 2; received 0.0 MiB
    Groups 123/223; images 4941/7924; HTTP requests 2; received 0.0 MiB
    Groups 124/223; images 4984/7924; HTTP requests 2; received 0.0 MiB
    Groups 126/223; images 5070/7924; HTTP requests 2; received 0.0 MiB
    Groups 127/223; images 5113/7924; HTTP requests 2; received 0.0 MiB
    Groups 128/223; images 5150/7924; HTTP requests 2; received 0.0 MiB
    Groups 129/223; images 5193/7924; HTTP requests 2; received 0.0 MiB
    Groups 130/223; images 5236/7924; HTTP requests 2; received 0.0 MiB
    Groups 132/223; images 5310/7924; HTTP requests 2; received 0.0 MiB
    Groups 133/223; images 5347/7924; HTTP requests 2; received 0.0 MiB
    Groups 134/223; images 5384/7924; HTTP requests 2; received 0.0 MiB
    Groups 135/223; images 5427/7924; HTTP requests 2; received 0.0 MiB
    Groups 136/223; images 5470/7924; HTTP requests 2; received 0.0 MiB
    Groups 137/223; images 5507/7924; HTTP requests 2; received 0.0 MiB
    Groups 138/223; images 5550/7924; HTTP requests 2; received 0.0 MiB
    Groups 139/223; images 5593/7924; HTTP requests 2; received 0.0 MiB
    Groups 140/223; images 5630/7924; HTTP requests 2; received 0.0 MiB
    Groups 141/223; images 5667/7924; HTTP requests 2; received 0.0 MiB
    Groups 142/223; images 5710/7924; HTTP requests 2; received 0.0 MiB
    Groups 143/223; images 5753/7924; HTTP requests 2; received 0.0 MiB
    Groups 144/223; images 5796/7924; HTTP requests 2; received 0.0 MiB
    Groups 145/223; images 5839/7924; HTTP requests 2; received 0.0 MiB
    Groups 146/223; images 5882/7924; HTTP requests 2; received 0.0 MiB
    Groups 147/223; images 5925/7924; HTTP requests 2; received 0.0 MiB
    Groups 149/223; images 5999/7924; HTTP requests 2; received 0.0 MiB
    Groups 150/223; images 6042/7924; HTTP requests 2; received 0.0 MiB
    Groups 151/223; images 6085/7924; HTTP requests 2; received 0.0 MiB
    Groups 152/223; images 6128/7924; HTTP requests 2; received 0.0 MiB
    Groups 153/223; images 6171/7924; HTTP requests 2; received 0.0 MiB
    Groups 154/223; images 6214/7924; HTTP requests 2; received 0.0 MiB
    Groups 155/223; images 6257/7924; HTTP requests 2; received 0.0 MiB
    Groups 156/223; images 6300/7924; HTTP requests 2; received 0.0 MiB
    Groups 157/223; images 6343/7924; HTTP requests 2; received 0.0 MiB
    Groups 159/223; images 6393/7924; HTTP requests 2; received 0.0 MiB
    Groups 160/223; images 6400/7924; HTTP requests 3; received 0.0 MiB
    Groups 161/223; images 6437/7924; HTTP requests 5; received 0.0 MiB
    Groups 162/223; images 6480/7924; HTTP requests 5; received 0.0 MiB
    Groups 163/223; images 6517/7924; HTTP requests 7; received 0.0 MiB
    Groups 164/223; images 6560/7924; HTTP requests 8; received 0.0 MiB
    Groups 165/223; images 6597/7924; HTTP requests 8; received 0.0 MiB
    Groups 166/223; images 6634/7924; HTTP requests 10; received 0.0 MiB
    Groups 167/223; images 6671/7924; HTTP requests 11; received 0.0 MiB
    Groups 168/223; images 6714/7924; HTTP requests 12; received 0.0 MiB
    Groups 169/223; images 6757/7924; HTTP requests 13; received 0.0 MiB
    Groups 170/223; images 6794/7924; HTTP requests 14; received 0.0 MiB
    Groups 171/223; images 6831/7924; HTTP requests 15; received 0.0 MiB
    Groups 172/223; images 6868/7924; HTTP requests 16; received 0.0 MiB
    Groups 173/223; images 6905/7924; HTTP requests 16; received 0.0 MiB
    Groups 174/223; images 6948/7924; HTTP requests 17; received 0.0 MiB
    Groups 175/223; images 6989/7924; HTTP requests 19; received 0.0 MiB
    Groups 176/223; images 7037/7924; HTTP requests 19; received 0.0 MiB
    Groups 177/223; images 7085/7924; HTTP requests 21; received 0.0 MiB
    Groups 178/223; images 7133/7924; HTTP requests 22; received 0.0 MiB
    Groups 179/223; images 7181/7924; HTTP requests 23; received 0.0 MiB
    Groups 180/223; images 7229/7924; HTTP requests 24; received 0.0 MiB
    Groups 181/223; images 7277/7924; HTTP requests 25; received 0.0 MiB
    Groups 182/223; images 7325/7924; HTTP requests 25; received 0.0 MiB
    Groups 184/223; images 7421/7924; HTTP requests 28; received 0.0 MiB
    Groups 185/223; images 7462/7924; HTTP requests 28; received 0.0 MiB
    Groups 186/223; images 7510/7924; HTTP requests 30; received 0.0 MiB
    Groups 187/223; images 7558/7924; HTTP requests 31; received 0.0 MiB
    Groups 188/223; images 7606/7924; HTTP requests 31; received 0.0 MiB
    Groups 189/223; images 7654/7924; HTTP requests 32; received 0.0 MiB
    Groups 190/223; images 7702/7924; HTTP requests 33; received 0.0 MiB
    Groups 191/223; images 7710/7924; HTTP requests 94; received 4.0 MiB
    Groups 191/223; images 7710/7924; HTTP requests 2471; received 11.1 MiB
    Groups 191/223; images 7710/7924; HTTP requests 4939; received 12.3 MiB
    Groups 191/223; images 7710/7924; HTTP requests 7378; received 13.5 MiB
    Groups 191/223; images 7710/7924; HTTP requests 9842; received 14.7 MiB
    Groups 191/223; images 7710/7924; HTTP requests 12352; received 16.0 MiB
    Groups 191/223; images 7710/7924; HTTP requests 14750; received 17.1 MiB
    Groups 191/223; images 7710/7924; HTTP requests 17172; received 18.3 MiB
    Groups 191/223; images 7710/7924; HTTP requests 19579; received 19.5 MiB
    Groups 191/223; images 7710/7924; HTTP requests 22065; received 20.7 MiB
    Groups 191/223; images 7710/7924; HTTP requests 24524; received 21.9 MiB
    Groups 191/223; images 7710/7924; HTTP requests 26963; received 23.1 MiB
    Groups 191/223; images 7710/7924; HTTP requests 29397; received 24.3 MiB
    Groups 191/223; images 7710/7924; HTTP requests 31893; received 25.5 MiB
    Groups 191/223; images 7710/7924; HTTP requests 34324; received 26.7 MiB
    Groups 192/223; images 7712/7924; HTTP requests 34612; received 27.3 MiB
    Groups 192/223; images 7712/7924; HTTP requests 36975; received 28.5 MiB
    Groups 193/223; images 7716/7924; HTTP requests 38030; received 29.7 MiB
    Groups 194/223; images 7724/7924; HTTP requests 39008; received 31.5 MiB
    Groups 195/223; images 7728/7924; HTTP requests 39861; received 32.5 MiB
    Groups 196/223; images 7736/7924; HTTP requests 41401; received 34.2 MiB
    Groups 197/223; images 7740/7924; HTTP requests 42090; received 35.7 MiB
    Groups 198/223; images 7750/7924; HTTP requests 42245; received 36.7 MiB
    Groups 199/223; images 7758/7924; HTTP requests 42423; received 37.4 MiB
    Groups 200/223; images 7758/7924; HTTP requests 42488; received 37.5 MiB
    Groups 201/223; images 7764/7924; HTTP requests 42916; received 38.6 MiB
    Groups 202/223; images 7774/7924; HTTP requests 43652; received 39.9 MiB
    Groups 203/223; images 7790/7924; HTTP requests 44221; received 43.3 MiB
    Groups 204/223; images 7794/7924; HTTP requests 44391; received 44.9 MiB
    Groups 205/223; images 7810/7924; HTTP requests 44420; received 45.2 MiB
    Groups 206/223; images 7816/7924; HTTP requests 44811; received 46.2 MiB
    Groups 207/223; images 7826/7924; HTTP requests 45096; received 48.6 MiB
    Groups 208/223; images 7840/7924; HTTP requests 45154; received 49.2 MiB
    Groups 209/223; images 7846/7924; HTTP requests 45420; received 50.0 MiB
    Groups 210/223; images 7854/7924; HTTP requests 45550; received 51.6 MiB
    Groups 211/223; images 7864/7924; HTTP requests 45634; received 52.3 MiB
    Groups 212/223; images 7870/7924; HTTP requests 45750; received 53.1 MiB
    Groups 213/223; images 7874/7924; HTTP requests 46295; received 53.9 MiB
    Groups 214/223; images 7882/7924; HTTP requests 46507; received 55.2 MiB
    Groups 215/223; images 7888/7924; HTTP requests 47059; received 56.1 MiB
    Groups 216/223; images 7892/7924; HTTP requests 47177; received 56.6 MiB
    Groups 217/223; images 7900/7924; HTTP requests 47544; received 57.3 MiB
    Groups 218/223; images 7906/7924; HTTP requests 47855; received 57.8 MiB
    Groups 219/223; images 7914/7924; HTTP requests 48212; received 58.7 MiB
    Groups 220/223; images 7920/7924; HTTP requests 48314; received 59.2 MiB
    Groups 221/223; images 7922/7924; HTTP requests 48459; received 59.4 MiB
    Groups 221/223; images 7922/7924; HTTP requests 48612; received 59.5 MiB
    Groups 221/223; images 7922/7924; HTTP requests 48740; received 59.6 MiB
    Groups 222/223; images 7924/7924; HTTP requests 48810; received 59.7 MiB
    Groups 223/223; images 7924/7924; HTTP requests 48846; received 59.7 MiB
    Selected image bytes: 0.819 GiB
    Report: /home/linfu/src/Test/ObjectConceptLearning/data/imagenet_index/last_run.json
    Complete: 7924 images downloaded or verified.
    ✓ • 9m 41s

## Assistant

官方备份与本地 `from_web.tgz` 大小一致，没有发现更新的数据包。我会再检查原站迁移后的图片地址和公开历史存档，并生成只包含测试所需图片及标注的传输清单，方便你上传到空间有限的服务器。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import importlib.util
        for name in ['pypdf','PyPDF2','fitz','pdfminer','torch','transformers']:
         print(name,importlib.util.find_spec(name) is not None)
        PY
    pypdf False
    PyPDF2 False
    fitz False
    pdfminer False
    torch True
    transformers True
    ✓ • 54ms

## Activity

    $ python -B - <<'PY'
        import importlib.util
        for name in ['pypdf','PyPDF2','fitz','pdfminer']:
         print(name,importlib.util.find_spec(name) is not None)
        PY
    pypdf False
    PyPDF2 False
    fitz False
    pdfminer False
    ✓ • 19ms

## Activity

    $ curl -L --fail --max-time 30 --silent --show-error 'https://ar5iv.labs.arxiv.org/html/2212.02710' -o /tmp/ocl-paper.html
    ✓ • 887ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import pickle, json
        from pathlib import Path
        from collections import Counter
        from PIL import Image
        selected=set(json.loads(Path('transfer_lists/selection.json').read_text())['selected_categories'])
        maxima=[];dims=Counter();out=[]
        for sp in ['train','val','test']:
         for row in pickle.load((Path('resources')/f'OCL_annot_{sp}.pkl').open('rb')):
          if row['name'].startswith('ImageNet/'):
           for obj in row['objects']:
            if obj['obj'] in selected and 'box' in obj:
             maxima.append(max(obj['box']))
             if max(obj['box'])>270:out.append((row['name'],obj['box']))
        print('selected_imagenet_boxes',len(maxima),'max',max(maxima),'over270',len(out));print('examples',out[:15])
        PY
    selected_imagenet_boxes 14855 max 261 over270 0
    examples []
    ✓ • 2.18s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B recover_web_images.py
    Recovery 10/216; recovered 1
    Recovery 20/216; recovered 3
    Recovery 30/216; recovered 4
    Recovery 40/216; recovered 4
    Recovery 50/216; recovered 6
    Recovery 60/216; recovered 7
    Recovery 70/216; recovered 8
    Recovery 80/216; recovered 8
    Recovery 90/216; recovered 8
    Recovery 100/216; recovered 9
    Recovery 110/216; recovered 12
    Recovery 120/216; recovered 13
    Recovery 130/216; recovered 13
    Recovery 140/216; recovered 14
    Recovery 150/216; recovered 14
    Recovery 160/216; recovered 14
    Recovery 170/216; recovered 14
    Recovery 180/216; recovered 14
    Recovery 190/216; recovered 15
    Recovery 200/216; recovered 16
    Recovery 210/216; recovered 16
    Recovery 216/216; recovered 16
    ✗ (1) • 1m 32s

## Assistant

ImageNet 所需的 7,924 张图片已全部下载并通过解码校验，共约 0.82 GiB，完整压缩包没有落盘。历史存档和原站 CDN 又恢复了 8 张网页图片；剩余工作是完成网页恢复、核实坐标差异，并输出最终校验报告。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from html.parser import HTMLParser
        import re
        class Parser(HTMLParser):
         def __init__(self):super().__init__();self.parts=[]
         def handle_data(self,s):self.parts.append(s)
        p=Parser();p.feed(Path('/tmp/ocl-paper.html').read_text());s=' '.join(p.parts);Path('/tmp/ocl-paper.txt').write_text(s)
        for term in ['256','resize','resolution','150K','ImageNet']:
         matches=list(re.finditer(re.escape(term),s,re.I));print('term',term,'count',len(matches))
         for m in matches[:12]:print(s[max(0,m.start()-200):m.end()+300])
        PY
    term 256 count 0
    term resize count 0
    term resolution count 1
    Edward E
    Smith.
    
    
     Default probability.
    
    
     Cognitive Science , 15(2):251–269, 1991.
    
    
    
     [59]
    
    Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bjorn
    Ommer.
    
    
     High-resolution image synthesis with latent diffusion models.
    
    
     In  CVPR , 2022.
    
    
    
     [60]
    
    Donald B Rubin.
    
    
     Causal inference using potential outcomes: Design, modeling,
    decisions.
    
    
     Journal of the American Statistical Association ,
    100(469):322–331, 2005.
    
    
    
     [61]
    
    Agrim Gupta, Piotr
    term 150K count 1
     Object
     # Attribute
     # Affordance
    
     APY  [ 12 ]
     15,339
     15,339
     32
     64
     /
    
     SUN  [ 11 ]
     14,340
     14,340
     717
     102
     /
    
     COCO-a  [ 23 ]
     84,044
     188,426
     29
     196
     /
    
     ImageNet150k  [ 22 ]
     150,000
     150,000
     1,000
     25
     /
    
     Chao  et al .  [ 19 ]
     /
     /
     91
     /
     957 ( B B )
    
     Hermans et.al.  [ 14 ]
     375
     -
     6
     21
     7
    
     Zhu  et al .  [ 16 ]
     4,000
     4,000
     40
     57
     14
    
     OCL
     80,463
     185,941
     381
     114
     170
    
    
    
     Table 1 :  Dense annotated  datasets.
    term ImageNet count 4
    ance
     # Object
     # Attribute
     # Affordance
    
     APY  [ 12 ]
     15,339
     15,339
     32
     64
     /
    
     SUN  [ 11 ]
     14,340
     14,340
     717
     102
     /
    
     COCO-a  [ 23 ]
     84,044
     188,426
     29
     196
     /
    
     ImageNet150k  [ 22 ]
     150,000
     150,000
     1,000
     25
     /
    
     Chao  et al .  [ 19 ]
     /
     /
     91
     /
     957 ( B B )
    
     Hermans et.al.  [ 14 ]
     375
     -
     6
     21
     7
    
     Zhu  et al .  [ 16 ]
     4,000
     4,000
     40
     57
     14
    
     OCL
     80,463
     185,941
     381
     114
     170
    
    
    
     Table 1 :  Dense annotated  datase
     Shanghai Qi Zhi Institute, Shanghai Science and Technology Commission (21511101200).
    
    
    
     References
    
    
    
     [1]
    
    Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei.
    
    
     Imagenet: A large-scale hierarchical image database.
    
    
     In  CVPR , 2009.
    
    
    
     [2]
    
    Tsung Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva
    Ramanan, Piotr Dollár, and C. Lawrence Zitnick.
    
    
     Microsoft coco: Common objects in context.
    
    
     In  ECCV , 2014.
    
    
    
     [3]
    
    
    a
    Ramanan, Piotr Dollár, and C. Lawrence Zitnick.
    
    
     Microsoft coco: Common objects in context.
    
    
     In  ECCV , 2014.
    
    
    
     [3]
    
    Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.
    
    
     Imagenet classification with deep convolutional neural networks.
    
    
     In  NIPS , 2012.
    
    
    
     [4]
    
    Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
    
    
     Faster r-cnn: Towards real-time object detection with region proposal
    networks.
    
    
     In  NIPS , 2015.
    
    
    
     [5]
    
    Phillip Isola, Joseph
     a low confusion ratio and multiple refining stages.
    
    
    
     D.12  Potential Bias
    
    
     We have considered the bias issue in the construction of our dataset.
    (1) In our dataset, the existing datasets (ImageNet  [ 1 ] , COCO  [ 2 ] , aPY  [ 12 ] , SUN  [ 11 ] ) are open-sourced datasets and the images collected from the Internet are publicly accessible too. The dataset is constructed for only non-commercial purposes. We will only provide the URLs of these images to avoid copyright infringement.
    (2) During
    ✓ • 43ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from PIL import Image, ImageDraw
        import json
        from pathlib import Path
        rows=[r for r in json.loads(Path('transfer_lists/web_recovery_report.json').read_text())['results'] if r['status']=='recovered']
        print('recovered',[(r['name'],r['recovered_from']) for r in rows])
        canvas=Image.new('RGB',(6*180,((len(rows)+5)//6)*170),'white');draw=ImageDraw.Draw(canvas)
        for i,r in enumerate(rows):
         with Image.open(r['name']) as im:
          thumb=im.convert('RGB');thumb.thumbnail((170,140));x=(i%6)*180;y=(i//6)*170;canvas.paste(thumb,(x,y));draw.text((x,y+142),Path(r['name']).name,fill='black')
        canvas.save('/tmp/ocl-recovered-preview.jpg')
        PY
    recovered [('from_web/test_0043.jpg', 'https://web.archive.org/web/20240520025020id_/http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201501/06/132053shdlga00hgd5zzhg.jpg'), ('from_web/test_0051.jpg', 'https://web.archive.org/web/20160402030401id_/http://sm.fjsen.com/images/attachement/jpg/site2/20160201/1c6f65ee7f521819606d0a.JPG'), ('from_web/test_0236.jpg', 'https://web.archive.org/web/20211120210345id_/http://www.chinadaily.com.cn/china/images/attachement/jpg/site1/20101214/002170196e1c0e7176dc1d.jpg'), ('from_web/test_0298.jpg', 'https://web.archive.org/web/20160518033546id_/http://localsguidesa.com/wp-content/uploads/2013/07/IMG_20130608_183803_467.jpg'), ('from_web/test_0569.jpg', 'https://web.archive.org/web/20180121002556id_/http://www.laosmotorbiketours.com/wp-content/uploads/2013/09/199-vietnam-dirt-bike-11.jpg'), ('from_web/test_0887.jpg', 'https://web.archive.org/web/20200215140728id_/http://laostravelpackagetours.com/wp-content/uploads/2015/03/Elephant-Village-in-Luang-Prabang.jpg'), ('from_web/test_1053.jpg', 'https://web.archive.org/web/20200503004515id_/http://www.chinadaily.com.cn/m/guizhou/images/attachement/jpg/site1/20151029/0023ae9888c1179bba6f03.jpg'), ('from_web/test_1092.jpg', 'https://web.archive.org/web/20210304052952id_/http://elders.com.au/wp-content/uploads/2016/08/rural-services-livestock-dairy-cattle-2-edit.jpg'), ('from_web/val_0338.jpg', 'https://web.archive.org/web/20190703040012id_/http://up.36992.com/pic_360/71/7f/0b/717f0bb79d4d98dc59a2929232074f85.jpg'), ('from_web/val_0578.jpg', 'https://web.archive.org/web/20191217062545id_/http://www.ctvnews.ca/polopoly_fs/1.4732484.1576532006%21/httpImage/image.jpg_gen/derivatives/landscape_800/image.jpg'), ('from_web/val_0596.jpg', 'https://web.archive.org/web/20220328144432id_/http://koreancarpart.com/store/assests/images/stock/17138278615a8d12ee83018.jpg'), ('from_web/val_0714.jpg', 'https://web.archive.org/web/20181222140650id_/http://dogsmonthly.co.uk/wp-content/uploads/2018/12/Tasha-is-back-enjoying-her-walks-now-thanks-to-vet-Eandil-Maddock-of-Oakwood-Vet-Referrals-part-of-Willows-Veterinary-Group30-1024x673.jpg'), ('from_web/val_0747.jpg', 'https://web.archive.org/web/20241121044955id_/http://images.freeimages.com/images/premium/previews/1798/17988284-wild-dog-lying-in-the-on-grass.jpg'), ('from_web/val_0750.jpg', 'https://m.media-amazon.com/images/I/619cXR-XnyL._SL1004_.jpg'), ('from_web/val_2420.jpg', 'https://m.media-amazon.com/images/I/51Fk0l0bc5L.jpg'), ('from_web/val_2434.jpg', 'https://m.media-amazon.com/images/I/51Ea6sAd1dL.jpg')]
    ✓ • 271ms

## Activity

    Viewed image /tmp/ocl-recovered-preview.jpg

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        print('recovery_counts',Counter(x['status'] for x in r['results']))
        print('failure_summary',Counter(a.get('error','').split(':')[0][:80] for x in r['results'] if x['status']=='unavailable' for a in x['attempts']).most_common(10))
        print('imagenet_report',json.loads(Path('imagenet_index/last_run.json').read_text()))
        PY
    recovery_counts Counter({'unavailable': 200, 'recovered': 16})
    failure_summary [('429 Client Error', 106), ('No snapshot available', 91), ('cannot identify image file <_io.BytesIO object at 0x70d3317994e0>', 1), ('404 Client Error', 1), ("HTTPSConnectionPool(host='web.archive.org', port=443)", 1)]
    imagenet_report {'mode': 'download', 'requested_images': 7924, 'completed_images': 7924, 'downloaded_images': 222, 'existing_images': 7702, 'selected_image_bytes': 879082015, 'http_requests': 48846, 'received_bytes': 62650487, 'missing_images': [], 'errors': []}
    ✓ • 19ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B audit_test_data.py --workers 12
    Validated 5000/35633 images
    Validated 10000/35633 images
    Validated 15000/35633 images
    Validated 20000/35633 images
    Validated 25000/35633 images
    Validated 30000/35633 images
    Validated 35000/35633 images
    {
      "generated_at": "2026-10-22T18:39:13.212874+00:00",
      "ready_for_full_evaluation": false,
      "selection_splits": [
        "train",
        "val",
        "test"
      ],
      "count_unit": "object_instance",
      "selected_categories": {
        "dog": 16171,
        "bird": 13961,
        "sheep": 13821,
        "car": 11511,
        "motorcycle": 8519,
        "apple": 8382,
        "cattle": 8379,
        "broccoli": 8333,
        "truck": 7769,
        "elephant": 7032
      },
      "selected_objects": 103878,
      "expected_evaluation_objects": 103877,
      "objects_blocked_by_missing_or_corrupt_images": 295,
      "required_images": 35633,
      "sources": {
        "COCO": {
          "valid": 25067,
          "required": 25067
        },
        "ImageNet": {
          "valid": 7924,
          "required": 7924
        },
        "aPY": {
          "valid": 1168,
          "required": 1168
        },
        "from_web": {
          "valid": 1275,
          "missing": 199,
          "required": 1474
        }
      },
      "valid_image_bytes": 5769923281,
      "vocabulary_sizes": {
        "object": 381,
        "attribute": 114,
        "affordance": 170
      },
      "excluded_invalid_boxes": [
        {
          "image_name": "COCO/val2014/COCO_val2014_000000315601.jpg",
          "object_index": 12,
          "category": "car",
          "box": [
            0,
            266,
            4,
            266
          ]
        }
      ],
      "crop_errors": [
        {
          "image_name": "ImageNet/train/n02089078/n02089078_178.JPEG",
          "object_index": 0,
          "box": [
            0.0,
            194.51502990722656,
            64.61176300048828,
            255.5253448486328
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02095314/n02095314_6284.JPEG",
          "object_index": 2,
          "box": [
            149,
            93,
            235,
            202
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02100735/n02100735_1090.JPEG",
          "object_index": 0,
          "box": [
            99,
            160,
            170,
            255
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02108000/n02108000_3426.JPEG",
          "object_index": 1,
          "box": [
            123.6557388305664,
            84.18275451660156,
            225.13156127929688,
            205.0046844482422
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n03796401/n03796401_5457.JPEG",
          "object_index": 1,
          "box": [
            90.1938247680664,
            167.32815551757812,
            199.00621032714844,
            251.77113342285156
          ],
          "category": "truck"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 2,
          "box": [
            183.3660888671875,
            214.6282196044922,
            246.3701171875,
            254.4662322998047
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 7,
          "box": [
            162.5959014892578,
            51.40813446044922,
            244.72694396972656,
            104.85037231445312
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 13,
          "box": [
            215.67884826660156,
            63.491458892822266,
            256.0,
            123.73628997802734
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "object_index": 16,
          "box": [
            207.257080078125,
            173.25148010253906,
            256.0,
            254.88124084472656
          ],
          "category": "broccoli"
        },
        {
          "image_name": "from_web/val_2026.jpg",
          "object_index": 0,
          "box": [
            297,
            44,
            528,
            346
          ],
          "category": "elephant"
        }
      ],
      "label_errors": [],
      "transfer_manifest_keeps_missing_paths": true
    }
    Report: /home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/data_audit.json
    ✗ (1) • 55.12s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        i=0
        for x in r['results']:
         if any('429' in a.get('error','') for a in x['attempts']):
          print(x);i+=1
          if i==3:break
        PY
    {'name': 'from_web/val_0749.png', 'original_url': 'http://hbimg.b0.upaiyun.com/1bcf7368f93c8fa6f3db9096baa9ca1f3d15359122b7e-4Ysxdo_fw658', 'attempts': [{'source': 'Internet Archive', 'error': '429 Client Error: Too Many Requests for url: https://archive.org/wayback/available?url=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F1bcf7368f93c8fa6f3db9096baa9ca1f3d15359122b7e-4Ysxdo_fw658&timestamp=20220101'}], 'status': 'unavailable'}
    {'name': 'from_web/val_0760.jpg', 'original_url': 'http://d1yn1kh78jj1rr.cloudfront.net/image/preview/rDtN98Qoishumwih/graphicstock-happy-dog-lying-on-his-back-in-grass-with-extending-paw-sunny-nature_HubChRXSM-_SB_PM.jpg', 'attempts': [{'source': 'Internet Archive', 'error': '429 Client Error: Too Many Requests for url: https://archive.org/wayback/available?url=http%3A%2F%2Fd1yn1kh78jj1rr.cloudfront.net%2Fimage%2Fpreview%2FrDtN98Qoishumwih%2Fgraphicstock-happy-dog-lying-on-his-back-in-grass-with-extending-paw-sunny-nature_HubChRXSM-_SB_PM.jpg&timestamp=20220101'}], 'status': 'unavailable'}
    {'name': 'from_web/val_0761.jpg', 'original_url': 'http://images.freeimages.com/images/premium/previews/1193/11937618-dog-in-the-cage-looking-away.jpg', 'attempts': [{'source': 'Internet Archive', 'error': '429 Client Error: Too Many Requests for url: https://archive.org/wayback/available?url=http%3A%2F%2Fimages.freeimages.com%2Fimages%2Fpremium%2Fpreviews%2F1193%2F11937618-dog-in-the-cage-looking-away.jpg&timestamp=20220101'}], 'status': 'unavailable'}
    ✓ • 64ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/recover_web_images.py
    @@ -2,2 +2,3 @@
     
    +import argparse
     from concurrent.futures import ThreadPoolExecutor, as_completed
    @@ -9,2 +10,3 @@
     import threading
    +import time
     from urllib.parse import urlsplit, urlunsplit
    @@ -18,4 +20,13 @@
     def main():
    +    parser = argparse.ArgumentParser(description=__doc__)
    +    parser.add_argument("--retry-transient", action="store_true")
    +    parser.add_argument("--request-delay", type=float, default=2.0)
    +    args = parser.parse_args()
    +    if args.request_delay < 1:
    +        parser.error("Use a request delay of at least one second")
         root = Path(__file__).resolve().parent
         reports = root / "transfer_lists"
    +    report_path = reports / "web_recovery_report.json"
    +    previous = json.loads(report_path.read_text()) if report_path.is_file() else {}
    +    saved_results = {r["name"]: r for r in previous.get("results", [])}
         wanted = {n for n in (reports / "ocl_non_imagenet.txt").read_text().splitlines()
    @@ -51,3 +62,19 @@
                 pending.append(name)
    +    if args.retry_transient:
    +        pending = [name for name in pending if name not in saved_results or any(
    +            token in attempt.get("error", "")
    +            for attempt in saved_results[name].get("attempts", [])
    +            for token in ("429", "500", "502", "503", "504", "timed out", "Connection", "SSL")
    +        )]
         local = threading.local()
    +    schedule_lock = threading.Lock()
    +    next_request = 0.0
    +
    +    def get(session, url, **kwargs):
    +        nonlocal next_request
    +        with schedule_lock:
    +            when = max(time.monotonic(), next_request)
    +            next_request = when + args.request_delay
    +        time.sleep(max(0, when - time.monotonic()))
    +        return session.get(url, **kwargs)
     
    @@ -64,3 +91,3 @@
                 try:
    -                with session.get(url, stream=True, timeout=(8, 15)) as response:
    +                with get(session, url, stream=True, timeout=(8, 15)) as response:
                         response.raise_for_status()
    @@ -88,3 +115,3 @@
             try:
    -            response = session.get("https://archive.org/wayback/available",
    +            response = get(session, "https://archive.org/wayback/available",
                                        params={"url": urls[name], "timestamp": "20220101"},
    @@ -112,16 +139,19 @@
                 raise SystemExit("Another selected-web download is running")
    -        results = []
    -        with ThreadPoolExecutor(max_workers=6) as pool:
    +        results = dict(saved_results)
    +        completed = 0
    +        with ThreadPoolExecutor(max_workers=3) as pool:
                 futures = [pool.submit(recover, name) for name in pending]
                 for future in as_completed(futures):
    -                results.append(future.result())
    -                report = {"requested": len(pending),
    -                          "recovered": sum(r["status"] == "recovered" for r in results),
    -                          "pending": len(pending) - len(results),
    -                          "results": sorted(results, key=lambda r: r["name"])}
    -                atomic_write(reports / "web_recovery_report.json",
    +                result = future.result()
    +                results[result["name"]] = result
    +                completed += 1
    +                report = {"requested": len(set(saved_results) | set(pending)),
    +                          "recovered": sum(r["status"] == "recovered" for r in results.values()),
    +                          "pending": len(pending) - completed,
    +                          "results": sorted(results.values(), key=lambda r: r["name"])}
    +                atomic_write(report_path,
                                  (json.dumps(report, indent=2) + "\n").encode())
    -                if len(results) % 10 == 0 or len(results) == len(pending):
    -                    print(f"Recovery {len(results)}/{len(pending)}; recovered {report['recovered']}", flush=True)
    -        return 1 if any(r["status"] == "unavailable" for r in results) else 0
    +                if completed % 10 == 0 or completed == len(pending):
    +                    print(f"Recovery {completed}/{len(pending)}; recovered {report['recovered']}", flush=True)
    +        return 1 if any(r["status"] == "unavailable" for r in results.values()) else 0
     

## Assistant

网页存档已额外恢复 16 张图片；部分查询触发了服务端限流，我已降低频率，只重试暂时失败的请求。上传目录会通过硬链接引用现有图片，避免在本地再复制一份大数据；缺失文件和裁剪问题会随目录一起保留为报告。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        s=Path('/tmp/ocl-paper.txt').read_text()
        for phrase in ['[22]', 'annotation process', 'Data Collection', 'Image Collection']:
         start=0
         for _ in range(6):
          i=s.lower().find(phrase.lower(),start)
          if i<0:break
          print(phrase,s[max(0,i-50):i+800]);start=i+len(phrase)
        PY
    [22] ense knowledge.
    
    
     In  ECCV , 2018.
    
    
    
     [22]
    
    H. Liu, R. Wang, S. Shan, and X. Chen.
    
    
     Learning multifunctional binary codes for both category and attribute
    oriented retrieval tasks.
    
    
     In  CVPR , 2017.
    
    
    
     [23]
    
    Genevieve Patterson and James Hays.
    
    
     Coco attributes: Attributes for people, animals, and objects.
    
    
     In  ECCV , 2016.
    
    
    
     [24]
    
    Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua
    Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma,
    Michael Bernstein, and Li Fei-Fei.
    
    
     Visual genome: Connecting language and vision using crowdsourced
    dense image annotations.
    
    
     IJCV , 2016.
    
    
    
     [25]
    
    Drew A Hudson and Christopher D Manning.
    
    
     Gqa: A new dataset for real-world visual reasoning and compositional
    question answering.
    
    
     In  CVPR ,
    Data Collection ting bias.
    
    
     Figure 2 :  OCL construction. a) Data collection. b) Annotating category-level attributes and affordances. c) Annotating instance-level attributes and affordances. d) Finding direct and clear instance-level causal relations.
    
    
    
     3  Constructing OCL Benchmark
    
    
     We construct a benchmark to characterize abundant object knowledge following Fig.  2 .
    
    
     3.1  Fine-Grained Object Knowledge Base
    
    
     Data Collection.
    We briefly introduce the collection of affordances, categories, attribute classes, and image sources here.
    
     (1)
    
     Affordance :
    We collect 170 affordances out of 1,006 candidates from widely-used action/affordance datasets  [ 19 ,  55 ,  44 ,  56 ,  16 ,  17 ]  given generality and commonness.
    
     (2)
    
     Category :
    Considering the taxonomy (WordNet  [ 57 ] ) and diversity, we collect 381 objects out
    Data Collection
    
     3.1  Fine-Grained Object Knowledge Base
    
    
     Data Collection.
    We briefly introduce the collection of affordances, categories, attribute classes, and image sources here.
    
     (1)
    
     Affordance :
    We collect 170 affordances out of 1,006 candidates from widely-used action/affordance datasets  [ 19 ,  55 ,  44 ,  56 ,  16 ,  17 ]  given generality and commonness.
    
     (2)
    
     Category :
    Considering the taxonomy (WordNet  [ 57 ] ) and diversity, we collect 381 objects out of 1,742 candidates from object datasets  [ 12 ,  11 ,  2 ,  23 ,  1 ,  22 ] .
    
     (3)
    
     Attribute :
    We manually filter the 500 most frequent attributes from attribute datasets  [ 12 ,  11 ,  2 ,  23 ,  1 ,  22 ,  24 ]  and choose 114 attributes, covering colors, deformations, supercategories, surface, geometrical and physical properties.
    
     (4)
    
     Image :
    We extr
    Image Collection n.
    
    
     Discovering states and transformations in image collections.
    
    
     In  CVPR , 2015.
    
    
    
     [6]
    
    James J Gibson.
    
    
     The ecological approach to the visual perception of pictures.
    
    
     Leonardo , 11(3):227–235, 1978.
    
    
    
     [7]
    
    Alex Martin.
    
    
     The representation of object concepts in the brain.
    
    
     Annu. Rev. Psychol. , 58:25–45, 2007.
    
    
    
     [8]
    
    Stevan Harnad.
    
    
     The symbol grounding problem.
    
    
     Physica D: Nonlinear Phenomena , 42(1-3):335–346, 1990.
    
    
    
     [9]
    
    B Ross.
    
    
     Category learning: Learning to access and use relevant knowledge.
    
    
     Memory and mind: A Festschrift for Gordon H. Bower , pages
    229–246, 2008.
    
    
    
     [10]
    
    Christoph H Lampert, Hannes Nickisch, and Stefan Harmeling.
    
    
     Learning to detect unseen object classes by between-class attribute
    transfer.
    
    
     In  CVPR , 20
    Image Collection mages to avoid copyright infringement.
    (2) During image collection, we choose images with general objects and are particularly careful with the image selection to avoid unsuitable content, private images, or implicit biases.
    (3) During annotation, the annotators cover different genders, ages, and fields of expertise to avoid potential annotation biases. And they are all informed on how we will use the annotations in our research.
    
    
    
    
     Appendix E  ITE Metric Details
    
    
     ITE ( Individual Treatment Effect (ITE)   [ 60 ] ) is to measure whether a model infers affordance with proper attention to the causality-related attribute. That said, when removing the attribute, the model is expected to have  large prediction difference further away from the ground truth .
    
    
     We detail some settings in our ITE metric. For the ITE score:
    
    
    
    
    
    ✓ • 0ms

## Activity

    $ curl -L --fail --max-time 20 --silent --show-error 'https://vipl.ict.ac.cn/en/resources/databases/201803/t20180316_34793.html' -o /tmp/ocl-imagenet150k-source.html
    ✓ • 473ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from html.parser import HTMLParser
        import re
        class P(HTMLParser):
         def __init__(self):super().__init__();self.text=[];self.links=[]
         def handle_data(self,s):self.text.append(s)
         def handle_starttag(self,t,a):
          if t=='a':self.links.extend(v for k,v in a if k=='href')
        p=P();p.feed(Path('/tmp/ocl-imagenet150k-source.html').read_text());s=' '.join(p.text)
        print(s[:9000]);print('LINKS',p.links[-25:])
        PY
    
    
    
    
    
    
    
    
    
    
    
    
         ImageNet-150K Dataset----Visual Information Processing and Learning (VIPL)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                   中国科学院  丨
                   所主站 丨
                   中文
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                   Home
    
    
                         Research
    
    
    
                               Affective Computing
    
    
    
                               Audio-Visual Speech Understanding Group
    
    
    
                               Face Recognition
    
    
    
                               Media Learning and Knowledge Reasoning
    
    
    
                               Multimedia Computing and Multimodal Intelligent
    
    
    
                               Medical Visual Intelligence Group
    
    
    
                               Sign Language Recognition
    
    
    
                               Visual Modeling
    
    
    
                               Visual Scene Understanding
    
    
    
                               AI Safety and Trustworthiness Group
    
    
    
    
    
    
    
                         People
    
    
    
    
                                Professor
    
    
    
    
    
    
    
    
                                Associate Professor
    
    
    
    
    
    
    
    
                                Assistant Research Fellow
    
    
    
    
    
    
    
    
                                Postdoctoral Fellow
    
    
    
    
    
    
    
    
                                Engineer
    
    
    
    
    
    
    
    
    
    
                         Publications
    
    
    
    
                                Accepted
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2025
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2024
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2023
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2022
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2021
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2020
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    
                                2019
    
    
    
    
    
                                      Journal Paper
    
    
    
    
    
                                      Conference Paper
    
    
    
    
    
    
    
    LINKS ['https://vipl.ict.ac.cn/en/resources/databases/', 'https://vipl.ict.ac.cn/en/resources/codes/', 'https://vipl.ict.ac.cn/en/resources/challen/', 'https://vipl.ict.ac.cn/en/news/', 'https://vipl.ict.ac.cn/en/news/defense/', 'https://vipl.ict.ac.cn/en/news/researchevents/', 'https://vipl.ict.ac.cn/en/news/academicevents/', 'https://vipl.ict.ac.cn/en/news/', 'https://vipl.ict.ac.cn/en/news/defense/', 'https://vipl.ict.ac.cn/en/news/defense/doctoral/', 'https://vipl.ict.ac.cn/en/news/defense/master/', 'https://vipl.ict.ac.cn/en/news/researchevents/', 'https://vipl.ict.ac.cn/en/news/academicevents/', '//vipl.ict.ac.cn/en/', '../../', '../', '../', '../../codes/', 'javascript:doZoom(22)', 'javascript:doZoom(19)', 'javascript:doZoom(14)', '../201801/t20180126_34795.html', '../202007/t20200730_34803.html', 'https://www.cas.cn/', 'http://beian.miit.gov.cn/']
    ✓ • 0ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from html.parser import HTMLParser
        import re
        class P(HTMLParser):
         def __init__(self):super().__init__();self.parts=[]
         def handle_data(self,s):self.parts.append(s)
        p=P();p.feed(Path('/tmp/ocl-imagenet150k-source.html').read_text());s=' '.join(' '.join(p.parts).split())
        for word in ['150K','resiz','256','download','provide']:
         for m in list(re.finditer(word,s,re.I))[:8]:print(s[max(0,m.start()-100):m.start()+900])
        PY
    ImageNet-150K Dataset----Visual Information Processing and Learning (VIPL) 中国科学院 丨 所主站 丨 中文 Home Research Affective Computing Audio-Visual Speech Understanding Group Face Recognition Media Learning and Knowledge Reasoning Multimedia Computing and Multimodal Intelligent Medical Visual Intelligence Group Sign Language Recognition Visual Modeling Visual Scene Understanding AI Safety and Trustworthiness Group People Professor Associate Professor Assistant Research Fellow Postdoctoral Fellow Engineer Publications Accepted Journal Paper Conference Paper 2025 Journal Paper Conference Paper 2024 Journal Paper Conference Paper 2023 Journal Paper Conference Paper 2022 Journal Paper Conference Paper 2021 Journal Paper Conference Paper 2020 Journal Paper Conference Paper 2019 Journal Paper Conference Paper 2018 Journal Paper Conference Paper 2017 Journal Paper Conference Paper 2016 Journal Paper Conference P
    ; if(currentChannel == curtxt){ $(this).children('.a-title').addClass("active"); } }); }); ImageNet-150K Dataset Time: Mar 16, 2018 【 L M S 】 Share: 1. Overview ImageNet-150K dataset is a subset of ImageNet with additional visual attribute annotations. The images are associated with category and visual attribute labels, and thus can be used for many different tasks, e.g. hash learning, attribute learning, and so on. Specifically, the dataset contains 1,000 categories with 150 images per category, resulting in 150,000 images in total. Moreover, we further select 50,000 out of 150,000 images (50 images per category) to annotate 25 visual attributes including color, texture, shape, material, and structure. The final attributes annotations are presented with three values, i.e. +1, −1, and 0, for indicating the presence, absence, and uncertainty of a specific attribute respectively. 2. Data annotation Based on the ImageNet dataset, 1000 categories with 150 images (148 images from the traini
    "active"); } }); }); ImageNet-150K Dataset Time: Mar 16, 2018 【 L M S 】 Share: 1. Overview ImageNet-150K dataset is a subset of ImageNet with additional visual attribute annotations. The images are associated with category and visual attribute labels, and thus can be used for many different tasks, e.g. hash learning, attribute learning, and so on. Specifically, the dataset contains 1,000 categories with 150 images per category, resulting in 150,000 images in total. Moreover, we further select 50,000 out of 150,000 images (50 images per category) to annotate 25 visual attributes including color, texture, shape, material, and structure. The final attributes annotations are presented with three values, i.e. +1, −1, and 0, for indicating the presence, absence, and uncertainty of a specific attribute respectively. 2. Data annotation Based on the ImageNet dataset, 1000 categories with 150 images (148 images from the training set and 2 images from the validation set) per category are randomly
    g set and 2 images from the validation set) per category are randomly selected to form the ImageNet-150K dataset. Moreover, we further select 50 out of 150 images per category (48 images from the training set and 2 images from the validation set) to annotate 25 visual attributes including color, texture, shape, material, and structure. The final attributes annotations are presented with three values, i.e. +1, −1, and 0, for indicating the presence, absence, and uncertainty of a certain attribute respectively. Specifically, for each attribute of each image, three individual annotators are required to choose from positive, negative, or uncertain to indicate the presence of that attribute in the image. Images with at least two annotations of positive/negative are labeled as +1/-1 respectively (i.e. positive/negative sample of the specific attribute), and the other images are labeled as 0 (uncertain). The annotated attributes on this dataset in order are: (1) black, (2) blue, (3) brown, (4
    ict.ac.cn), Institute of Computing Technology, Chinese Academy of Sciences 5. Download The ImageNet-150K dataset is released to universities and research institutes for research purpose only. To request a copy of the ImageNet-150K dataset, please do as follows: • Send an email to Dr. Wang (wangruiping@ict.ac.cn). When we receive your email, we would provide the download link to you. • By using the ImageNet-150K dataset, you are recommended to refer to the following paper: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen. Learning Multifunctional Binary Codes for Both Category and Attribute Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel = $(".bread-item").fi
    o universities and research institutes for research purpose only. To request a copy of the ImageNet-150K dataset, please do as follows: • Send an email to Dr. Wang (wangruiping@ict.ac.cn). When we receive your email, we would provide the download link to you. • By using the ImageNet-150K dataset, you are recommended to refer to the following paper: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen. Learning Multifunctional Binary Codes for Both Category and Attribute Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel = $(".bread-item").find("a:eq(1)").text(); $(".dropdown").each(function(){ len = $(this).children(".dropdown-menu").children("li").length; if(len<1
    cn). When we receive your email, we would provide the download link to you. • By using the ImageNet-150K dataset, you are recommended to refer to the following paper: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen. Learning Multifunctional Binary Codes for Both Category and Attribute Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel = $(".bread-item").find("a:eq(1)").text(); $(".dropdown").each(function(){ len = $(this).children(".dropdown-menu").children("li").length; if(len<1){ $(this).removeClass("dropdown"); $(this).children(".dropdown-menu").remove(); $(this).children("a").removeAttr("data-toggle").removeClass("dropdown-toggle"); $("a", this).off('click
    Liu (haomiao.liu@vipl.ict.ac.cn), Institute of Computing Technology, Chinese Academy of Sciences 5. Download The ImageNet-150K dataset is released to universities and research institutes for research purpose only. To request a copy of the ImageNet-150K dataset, please do as follows: • Send an email to Dr. Wang (wangruiping@ict.ac.cn). When we receive your email, we would provide the download link to you. • By using the ImageNet-150K dataset, you are recommended to refer to the following paper: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen. Learning Multifunctional Binary Codes for Both Category and Attribute Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel
    Send an email to Dr. Wang (wangruiping@ict.ac.cn). When we receive your email, we would provide the download link to you. • By using the ImageNet-150K dataset, you are recommended to refer to the following paper: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen. Learning Multifunctional Binary Codes for Both Category and Attribute Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel = $(".bread-item").find("a:eq(1)").text(); $(".dropdown").each(function(){ len = $(this).children(".dropdown-menu").children("li").length; if(len<1){ $(this).removeClass("dropdown"); $(this).children(".dropdown-menu").remove(); $(this).children("a").removeAttr("data-toggle").removeCla
    Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel = $(".bread-item").find("a:eq(1)").text(); $(".dropdown").each(function(){ len = $(this).children(".dropdown-menu").children("li").length; if(len<1){ $(this).removeClass("dropdown"); $(this).children(".dropdown-menu").remove(); $(this).children("a").removeAttr("data-toggle").removeClass("dropdown-toggle"); $("a", this).off('click'); $("a.dropdown-toggle", this).on('click', function (e) { }); } if($(this).children("a").text()==curChannel){ $(this).addClass("active"); } }); // 检索 function isValid(str) { if (str.indexOf('&') != -1 || str.indexOf('<') != -1 || str.indexOf('>') != -1 || str.indexOf('\'') != -1 || str.in
     follows: • Send an email to Dr. Wang (wangruiping@ict.ac.cn). When we receive your email, we would provide the download link to you. • By using the ImageNet-150K dataset, you are recommended to refer to the following paper: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen. Learning Multifunctional Binary Codes for Both Category and Attribute Oriented Retrieval Tasks. Computer Vision and Pattern Recognition (CVPR), pp: 6259-6268, July 2017. Download: Previous： DEVISIGN Database Next： Occluded-DukeMTMC-VideoReID Database 版权所有©中科院计算所视觉信息处理与学习组 京ICP备05002829号-1 京公网安签1101080060号 单位地址:北京海淀区中关村科学院南路6号 邮编:100190 联系电话:010-62600514 Email: chengyi@ict.ac.cn Valse 深度学习大讲堂 $(function () { // 导航选中 var len = ""; var curChannel = $(".bread-item").find("a:eq(1)").text(); $(".dropdown").each(function(){ len = $(this).children(".dropdown-menu").children("li").length; if(len<1){ $(this).removeClass("dropdown"); $(this).children(".dropdown-menu").remove(); $(this).children("a").removeAttr("data-toggle
    ✓ • 2ms

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/build_test_subset.py
    """Create a compact upload directory using hard links to audited OCL data."""
    
    import argparse
    import json
    import os
    from pathlib import Path
    import tempfile
    
    from audit_test_data import save
    
    
    def main():
        root = Path(__file__).resolve().parent
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--output", type=Path, default=root / "test_subset")
        args = parser.parse_args()
        output = args.output.expanduser().resolve()
        if output == root or root.is_relative_to(output):
            parser.error("The subset must be a separate directory")
        reports = root / "transfer_lists"
        audit = json.loads((reports / "data_audit.json").read_text())
        marker = output / ".ocl-subset.json"
        if output.exists() and not marker.is_file():
            raise ValueError(f"Refusing to alter an existing unmanaged directory: {output}")
        previous = json.loads(marker.read_text()) if marker.is_file() else {"linked_files": {}}
        output.mkdir(parents=True, exist_ok=True)
        if not marker.is_file():
            save(marker, json.dumps(previous) + "\n")
        names = (reports / "test_data.txt").read_text().splitlines()
        linked = dict(previous["linked_files"])
        missing = []
        for name in names:
            source = root / name
            if not source.is_file():
                missing.append(name)
                continue
            destination = output / name
            stat = source.stat()
            identity = [stat.st_dev, stat.st_ino]
            if destination.exists():
                old = destination.stat()
                if [old.st_dev, old.st_ino] == identity:
                    linked[name] = identity
                    continue
                if linked.get(name) != [old.st_dev, old.st_ino]:
                    raise ValueError(f"Unexpected file change in subset: {destination}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as handle:
                temporary = Path(handle.name)
            temporary.unlink()
            try:
                os.link(source, temporary)
                temporary.replace(destination)
            finally:
                temporary.unlink(missing_ok=True)
            linked[name] = identity
            if len(linked) % 1000 == 0:
                save(marker, json.dumps({"linked_files": linked}) + "\n")
        save(marker, json.dumps({"linked_files": linked}) + "\n")
        for source in reports.iterdir():
            if source.is_file() and source.suffix in (".json", ".jsonl", ".txt", ".sha256"):
                save(output / "transfer_lists" / source.name, source.read_text())
        scripts = ["audit_test_data.py", "download_imagenet_subset.py", "extract_imagenet_subset.py",
                   "download_selected_web.py", "download_web_images.py", "recover_web_images.py"]
        for name in scripts:
            save(output / name, (root / name).read_text())
        payload = sum((root / name).stat().st_size for name in names if (root / name).is_file())
        manifest = {
            "ready_for_full_evaluation": audit["ready_for_full_evaluation"],
            "required_files": len(names), "linked_files": len(names) - len(missing),
            "missing_files": missing, "payload_bytes": payload,
            "selection": "All objects from the top ten categories across train + val + test",
            "storage": "Hard links locally; ordinary files when transferred with rsync",
        }
        save(reports / "subset_manifest.json", json.dumps(manifest, indent=2) + "\n")
        save(output / "transfer_lists/subset_manifest.json", json.dumps(manifest, indent=2) + "\n")
        status = "READY" if audit["ready_for_full_evaluation"] else "INCOMPLETE - do not report full-test metrics yet"
        text = f"""# OCL top-ten evaluation data
    
    Status: {status}.
    
    Selection: train + val + test annotations are merged; categories are ranked by
    object-instance count. Every selected object belongs to the evaluation set.
    Required images: {audit['required_images']}. Missing files: {len(missing)}.
    Selected objects: {audit['selected_objects']}; the existing DataLoader excludes
    {len(audit['excluded_invalid_boxes'])} zero-area/invalid box before evaluation.
    Image and metadata payload currently present: {payload / 1024**3:.3f} GiB.
    
    See transfer_lists/data_audit.json for missing files, crop errors and label checks.
    transfer_lists/test_data.txt retains ALL required paths, including missing ones.
    The annotation files and raw image dimensions are preserved.
    
    ## Upload from the project root
    
    Replace USER, HOST and REMOTE_PROJECT with your SSH destination:
    
        rsync -av --partial --info=progress2 --exclude=.ocl-subset.json data/test_subset/ USER@HOST:REMOTE_PROJECT/data/
    
    The destination data directory contains COCO/, ImageNet/, aPY/, from_web/ and
    resources/, matching the relative paths in the annotations. Large source archives,
    unselected images, and local COCO symlinks are absent from this upload directory.
    The local files are hard-linked, so do not edit them in place: that also changes
    the source files. Uploading with rsync produces ordinary files on the server.
    
    ## Verify on the server
    
    From REMOTE_PROJECT/data with Pillow installed:
    
        sha256sum --quiet -c transfer_lists/available_files.sha256
        python audit_test_data.py
    
    Checksum success validates the transferred available files; the audit separately
    checks completeness and object crops, returning nonzero if anything is blocked.
    It needs no CLIP weights, torch or network access.
    
    ## Remaining issues
    
    Some original web URLs are no longer available. See web_download_report.json and
    web_recovery_report.json under transfer_lists/ for attempts and recovered sources.
    The OCL author previously supplied missing originals on request in issue 1:
    https://github.com/silicx/ObjectConceptLearning/issues/1#issuecomment-1875649083
    
    Some ImageNet boxes do not intersect the original-size images. The selected
    ImageNet coordinates are concentrated near a 256 x 256 frame, but the correct
    resize/crop convention has not been confirmed from the official code or paper.
    Confirm that convention before trusting image crops or evaluation metrics.
    The audit reports concrete failures; no speculative coordinate rewrite is applied.
    """
        save(output / "README.md", text)
        save(reports / "DATA_STATUS.md", text)
        print(f"Subset: {output}")
        print(f"Linked {len(names) - len(missing)}/{len(names)} files; payload {payload / 1024**3:.3f} GiB")
        print(f"Status: {status}")
    
    
    if __name__ == "__main__":
        main()

## Activity

    file changes: Completed · 1 changes
    Add: /home/linfu/src/Test/ObjectConceptLearning/data/.gitignore
    /ImageNet/
    /imagenet_index/
    /test_subset/
    /transfer_lists/*.lock

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/build_test_subset.py
    @@ -120,3 +120,3 @@
     The OCL author previously supplied missing originals on request in issue 1:
    -https://github.com/silicx/ObjectConceptLearning/issues/1#issuecomment-1875649083
    +https://github.com/silicx/ObjectConceptLearning/issues/1
     

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import ast,json
        for name in ['audit_test_data.py','build_test_subset.py','download_imagenet_subset.py','download_selected_web.py','recover_web_images.py']:
         ast.parse(Path(name).read_text(),filename=name)
        print('All preparation scripts parse successfully')
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        print('Recovery',r['recovered'],'pending',r['pending'])
        for name in ['ImageNet/val/ILSVRC2012_val_00023687.JPEG','from_web/val_2026.jpg']:
         print(name,Path(name).stat().st_size if Path(name).exists() else 'missing')
        PY
    All preparation scripts parse successfully
    Recovery 20 pending 47
    ImageNet/val/ILSVRC2012_val_00023687.JPEG 216177
    from_web/val_2026.jpg 130
    ✓ • 0ms

## Assistant

精简上传目录的生成脚本已准备好，预计数据和标注合计约 5.5 GiB。原图与标注将保持原样；最终报告会列出仍缺失的网页图片，以及导致 9 个 ImageNet 对象无法正常裁剪的坐标问题。

## Activity

    $ rg --files --hidden --no-ignore /home/linfu/src/Test -g '*from_web*.tgz' -g '*from_web*.zip' -g 'val_2026.jpg' -g 'val_0761.jpg'
    /home/linfu/src/Test/ObjectConceptLearning/data/from_web.tgz
    /home/linfu/src/Test/ObjectConceptLearning/data/from_web/val_2026.jpg
    ✓ • 136ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        print('recovered',r['recovered'],'pending',r['pending'])
        for x in r['results']:
         if x['name']=='from_web/val_2026.jpg':print(x)
        print('remaining_missing_web',sum(n.startswith('from_web/') and not Path(n).is_file() for n in Path('transfer_lists/ocl_non_imagenet.txt').read_text().splitlines()))
        print('current_transient_failures',sum(any('429' in a.get('error','') for a in x['attempts']) for x in r['results']))
        PY
    recovered 21 pending 22
    {'name': 'from_web/val_2026.jpg', 'original_url': 'http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg', 'attempts': [{'url': 'https://web.archive.org/web/20140808163827id_/http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg', 'error': "HTTPSConnectionPool(host='web.archive.org', port=443): Read timed out. (read timeout=15)"}], 'snapshot': {'status': '200', 'available': True, 'url': 'http://web.archive.org/web/20140808163827/http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg', 'timestamp': '20140808163827'}, 'status': 'unavailable'}
    remaining_missing_web 194
    current_transient_failures 22
    ✓ • 82ms

## Activity

    $ curl -L --fail --max-time 90 --connect-timeout 15 --retry 1 --retry-delay 5 --silent --show-error 'https://web.archive.org/web/20140808163827id_/http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg' -o /tmp/ocl-val-2026-original.jpg
    curl: (22) The requested URL returned error: 404
    ✗ (22) • 644ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        from PIL import Image
        import json
        rows=[json.loads(line) for line in Path('transfer_lists/test_image_integrity.jsonl').read_text().splitlines()]
        ims=[r for r in rows if r['name'].startswith('ImageNet/') and r['status']=='valid']
        print('ImageNet dimensions',Counter((r['width'],r['height']) for r in ims).most_common(8))
        print('not256x256',sum((r['width'],r['height'])!=(256,256) for r in ims),'of',len(ims))
        print('ImageNet raw size',sum(r['size_bytes'] for r in ims))
        print('latest_recovered',json.loads(Path('transfer_lists/web_recovery_report.json').read_text())['recovered'])
        PY
    ImageNet dimensions [((500, 375), 1837), ((500, 333), 806), ((375, 500), 316), ((333, 500), 204), ((500, 334), 175), ((500, 332), 131), ((500, 400), 87), ((640, 480), 82)]
    not256x256 7924 of 7924
    ImageNet raw size 879082015
    latest_recovered 22
    ✓ • 388ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B recover_web_images.py --retry-transient --request-delay 3
    Recovery 10/107; recovered 16
    Recovery 20/107; recovered 17
    Recovery 30/107; recovered 18
    Recovery 40/107; recovered 19
    Recovery 50/107; recovered 20
    Recovery 60/107; recovered 20
    Recovery 70/107; recovered 20
    Recovery 80/107; recovered 20
    Recovery 90/107; recovered 21
    Recovery 100/107; recovered 23
    Recovery 107/107; recovered 23
    ✗ (1) • 6m 36s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        print('recovery_summary',{k:v for k,v in r.items() if k!='results'})
        print('remaining_missing_web',sum(n.startswith('from_web/') and not Path(n).is_file() for n in Path('transfer_lists/ocl_non_imagenet.txt').read_text().splitlines()))
        print('unavailable_reasons',Counter('rate_limit' if '429' in a.get('error','') else 'no_snapshot' if 'No snapshot' in a.get('error','') else a.get('error','')[:45] for x in r['results'] if x['status']=='unavailable' for a in x['attempts']))
        PY
    recovery_summary {'requested': 216, 'recovered': 23, 'pending': 0}
    remaining_missing_web 192
    unavailable_reasons Counter({'no_snapshot': 162, "HTTPSConnectionPool(host='archive.org', port=": 26, "HTTPSConnectionPool(host='web.archive.org', p": 2, 'cannot identify image file <_io.BytesIO objec': 1, '404 Client Error: Not Found for url: https://': 1, '503 Server Error: Service Unavailable for url': 1})
    ✓ • 112ms

## Assistant

目前已补回 77 张网页原图，仍缺 192 张。其中一些存档查询是超时，我会再做一次低频重试。ImageNet、COCO 和 aPY 所需图片均已齐全；数据是否能完整测试，仍取决于剩余网页图片和坐标问题的处理。

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/recover_web_images.py
    @@ -23,5 +23,6 @@
         parser.add_argument("--request-delay", type=float, default=2.0)
    +    parser.add_argument("--timeout", type=float, default=20)
         args = parser.parse_args()
    -    if args.request_delay < 1:
    -        parser.error("Use a request delay of at least one second")
    +    if args.request_delay < 1 or args.timeout <= 0:
    +        parser.error("Use a request delay of at least one second and a positive timeout")
         root = Path(__file__).resolve().parent
    @@ -91,3 +92,3 @@
                 try:
    -                with get(session, url, stream=True, timeout=(8, 15)) as response:
    +                with get(session, url, stream=True, timeout=(8, args.timeout)) as response:
                         response.raise_for_status()
    @@ -117,3 +118,3 @@
                                        params={"url": urls[name], "timestamp": "20220101"},
    -                                   timeout=(8, 15))
    +                                   timeout=(8, args.timeout))
                 response.raise_for_status()

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        import json,os,shutil,subprocess,sys,tempfile
        from pathlib import Path
        scripts=['build_test_subset.py','audit_test_data.py','download_imagenet_subset.py','extract_imagenet_subset.py','download_selected_web.py','download_web_images.py','recover_web_images.py']
        with tempfile.TemporaryDirectory(prefix='ocl-subset-check-') as tmp:
         root=Path(tmp)
         for name in scripts:shutil.copyfile(name,root/name)
         (root/'transfer_lists').mkdir();(root/'resources').mkdir();(root/'COCO/train2014').mkdir(parents=True)
         source=root/'COCO/train2014/example.jpg';source.write_bytes(b'original fixture bytes')
         (root/'resources/example.json').write_text('{}\n')
         (root/'transfer_lists/test_data.txt').write_text('COCO/train2014/example.jpg\nfrom_web/missing.jpg\nresources/example.json\n')
         audit={'ready_for_full_evaluation':False,'required_images':2,'selected_objects':2,'excluded_invalid_boxes':[]}
         (root/'transfer_lists/data_audit.json').write_text(json.dumps(audit))
         command=[sys.executable,'-B',str(root/'build_test_subset.py')]
         for _ in range(2):subprocess.run(command,check=True,capture_output=True)
         target=root/'test_subset/COCO/train2014/example.jpg'
         assert os.path.samefile(source,target)
         assert not (root/'test_subset/from_web/missing.jpg').exists()
         replacement=root/'replacement';replacement.write_bytes(b'recovered fixture bytes');replacement.replace(source)
         subprocess.run(command,check=True,capture_output=True)
         assert os.path.samefile(source,target) and target.read_bytes()==b'recovered fixture bytes'
         target.unlink();target.write_bytes(b'user edited fixture')
         result=subprocess.run(command,capture_output=True,text=True)
         assert result.returncode!=0 and 'Unexpected file change' in result.stderr
         assert target.read_bytes()==b'user edited fixture'
         print('Subset checks passed: hard-link reuse, missing-file reporting, refreshed downloads, and protection of unexpected edits.')
        PY
    Subset checks passed: hard-link reuse, missing-file reporting, refreshed downloads, and protection of unexpected edits.
    ✓ • 365ms

## Activity

    $ git diff --stat
     .gitignore                  |   7 +++
     README.md                   |   9 ++-
     data/download_web_images.py | 137 ++++++++++++++++++++++++++++++++++++++++----
     data/prepare_data.sh        |   3 +-
     4 files changed, 142 insertions(+), 14 deletions(-)
    ✓ • 20ms

## Activity

    $ git status --short
     M .gitignore
     M README.md
     M data/download_web_images.py
     M data/prepare_data.sh
    ?? Test.md
    ?? aPY/
    ?? clip_dataset.py
    ?? clip_inference.py
    ?? data/.gitignore
    ?? data/audit_test_data.py
    ?? data/build_test_subset.py
    ?? data/download_imagenet_subset.py
    ?? data/download_selected_web.py
    ?? data/extract_imagenet_subset.py
    ?? data/from_web.tgz
    ?? data/from_web.tgz:Zone.Identifier
    ?? data/recover_web_images.py
    ?? data/resources/OCL_annot_test.pkl
    ?? data/resources/OCL_annot_train.pkl
    ?? data/resources/OCL_annot_val.pkl
    ?? data/transfer_lists/
    ?? data/web_download_failures.json
    ?? docs/clip_inference.md
    ?? requirements-clip.txt
    ?? setup_clip_gpu.sh
    ?? tests/
    ✓ • 0ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/audit_test_data.py
    @@ -112,4 +112,8 @@
         corrupt = [r for r in ordered if r["status"] == "corrupt"]
    -    crop_errors = [{"image_name": r["name"], **error}
    +    crop_errors = [{"image_name": r["name"], "image_size": [r["width"], r["height"]], **error}
                        for r in ordered for error in r.get("crop_errors", [])]
    +    imagenet_rows = [r for r in ordered if r["name"].startswith("ImageNet/")
    +                     and r["status"] == "valid"]
    +    imagenet_boxes = [obj["box"] for name in names if name.startswith("ImageNet/")
    +                      for _, obj in objects[name] if "box" in obj]
         by_source = {}
    @@ -136,2 +140,10 @@
             "crop_errors": crop_errors, "label_errors": label_errors,
    +        "imagenet_coordinate_diagnostic": {
    +            "selected_boxes": len(imagenet_boxes),
    +            "maximum_box_coordinate": max((max(box) for box in imagenet_boxes), default=None),
    +            "available_images_not_256_square": sum(
    +                (r["width"], r["height"]) != (256, 256) for r in imagenet_rows
    +            ),
    +            "note": "Coordinates appear based on a 256-square frame. The correct resize/crop convention remains unconfirmed; no transform was applied.",
    +        },
             "transfer_manifest_keeps_missing_paths": True,

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        print('recovery_counts',r['recovered'],'pending',r['pending'])
        print('missing_web',sum(n.startswith('from_web/') and not Path(n).is_file() for n in Path('transfer_lists/ocl_non_imagenet.txt').read_text().splitlines()))
        PY
    recovery_counts 25 pending 13
    missing_web 190
    ✓ • 0ms

## Assistant

低频重试又恢复了 2 张原图，目前共补回 79 张。下载任务结束后，我会更新完整校验报告，并核对上传目录的文件数、硬链接和校验和；当前仍缺的文件会明确列出。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        print('pending',r['pending'],'recovered',r['recovered'])
        for x in r['results']:
         if x['name']=='from_web/val_2026.jpg': print('val_2026',x['status'],x['attempts'][-1] if x['attempts'] else '')
        print('Temporary_image_files',len(list(Path('ImageNet').rglob('*.part')))+len(list(Path('from_web').glob('*.part'))))
        PY
    pending 6 recovered 25
    val_2026 unavailable {'url': 'https://web.archive.org/web/20140808163827id_/http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg', 'error': '404 Client Error: NOT FOUND for url: https://web.archive.org/web/20140808163827id_/http://images.china.cn/attachement/jpg/site1000/20140808/001aa0bce274154e59892e.jpg'}
    Temporary_image_files 0
    ✓ • 0ms

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B build_test_subset.py
    Subset: /home/linfu/src/Test/ObjectConceptLearning/data/test_subset
    Linked 35450/35640 files; payload 5.433 GiB
    Status: INCOMPLETE - do not report full-test metrics yet
    ✓ • 15.99s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B recover_web_images.py --retry-transient --request-delay 4 --timeout 45
    Recovery 10/29; recovered 24
    Recovery 20/29; recovered 25
    Recovery 29/29; recovered 25
    ✗ (1) • 2m 51s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import os,json
        root=Path('.')
        subset=root/'test_subset'
        manifest=json.loads((root/'transfer_lists/subset_manifest.json').read_text())
        print('subset', {k:v for k,v in manifest.items() if k!='missing_files'})
        print('root_directories',sorted(p.name for p in subset.iterdir() if p.is_dir()))
        print('symbolic_links',sum(p.is_symlink() for p in subset.rglob('*')))
        print('sources_share_inodes',all(os.path.samefile(root/n,subset/n) for n in (root/'transfer_lists/test_data.txt').read_text().splitlines() if (root/n).is_file()))
        PY
    subset {'ready_for_full_evaluation': False, 'required_files': 35640, 'linked_files': 35450, 'payload_bytes': 5833506637, 'selection': 'All objects from the top ten categories across train + val + test', 'storage': 'Hard links locally; ordinary files when transferred with rsync'}
    root_directories ['COCO', 'ImageNet', 'aPY', 'from_web', 'resources', 'transfer_lists']
    symbolic_links 0
    sources_share_inodes True
    ✓ • 1.65s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        import json
        r=json.loads(Path('transfer_lists/web_recovery_report.json').read_text())
        errors=[a.get('error','') for x in r['results'] if x['status']=='unavailable' for a in x['attempts']]
        print('Final_recovery',r['recovered'],'pending',r['pending'])
        print('Rate_limits',sum('429' in e for e in errors),'Timeouts',sum('timed out' in e for e in errors),'No_snapshot',sum('No snapshot' in e for e in errors))
        PY
    Final_recovery 25 pending 0
    Rate_limits 0 Timeouts 0 No_snapshot 186
    ✓ • 0ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/linfu/src/Test/ObjectConceptLearning/data/build_test_subset.py
    @@ -21,2 +21,14 @@
         audit = json.loads((reports / "data_audit.json").read_text())
    +    urls = {name: url for url, name in
    +            json.loads((root / "resources/url_to_filename.json").read_text())}
    +    unresolved_web = {name: {"name": name, "url": urls.get(name), "reason": "missing"}
    +                      for name in audit["missing_images"] if name.startswith("from_web/")}
    +    for error in audit["crop_errors"]:
    +        name = error["image_name"]
    +        if name.startswith("from_web/"):
    +            unresolved_web[name] = {"name": name, "url": urls.get(name),
    +                                    "reason": "image dimensions incompatible with annotated object",
    +                                    "image_size": error.get("image_size"), "box": error["box"]}
    +    save(reports / "unresolved_web_images.json",
    +         json.dumps(list(unresolved_web.values()), indent=2) + "\n")
         marker = output / ".ocl-subset.json"
    @@ -119,2 +131,5 @@
     web_recovery_report.json under transfer_lists/ for attempts and recovered sources.
    +These are historical attempt reports; data_audit.json shows the current state.
    +unresolved_web_images.json lists missing or unusable web images with original URLs
    +so that the exact originals can be requested from an existing dataset backup.
     The OCL author previously supplied missing originals on request in issue 1:

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B audit_test_data.py --workers 12
    Validated 5000/35633 images
    Validated 10000/35633 images
    Validated 15000/35633 images
    Validated 20000/35633 images
    Validated 25000/35633 images
    Validated 30000/35633 images
    Validated 35000/35633 images
    {
      "generated_at": "2026-10-22T18:53:26.815713+00:00",
      "ready_for_full_evaluation": false,
      "selection_splits": [
        "train",
        "val",
        "test"
      ],
      "count_unit": "object_instance",
      "selected_categories": {
        "dog": 16171,
        "bird": 13961,
        "sheep": 13821,
        "car": 11511,
        "motorcycle": 8519,
        "apple": 8382,
        "cattle": 8379,
        "broccoli": 8333,
        "truck": 7769,
        "elephant": 7032
      },
      "selected_objects": 103878,
      "expected_evaluation_objects": 103877,
      "objects_blocked_by_missing_or_corrupt_images": 285,
      "required_images": 35633,
      "sources": {
        "COCO": {
          "valid": 25067,
          "required": 25067
        },
        "ImageNet": {
          "valid": 7924,
          "required": 7924
        },
        "aPY": {
          "valid": 1168,
          "required": 1168
        },
        "from_web": {
          "valid": 1284,
          "missing": 190,
          "required": 1474
        }
      },
      "valid_image_bytes": 5773865781,
      "vocabulary_sizes": {
        "object": 381,
        "attribute": 114,
        "affordance": 170
      },
      "excluded_invalid_boxes": [
        {
          "image_name": "COCO/val2014/COCO_val2014_000000315601.jpg",
          "object_index": 12,
          "category": "car",
          "box": [
            0,
            266,
            4,
            266
          ]
        }
      ],
      "crop_errors": [
        {
          "image_name": "ImageNet/train/n02089078/n02089078_178.JPEG",
          "image_size": [
            150,
            150
          ],
          "object_index": 0,
          "box": [
            0.0,
            194.51502990722656,
            64.61176300048828,
            255.5253448486328
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02095314/n02095314_6284.JPEG",
          "image_size": [
            140,
            140
          ],
          "object_index": 2,
          "box": [
            149,
            93,
            235,
            202
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02100735/n02100735_1090.JPEG",
          "image_size": [
            129,
            97
          ],
          "object_index": 0,
          "box": [
            99,
            160,
            170,
            255
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n02108000/n02108000_3426.JPEG",
          "image_size": [
            89,
            89
          ],
          "object_index": 1,
          "box": [
            123.6557388305664,
            84.18275451660156,
            225.13156127929688,
            205.0046844482422
          ],
          "category": "dog"
        },
        {
          "image_name": "ImageNet/train/n03796401/n03796401_5457.JPEG",
          "image_size": [
            150,
            105
          ],
          "object_index": 1,
          "box": [
            90.1938247680664,
            167.32815551757812,
            199.00621032714844,
            251.77113342285156
          ],
          "category": "truck"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "image_size": [
            158,
            210
          ],
          "object_index": 2,
          "box": [
            183.3660888671875,
            214.6282196044922,
            246.3701171875,
            254.4662322998047
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "image_size": [
            158,
            210
          ],
          "object_index": 7,
          "box": [
            162.5959014892578,
            51.40813446044922,
            244.72694396972656,
            104.85037231445312
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "image_size": [
            158,
            210
          ],
          "object_index": 13,
          "box": [
            215.67884826660156,
            63.491458892822266,
            256.0,
            123.73628997802734
          ],
          "category": "broccoli"
        },
        {
          "image_name": "ImageNet/train/n07715103/n07715103_12246.JPEG",
          "image_size": [
            158,
            210
          ],
          "object_index": 16,
          "box": [
            207.257080078125,
            173.25148010253906,
            256.0,
            254.88124084472656
          ],
          "category": "broccoli"
        },
        {
          "image_name": "from_web/val_2026.jpg",
          "image_size": [
            24,
            24
          ],
          "object_index": 0,
          "box": [
            297,
            44,
            528,
            346
          ],
          "category": "elephant"
        }
      ],
      "label_errors": [],
      "imagenet_coordinate_diagnostic": {
        "selected_boxes": 14855,
        "maximum_box_coordinate": 261,
        "available_images_not_256_square": 7924,
        "note": "Coordinates appear based on a 256-square frame. The correct resize/crop convention remains unconfirmed; no transform was applied."
      },
      "transfer_manifest_keeps_missing_paths": true
    }
    Report: /home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/data_audit.json
    ✗ (1) • 1m 12s

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -u -B build_test_subset.py
    Subset: /home/linfu/src/Test/ObjectConceptLearning/data/test_subset
    Linked 35450/35640 files; payload 5.433 GiB
    Status: INCOMPLETE - do not report full-test metrics yet
    ✓ • 3.96s

## Assistant

下载和恢复任务已结束。最终检查确认：35,633 张目标图片中，35,443 张可解码，仍缺 190 张网页原图；另有 1 张网页占位图和 9 个 ImageNet 对象存在裁剪问题。我正在核对精简目录与校验和，目录中的报告会明确标记为尚未满足完整评测条件。

## Activity

    $ /home/linfu/src/Test/ObjectConceptLearning/.venv/bin/python -B - <<'PY'
        from pathlib import Path
        from collections import Counter
        import json,os
        root=Path('.');subset=root/'test_subset'
        audit=json.loads((root/'transfer_lists/data_audit.json').read_text())
        names=(root/'transfer_lists/test_data.txt').read_text().splitlines()
        existing=[n for n in names if (root/n).is_file()]
        assert all((subset/n).is_file() and os.path.samefile(root/n,subset/n) for n in existing)
        assert not any(p.is_symlink() for p in subset.rglob('*'))
        assert (root/'transfer_lists/data_audit.json').read_bytes()==(subset/'transfer_lists/data_audit.json').read_bytes()
        checks=(subset/'transfer_lists/available_files.sha256').read_text().splitlines()
        assert len(checks)==len(existing)
        assert len(audit['missing_images'])==len(names)-len(existing)
        url_report=json.loads((subset/'transfer_lists/unresolved_web_images.json').read_text())
        print('Final directory and manifest checks passed')
        print('required_images',audit['required_images'],'missing_images',len(audit['missing_images']))
        print('images_by_source',audit['sources'])
        print('selected_objects',audit['selected_objects'],'expected_after_box_filter',audit['expected_evaluation_objects'])
        print('objects_missing_images',audit['objects_blocked_by_missing_or_corrupt_images'])
        print('crop_errors_by_source',dict(Counter(x['image_name'].split('/')[0] for x in audit['crop_errors'])))
        print('unresolved_web_originals',len(url_report))
        print('payload_GiB',sum((root/n).stat().st_size for n in existing)/1024**3)
        print('subset_total_GiB',sum(p.stat().st_size for p in subset.rglob('*') if p.is_file() and p.name!='.ocl-subset.json')/1024**3)
        print('required_image_hash_records',len(checks)-7)
        print('partial_image_files',len(list((root/'ImageNet').rglob('*.part')))+len(list((root/'from_web').glob('*.part'))))
        PY
    Final directory and manifest checks passed
    required_images 35633 missing_images 190
    images_by_source {'COCO': {'valid': 25067, 'required': 25067}, 'ImageNet': {'valid': 7924, 'required': 7924}, 'aPY': {'valid': 1168, 'required': 1168}, 'from_web': {'valid': 1284, 'missing': 190, 'required': 1474}}
    selected_objects 103878 expected_after_box_filter 103877
    objects_missing_images 285
    crop_errors_by_source {'ImageNet': 9, 'from_web': 1}
    unresolved_web_originals 191
    payload_GiB 5.432876420207322
    subset_total_GiB 5.448726110160351
    required_image_hash_records 35443
    partial_image_files 0
    ✓ • 2.00s

## Activity

    $ sha256sum --quiet -c transfer_lists/available_files.sha256
    ✓ • 1m 33s

## Assistant

已检查并续传，已有图片已复用，**目前仍未完全满足 `Test.md`**。

- ImageNet：7,924 张全部下载完成，约 0.82 GiB。
- COCO、aPY：所需图片齐全。
- 网页图片：补回 79 张，重试原链接和历史存档后仍缺 190 张。
- 已整理 `data/test_subset/`，约 **5.45 GiB**；使用硬链接避免重复存储，现有文件通过了解码和 SHA256 校验。

此外，发现 **1 张网页占位图**，以及 **9 个 ImageNet 对象裁剪失败**；ImageNet 标注的坐标缩放规则仍需确认。

上传时，将 `data/test_subset/` 的内容放到服务器项目的 `data/`。详见：

- [上传与校验说明](/home/linfu/src/Test/ObjectConceptLearning/data/test_subset/README.md)
- [完整检查报告](/home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/data_audit.json)
- [缺失或不可用网页原图清单](/home/linfu/src/Test/ObjectConceptLearning/data/transfer_lists/unresolved_web_images.json)
