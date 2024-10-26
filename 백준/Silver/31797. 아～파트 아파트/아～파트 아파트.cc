#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    deque<pair<int, int>> hands;

    // 각 참가자의 손 높이와 번호를 입력받아 deque에 저장
    for (int i = 1; i <= M; ++i) {
        int H1, H2;
        cin >> H1 >> H2;
        hands.push_back({H1, i});
        hands.push_back({H2, i});
    }

    // 손 높이 기준으로 정렬
    sort(hands.begin(), hands.end());

    // N번 반복하여 가장 아래 손을 위로 올리기
    for (int i = 0; i < N; ++i) {
        auto hand = hands.front();  // 가장 아래 손을 가져오고
        hands.pop_front();          // 아래 손을 제거한 후
        hands.push_back(hand);      // 맨 위로 다시 추가
    }

    // N번째 층에 해당하는 참가자의 번호 출력
    cout << hands.back().second << endl;

    return 0;
}
