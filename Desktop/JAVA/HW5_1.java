import java.util.*;

public class PhoneBook {
    public static void main(String[] args) {
        HashMap<String, List<String>> phoneBook = new HashMap<>();
        phoneBook.put("Иван Иванов", Arrays.asList("111-111-111", "222-222-222"));
        phoneBook.put("Светлана Петрова", Arrays.asList("333-333-333"));
        phoneBook.put("Кристина Белова", Arrays.asList("444-444-444", "555-555-555"));
        phoneBook.put("Анна Мусина", Arrays.asList("666-666-666"));
        phoneBook.put("Анна Крутова", Arrays.asList("777-777-777"));
        phoneBook.put("Иван Юрин", Arrays.asList("888-888-888"));
        phoneBook.put("Петр Лыков", Arrays.asList("999-999-999"));
        phoneBook.put("Павел Чернов", Arrays.asList("000-000-000"));
        phoneBook.put("Петр Чернышов", Arrays.asList("111-111-111"));
        phoneBook.put("Мария Федорова", Arrays.asList("222-222-222"));
        phoneBook.put("Марина Светлова", Arrays.asList("333-333-333"));
        phoneBook.put("Мария Савина", Arrays.asList("444-444-444"));
        phoneBook.put("Мария Рыкова", Arrays.asList("555-555-555"));
        phoneBook.put("Марина Лугова", Arrays.asList("666-666-666"));
        phoneBook.put("Анна Владимирова", Arrays.asList("777-777-777"));
        phoneBook.put("Иван Мечников", Arrays.asList("888-888-888"));
        phoneBook.put("Петр Петин", Arrays.asList("999-999-999"));
        phoneBook.put("Иван Ежов", Arrays.asList("000-000-000"));

        HashMap<String, Integer> nameCount = new HashMap<>();
        for (String name : phoneBook.keySet()) {
            String firstName = name.split(" ")[0];
            if (nameCount.containsKey(firstName)) {
                nameCount.put(firstName, nameCount.get(firstName) + 1);
            } else {
                nameCount.put(firstName, 1);
            }
        }

        List<Map.Entry<String, Integer>> sortedNames = new ArrayList<>(nameCount.entrySet());
        sortedNames.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        for (Map.Entry<String, Integer> entry : sortedNames) {
            if (entry.getValue() > 1) {
                System.out.println(entry.getKey() + " - " + entry.getValue() + " раз(а)");
            }
        }
    }
}