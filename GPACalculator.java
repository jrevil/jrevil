package gpa;

import java.util.Scanner;

public class GPACalculator {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		System.out.println("Enter number of classes taken this semester: ");
			int total_classes = scanner.nextInt();

		String grades;
		double value;
		double sum = 0;

		for (int i = 0; i < total_classes; i++) {
			System.out.println("Enter letter grade: ");
			grades = scanner.next();

			if (grades.equals("A")) {
				value = 4.0;
				sum += value;
			}
			if (grades.equals("A-")) {
				value = 3.7;
				sum += value;
			}
			if (grades.equals("B+")) {
				value = 3.3;
				sum += value;
			}
			if (grades.equals("B")) {
				value = 3.0;
				sum += value;
			}
			if (grades.equals("B-")) {
				value = 2.7;
				sum += value;
			}
			if (grades.equals("C+")) {
				value = 2.3;
				sum += value;
			}
			if (grades.equals("C")) {
				value = 2.0;
				sum += value;
			}
			if (grades.equals("C-")) {
				value = 1.7;
				sum += value;
			}
			if (grades.equals("D+")) {
				value = 1.3;
				sum += value;
			}
			if (grades.equals("D")) {
				value = 1.0;
				sum += value;
			}
			if (grades.equals("D-")) {
				value = 0.67;
				sum += value;
			}
			if (grades.equals("F")) {
				value = 0.0;
				sum += value;
			}
		}
		double GPA = sum / total_classes;
		System.out.printf("Your GPA is: " + GPA);

	}

}
