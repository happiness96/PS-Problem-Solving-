#include <iostream>
using namespace std;
/*
 -------------------------------------- 
 | Created by happiness96             | 
 | Year 2021                          | 
 | Month 06                           | 
 | Day 27                             | 
 | 18868 멀티버스 Ⅰ                   | 
 -------------------------------------- 
*/

int main(){
    int M, N, result = 0;

    cin >> M >> N;

    int planets[M][N];

    for(int i = 0; i < M; i ++){
        for(int j = 0; j < N; j ++){
            cin >> planets[i][j];
        }
    }

    for(int i = 0; i < M; i ++){
        for(int j = i + 1; j < M; j ++){
            int flag = 1;

            for(int a = 0; a < N; a ++){
                for(int b = 0; b < N; b ++){
                    if(planets[i][a] == planets[i][b] and planets[j][a] == planets[j][b]) continue;
                    else if(planets[i][a] > planets[i][b] and planets[j][a] > planets[j][b]) continue;
                    else if(planets[i][a] < planets[i][b] and planets[j][a] < planets[j][b]) continue;
                    flag = 0;
                    break;
                }
                if(flag == 0) break;
            }
            result += flag;
        }
    }

    cout << result;
    return 0;
}