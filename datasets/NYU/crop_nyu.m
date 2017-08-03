% overscan 
clear all;
close all;
clc;
load nyu_depth_v2_labeled;
clearvars rawDepths;
clearvars instances;
clearvars labels;
crop_para = [33 25 575 431];
images_src = images;
depths_src = depths;
images = zeros(432,576,3,1449, 'uint8');
depths = zeros(432,576,1449, 'single');
for i=1:1449
    temp1 = imcrop(images_src(:,:,:,i), crop_para);
    temp2 = imcrop(depths_src(:,:,i), crop_para);
    images(:,:,:,i) = temp1;
    depths(:,:,i) = temp2;
end
save('nyu_v2_432x576', 'images', 'depths' , '-v7.3' );
