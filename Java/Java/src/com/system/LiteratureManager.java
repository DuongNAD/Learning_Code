package com.system;

import com.library.literature.LiteraryWork;

import java.util.ArrayList;
import java.util.List;

public class LiteratureManager {
    private List<LiteraryWork> works;

    public LiteratureManager() {
        works = new ArrayList<>();
    }

    public void addWork() {
        System.out.println("--- Thêm 1 tác phẩm mới ---");
        LiteraryWork newWork = new LiteraryWork();

        newWork.inputDetails();
        this.works.add(newWork);
        System.out.println("==> Đã thêm tác phẩm '" + newWork.getTitle() + "' vào thư viện thành công!");
    }

    public void showWorks() {
        if(this.works.isEmpty()) {
            System.out.println("Thư viện hiện chưa có tác phẩm nào");
            return;
        }
        System.out.println("=== TẤT CẢ CÁC TÁC PHẨM TRONG THƯ VIỆN ===");
        for (LiteraryWork work : this.works) {
            work.displayDetails();
        }
    }

    public void findLongestWork(){
        if(this.works.isEmpty()) {
            System.out.println("Thư viện hiện chưa có tác phẩm nào");
            return;
        }

        LiteraryWork longestWork = this.works.get(0);

        for(LiteraryWork work : this.works){
            if(work.getPageCount() > longestWork.getPageCount()){
                longestWork = work;
            }
        }

        System.out.println("\n--- TÁC PHẨM DÀI NHẤT (CÓ SỐ TRANG NHIỀU NHẤT) ---");
        longestWork.displayDetails();
    }
}
