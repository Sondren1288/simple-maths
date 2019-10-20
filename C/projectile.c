//Calculate the distance of a projectile
//10-20-2019 Mathieu Rancourt

#include<stdio.h>
#include <math.h>
int main()
{
    //Known values
    double dy = 51.5;
    double angle = 55;
    double gravity = 9.8;
    double vi = 110;
    
    //Trig values
    double vix = cos(angle*(M_PI/180))*vi;
    double viy = sin(angle*(M_PI/180))*vi;
    //printf("vix = %f\n viy = %f\n", vix, viy);
    
    //quadratic values
    double quada = gravity/2;
    double quadb = -1*viy;
    double quadc = -1*dy;
    double inside = (quadb*quadb)-(4*(quada*quadc));
    
    
    //Zeros/Time given form quadratic formula
    double time1 = ((-1*quadb)+(sqrt(inside)))/gravity;
    double time2 = ((-1*quadb)-(sqrt(inside)))/gravity;
   
    //time can only be positive 
    if (time1 < 0) {
        printf("The distance travelled by the projectile is %0.2f units.\n", (vix*time2));
    }
    
    if (time2 < 0) {
        printf("The distance travelled by the projectile is %0.2f units.\n", (vix*time1));
    }
    
    //debug
    //printf("time1 =%f\n time2 = %f\n", time1, time2);
    
    /*
     
     + (up)
     |
     |
     |
     ------+ (for)
     
     */
    
    return 0;
}
