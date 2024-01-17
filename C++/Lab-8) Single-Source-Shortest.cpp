// Single Source Shortest Path
#include<iostream>
#define INF 30000
#define R 100
using namespace std;

int n, v, cost[R][R], dist[R];

// Data Input
void input()
{
    int x, y, length;
    cout << "Enter Number of Vertices: ";
    cin >> n;

    for(x = 0; x <= n; x++)     // Elements of cost[][] is
    {
        for(y = 1; y <= n; y++)
        {
            cost[x][y] = INF; // Initializing by Infinite
        }
        cost[x][x] = 0;
    }

    do      // Getting Edges and Cost
    {
        cout << "\nEnter Edge (-1, -1 to Quit): ";
        cin >> x >> y;

        if(x == -1 || y == -1)
            break;

        cout << "Enter Length: ";
        cin >> length;

        cost[x][y] = length;

    }
    while(1);

    cout << "\nEnter Source: ";
    cin >> v;
    cout << "\n";
}

// Single Source Shortest Path

void ShortestPath()
{
    int i, j, temp, u, w, s[R];

    for(i = 1; i <= n; i++)
    {
        s[i] = 0;
        dist[i] = cost[v][i];
    }

    s[v] = 1;
    dist[v] = 0;

    for(i = 2; i < n - 1; i++)
    {
        temp = INF;
        u = 1;

        for(j = 1; j <= n; j++)
        {
            if(s[j] == 0 && dist[j] < temp)
            {
                u = j;
                temp = dist[j];
            }
        }

        s[u] = 1;

        for(w = 1; w <= n; w++)
        {
            if(s[w] == 0 && dist[w] > dist[u] + cost[u][w])
                dist[w] = dist[u] + cost[u][w];
        }
    }
}

// Output

void display()
{
    int i;

    cout << "\nShortest Path From Source " << v << " is:\n";

    for(i = 1; i <= n; i++)
        cout << i << ":" << dist[i] << " ";

    cout << "\n\n";
}

// Main Function

int main()
{
    int q;

    do
    {
        cout << "1. Input Data\n";
        cout << "2. Evaluate Single Source Shortest Path\n";
        cout << "3. Quit\n";
        cout<<"Enter Choice: ";
        cin >> q;

        if(q == 1)
            input();

        else if(q == 2)
        {
            ShortestPath();
            display();
        }
    }
    while(q != 3);

    return 0;
}
