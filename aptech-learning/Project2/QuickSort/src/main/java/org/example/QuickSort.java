package org.example;

public class QuickSort {

    public void sort(int[] array, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(array, left, right);

            sort(array, left, pivotIndex - 1);
            sort(array, pivotIndex + 1, right);
        }
    }

    private int partition(int[] array, int left, int right) {
        int pivot = array[right];
        int i = left - 1;

        for (int j = left; j < right; j++) {
            if (array[j] <= pivot) {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        int temp = array[i + 1];
        array[i + 1] = array[right];
        array[right] = temp;

        return i + 1;
    }
}