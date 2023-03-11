function twoSum(nums: number[], target: number): number[] {
  const numberMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const remainder = target - nums[i];

    if (numberMap.has(remainder)) {
      return [numberMap.get(remainder), i];
    }

    numberMap.set(nums[i], i);
  }

  return nums;
}
