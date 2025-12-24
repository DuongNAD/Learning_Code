void sothuannghich(int arr[], int *n)
{
    int dem = 0;
    for (int i = 0; i < *n; i++)
    {
        if (arr[i] < 0)
        {
            continue;
        }
        int songhichdao = 0;
        int thuc = arr[i];
        while (thuc != 0)
        {
            int tong = thuc % 10;
            thuc /= 10;
            songhichdao = songhichdao * 10 + tong;
        }
        if (arr[i] == songhichdao)
        {
            dem = dem + 1;
            printf("arr[%d] = %d\n", i, arr[i]);
        }
    }
    printf("Tong so thuan nghich = %d", dem);
}