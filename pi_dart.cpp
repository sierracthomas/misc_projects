#include <cstddef>
#include <iostream>
#include <random>
​
size_t throw_darts(const size_t number_of_throws) {
  std::random_device
    device;  // Will be used to obtain a seed for the random number engine
  std::mt19937 generator(
			 device());  // Standard mersenne_twister_engine seeded with device()
  std::uniform_real_distribution<> distribution(0.0, 1.0);
  size_t dart_hits = 0;
  for (size_t i = 0; i < number_of_throws; ++i) {
    const double x = distribution(generator);
    const double y = distribution(generator);
    if (x * x + y * y <= 1) {
      ++dart_hits;
    }
  }
  return dart_hits;
}
​
int main() {
  const size_t number_of_throws = 10000;
  const double pi_estimate =
    (4.0 * throw_darts(number_of_throws)) / (number_of_throws);
  std::cout << pi_estimate << std::endl;
  return 0;
}
