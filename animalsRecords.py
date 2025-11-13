def animalsRecords():
  records = []

  while True:
      print("\nVyber akci tak, že napíšeš číslo požadované akce:\n\n1 - Přidat zvíře\n2 - Zobrazit seznam\n3 - Vyhledat zvíře\n4 - Konec\n")

      try:
          choose_action = int(input("\nZadej číslo akce: "))
      except ValueError:
          print("\nZadej prosím celé číslo (1–4).")
          continue  

      if choose_action == 1:
          add_animal = input("\nNapiš jméno zvířete, které chceš přidat: ").title()
          records.append(add_animal)
          print(f"\nZvíře '{add_animal}' bylo přidáno do seznamu!")

      elif choose_action == 2:
          if records:
              print("\nSeznam zvířat:")
              for i, animal in enumerate(records, start=1):
                  print(f"{i}. {animal}")
          else:
              print("\nEvidence je zatím prázdná.")

      elif choose_action == 3:
          search = input("\nZadej jméno zvířete pro vyhledání: ").title()
          if search in records:
              print(f"\nZvíře '{search}' bylo nalezeno v evidenci.")
          else:
              print(f"\nZvíře '{search}' nebylo nalezeno.")

      elif choose_action == 4:
          print("\nDobře, končíme program. Měj hezký den!")
          break

      else:
          print("\nNeplatná volba, zkus to znovu!")

animalsRecords()
