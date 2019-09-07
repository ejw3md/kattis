#include <iostream>
#include <cmath>

#define PI 3.14159265

using namespace std;

typedef pair<double, double> coord;

bool is_in_circle(coord c, coord center, double radius)
{
    return pow((c.first-center.first), 2) + pow((c.second-center.second), 2) <= pow(radius, 2);
}

coord rotate(coord pivot, double radius, double angle)
{
    coord c;
    c.first = pivot.first + radius*cos(PI/180*angle);
    c.second = pivot.second + radius*sin(PI/180*angle);

    return c;
}

int catch_mosquitos(coord mosquitos[], int m, coord center, double radius)
{
    int caught = 0;
    for( int i=0; i<m; i++)
    {
        if(is_in_circle(mosquitos[i], center, radius))
        {
            caught+=1;
        }
    }
    return caught;
}

int idk(coord mosquitos[], int m, double radius)
{
    int max_caught =0;
    double angle_dif = .1;
    int caught = 0;
    for(int i=0; i<m; i++)
    {
        double angle = 0;
        while( angle < 360)
        {
            coord center = rotate(mosquitos[i], radius, angle);
            caught = catch_mosquitos(mosquitos, m, center, radius);
            angle+=angle_dif;
            if( caught> max_caught)
            {
                max_caught = caught;
            }

        }
    }
    return  max_caught;
}

void do_it()
{
    int m;
    double diameter;
    cin>>m>>diameter;
    double radius = diameter/2;
    coord mosquitos[m];
    for(int i=0; i<m; i++)
    {
        coord temp;
        cin>>temp.first>>temp.second;
        mosquitos[i] = temp;

    }
    cout<<idk(mosquitos, m, radius)<<endl;
}

int main()
{
    int cases;
    cin>>cases;
    for(int i=0; i<cases; i++)
    {
        do_it();
    }

    return 0;
}