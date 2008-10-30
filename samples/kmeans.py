#!/usr/bin/python
from opencv import *
from ctypes import *
from random import randint
MAX_CLUSTERS=5

if __name__ == "__main__":

    color_tab = [
        CV_RGB(255,0,0),
        CV_RGB(0,255,0),
        CV_RGB(100,100,255),
        CV_RGB(255,0,255),
        CV_RGB(255,255,0)];
    img = cvCreateImage( cvSize( 500, 500 ), 8, 3 );
    rng = cvRNG(-1);

    cvNamedWindow( "clusters", 1 );
        
    while True:
        cluster_count = randint(2, MAX_CLUSTERS)
        sample_count = randint(1, 1000)
        points = cvCreateMat( sample_count, 1, CV_32FC2 );
        clusters = cvCreateMat( sample_count, 1, CV_32SC1 );
        
        # generate random sample from multigaussian distribution
        for k in range(cluster_count):
            center = CvPoint();
            center.x = cvRandInt(rng)%img[0].width;
            center.y = cvRandInt(rng)%img[0].height;
            first = k*sample_count/cluster_count
            last = sample_count
            if k != cluster_count:
                last = (k+1)*sample_count/cluster_count

            point_chunk = pointer(CvMat())
            cvGetRows(points, point_chunk, first, last)
            
            cvRandArr( byref(rng), point_chunk, CV_RAND_NORMAL,
                       cvScalar(center.x,center.y,0,0),
                       cvScalar(img[0].width*0.1,img[0].height*0.1,0,0));
        

        # shuffle samples 
        cvRandShuffle( points, rng )

        cvKMeans2( points, cluster_count, clusters,
                   cvTermCriteria( CV_TERMCRIT_EPS+CV_TERMCRIT_ITER, 10, 1.0 ));

        cvZero( img );

        for i in range(sample_count):
            cluster_idx = clusters[0].data.i[i]
            ipt = CvPoint(int(points[0].data.fl[i*2]), int(points[0].data.fl[i*2+1]))
            cvCircle( img, ipt, 2, color_tab[cluster_idx], CV_FILLED, CV_AA, 0 );
        
        cvReleaseMat(points)
        cvReleaseMat(clusters)

        cvShowImage( "clusters", img );

        key = cvWaitKey(0)
        if( key == 27 or key == 'q' or key == 'Q' ): # 'ESC'
            break;
    
    
    cvDestroyWindow( "clusters" );
    cvReleaseImage(img)
    