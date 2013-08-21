"""
Future implementations

Enemy item drops
Enemy attack types (magic armor)
Speed
Enemy charging attacks (to defend against)
Storyline
Random monsters (rather than 1, b, d)
"""



import random
print "\t\t\t\t\t\t<WELCOME TO HALCYON DAYS>"
prompt = '> '
def start_game():
	ehp = 0
	enemy_name = ''
	enemy_descrip = ''
	exp_drop = 0
	gold_drop = 0
	attack_type = 1
	eBurn = 0
	eFrozen = 0
	eStun = False
	echarge = False
	focus = False
	firstTalk = True
	potion = 1
	hipotion = 0
	xpotion = 0
	ether = 1
	maxether = 0
	elixir = 0
	megalixir = 0
	bomb = 0
	smoke = 0
	escape = False
	godchance = 0
	seek = 0
	attackAction = False
	smoked = 0
	defend = 1
	
	print "\t\t\t\t\t\t(1) New Game (2) Continue"
	choice = raw_input(prompt)
	print "\t\t\tWhat is your name?"
	name = ''
	while name == '':
		name = raw_input(prompt)
	if choice == '1': #Create new character
		print "\t\t\tWhat class are you?"
		print "\t\t\t(f) for fighter, (m) for mage"
		cclass = ''
		while cclass == '':
			cclass = raw_input(prompt)
		if cclass == 'f':
			cclass = "fighter"
		elif cclass == 'm':
			cclass = "mage"
		#DEFAULT FIGHTER CLASS
		lvl = 1
		exp = 0
		gold = 10
		mhp = 20
		mmp = 5
		attack = 3
		magic = 1
		armor = 1
		mdef = 1
		speed = 3
		crit = 1
		gauge = ''
		if cclass == 'mage': #MAGE CLASS
			mhp -= 2
			mmp += 2
			attack -= 1
			magic += 2
			mdef += 1
			crit -= 1
		hp = mhp
		mp = mmp
		weapon_atk = 1
		weapon_mgc = 1
		weapon_name = 'Wooden Stick'
		armor_def = 0
		armor_mdef = 0
		armor_name = 'Rag'
	elif choice == '2': #Load character
		filename = name + '.txt'
		target = open(filename, 'r')
		cclass = target.readline()[4:].strip()
		lvl = int(target.readline()[4:])
		exp = int(target.readline()[4:])
		gold = int(target.readline()[4:])
		hp = int(target.readline()[4:])
		mhp = int(target.readline()[4:])
		mp = int(target.readline()[4:])
		mmp = int(target.readline()[4:])
		attack = int(target.readline()[4:])
		magic = int(target.readline()[4:])
		armor = int(target.readline()[4:])
		mdef = int(target.readline()[4:])
		speed = int(target.readline()[4:])
		crit = int(target.readline()[4:])
		gauge = target.readline()[4:].strip()
		weapon_name = target.readline().strip()
		weapon_atk = int(target.readline()[4:])
		weapon_mgc = int(target.readline()[4:])
		armor_name = target.readline().strip()
		armor_def = int(target.readline()[4:])
		armor_mdef = int(target.readline()[4:])
		potion = int(target.readline())
		hipotion = int(target.readline())
		xpotion = int(target.readline())
		ether = int(target.readline())
		maxether = int(target.readline())
		elixir = int(target.readline())
		megalixir = int(target.readline())
		bomb = int(target.readline())
		smoke = int(target.readline())
		target.close()
	print "\t\t\t%s is a %s." % (name, cclass)
	print "\t\t\tWelcome,", name, ", to Eliwood. What would you like to do?"
	
	def combatUI():
		print "\t\t\t\t\t\t\t\t\t<", hp, "/", mhp, "hp |", mp, "/", mmp, "mp >"
		print "\t\t\t\t\t\t\t\t\t<<", gauge, ">>"
	def checkBurn(eBurn): #Enemy burn status, takes damage over time
		if eBurn > 0:
			burn_damage = int(round(lvl * 0.75)) + random.randrange(-2, 4)
			if burn_damage < 0:
				burn_damage = 0
			print "\t\t\tThe enemy took", burn_damage, "burn damage."
			return burn_damage
	def eLife(ehp): #Display enemy hp
		print "\t\t\tThe enemy has ", ehp, "hp."
	def noGold():
		print "\t\t\tNot enough gold."
	def bought(item):
		print "\t\t\tThank you for buying", item
	def equip():
		print "\t\t\t<Weapon>", weapon_name, "|", weapon_atk, "ATK", "|", weapon_mgc, "MGC"
		print "\t\t\t< Armor>", armor_name, "|", armor_def, "ARM", "|", armor_mdef, "MDF"
		print "\t"
	def items():
		print "\t\t\t--Inventory--"
		print "\t\t\t<Potions>     ", potion
		print "\t\t\t<Hi-Potions>  ",	hipotion
		print "\t\t\t<X-Potions>   ", xpotion
		print "\t\t\t<Ethers>      ", ether
		print "\t\t\t<Max Ethers>  ", maxether
		print "\t\t\t<Elixirs>     ", elixir
		print "\t\t\t<Megalixirs>  ",	megalixir
		print "\t\t\t<Bombs>	      ",	bomb
		print "\t\t\t<Smokescreens>",	smoke
		print "\t"
	
	while hp > 0:
		if firstTalk == False:
			print "\t\t\tWelcome back", name, ". What would you like to do?"
		else:
			firstTalk = False
		#Town Options
		print "\t\t\t(1) Fight"
		print "\t\t\t(2) Visit Eliwood Inn"
		print "\t\t\t(3) Visit General Store"
		print "\t\t\t(4) View Stats"
		print "\t\t\t(5) View Equipment"
		print "\t\t\t(6) View Items"
		print "\t\t\t(7) Save"
		action = raw_input(prompt)
			
		if action == '4': #View Stats
			print "\t\t\t", name, " is a level", lvl, cclass, "at", exp, "exp."
			print "\t\t\tYou currently have", hp, "/", mhp, "hp and", mp, "/", mmp, "mp."
			print "\t\t\tYou have", gold, "gold."
			print "\t\t\tStats: ATK", attack, "MGC", magic, "ARM", armor, "MDF", mdef, "SPD", speed, "CRT", crit
			print "\n"
		
		elif action == '3': #General Store
			print "\t\t\tWelcome to the General Store"
			print "\t\t\tYou have", gold, "gold."
			print "\t\t\t(1) View Weapons  (2) View Staves"
			print "\t\t\t(3) View Armor    (4) View Items"
			shop = raw_input(prompt)
			if shop == '1':
				print "\t\t\t(1) Pendagger 		|   30G |  3 ATK"
				print "\t\t\t(2) Quoral Rapier 	|   75G |  8 ATK | Life Steal"
				print "\t\t\t(3) Pathfinder		|  100G | 11 ATK"
				print "\t\t\t(4) Firebrand 		|  225G | 12 ATK | Burn Enchanted"
				print "\t\t\t(5) Skyward Blade 	|  225G | 13 ATK | Stun Enchanted"
				print "\t\t\t(6) Serpentine		|  250G | 10 ATK | Frostbite Enchanted"
				print "\t\t\t(7) Muramasa		|  750G | 17 ATK | A Cursed Blade"
				print "\t\t\t(8) Excalibur 		| 1250G | 25 ATK | Crits crits crits!"
				print "\t\t\t(9) Godblade	 	| 2500G |  1 ATK | ????"
				option = raw_input(prompt)
				if option == '1' and gold >= 30:
					weapon_name = 'Pendagger'
					weapon_atk = 3
					weapon_mgc = 0
					gold -= 30
					bought(weapon_name)
				elif option == '2' and gold >= 75:
					weapon_name = 'Quoral Rapier'
					weapon_atk = 8
					weapon_mgc = 0
					gold -= 75
					bought(weapon_name)
				elif option == '3' and gold >= 100:
					weapon_name = 'Pathfinder'
					weapon_atk = 11
					weapon_mgc = 0
					gold -= 100
					bought(weapon_name)
				elif option == '4' and gold >= 250:
					weapon_name = 'Firebrand'
					weapon_atk = 11
					weapon_mgc = 0
					gold -= 250
					bought(weapon_name)
				elif option == '5' and gold >= 250:
					weapon_name = 'Skyward Blade'
					weapon_atk = 13
					weapon_mgc = 0
					gold -= 250
					bought(weapon_name)
				elif option == '6' and gold >= 250:
					weapon_name = 'Serpentine'
					weapon_atk = 10
					weapon_mgc = 0
					gold -= 250
					bought(weapon_name)
				elif option == '7' and gold >= 750:
					weapon_name = 'Muramasa'
					weapon_atk = 17
					weapon_mgc = 0
					gold -= 750
					bought(weapon_name)
				elif option == '8' and gold >= 1250:
					weapon_name = 'Excalibur'
					weapon_atk = 25
					weapon_mgc = 0
					gold -= 1250
					bought(weapon_name)
				elif option == '9' and gold >= 2500:
					weapon_name = 'Godblade'
					weapon_atk = 1
					weapon_mgc = 0
					gold -= 2500
					bought(weapon_name)
				else:
					noGold()
					
			if shop == '2':
				print "\t\t\t(1) Power Source 	|   30G |  3 MGC"
				print "\t\t\t(2) Blackbriar		|   75G |  8 MGC | Escape Mech"
				print "\t\t\t(3) Vorpal Wand 	|  120G | 10 MGC | Mana Regen"
				print "\t\t\t(4) Cthulhu Branch	|  150G | 15 MGC"
				print "\t\t\t(5) Blood Funnel 	|  250G | 13 MGC | Self Inflicting"
				print "\t\t\t(6) Sieglinde 		|  450G | 10 MGC | Ephemeral Boost"
				print "\t\t\t(7) Life Seeker		|  575G | 17 MGC | Life Leech"
				print "\t\t\t(8) Oathkeeper 		| 1500G | 21 MGC | Double Cast"
				print "\t\t\t(9) Harbinger 		| 2250G | 30 MGC | Ultima"	
				option = raw_input(prompt)
				if option == '1' and gold >= 30:
					weapon_name = 'Power Source'
					weapon_atk = 0
					weapon_mgc = 3
					gold -= 30
					bought(weapon_name)
				elif option == '2' and gold >= 75:
					weapon_name = 'Blackbriar'
					weapon_atk = 0
					weapon_mgc = 8
					gold -= 75
					bought(weapon_name)
				elif option == '3' and gold >= 120:
					weapon_name = 'Vorpal Wand'
					weapon_atk = 0
					weapon_mgc = 10
					gold -= 120
					bought(weapon_name)
				elif option == '4' and gold >= 150:
					weapon_name = 'Cthulhu Branch'
					weapon_atk = 0
					weapon_mgc = 15
					gold -= 150
					bought(weapon_name)
				elif option == '5' and gold >= 250:
					weapon_name = 'Blood Funnel'
					weapon_atk = 0
					weapon_mgc = 13
					gold -= 250
					bought(weapon_name)
				elif option == '6' and gold >= 450:
					weapon_name = 'Sieglinde'
					weapon_atk = 0
					weapon_mgc = 10
					gold -= 450
					bought(weapon_name)
				elif option == '7' and gold >= 575:
					weapon_name = 'Life Seeker'
					weapon_atk = 0
					weapon_mgc = 17
					gold -= 575
					bought(weapon_name)
				elif option == '8' and gold >= 1500:
					weapon_name = 'Oathkeeper'
					weapon_atk = 0
					weapon_mgc = 21
					gold -= 1500
					bought(weapon_name)
				elif option == '9' and gold >= 2250:
					weapon_name = 'Harbinger'
					weapon_atk = 0
					weapon_mgc = 30
					gold -= 2250
					bought(weapon_name)
				else:
					noGold()
				
			if shop == '3':
				print "\t\t\t(1) Weavemail 		  |   25G |   2 ARM |   2 MDF"
				print "\t\t\t(2) Barbed Armor	  |   75G |   4 ARM |   1 MDF | Reflect Damage"
				print "\t\t\t(3) Silk Garb 		  |  100G |   3 ARM |   6 MDF"
				print "\t\t\t(4) Enigma 		  |  150G |   7 ARM |   7 MDF | Mystic Healing"
				print "\t\t\t(5) Kraken's Shell	  |  200G |  12 ARM |   5 MDF | Damage Reduce"
				print "\t\t\t(6) Cloak of Shadows	  |  275G |  10 ARM |   2 MDF | Dodge Up"
				print "\t\t\t(7) Fire Vest 		  |  400G |  15 ARM |  10 MDF | Burn Enchanted"
				print "\t\t\t(8) Mirror Armor 	  | 1000G |  20 ARM |  25 MDF | Reflect Damage"
				print "\t\t\t(9) The Forsaken 	  | 2250G | -10 ARM | -10 MDF | Final Resort"
				option = raw_input(prompt)
				if option == '1' and gold >= 25:
					armor_name = 'Weavemail'
					armor_def = 2
					armor_mdef = 2
					gold -= 25
					bought(armor_name)
				elif option == '2' and gold >= 75:
					armor_name = 'Barbed Armor'
					armor_def = 4
					armor_mdef = 1
					gold -= 75
					bought(armor_name)
				elif option == '3' and gold >= 100:
					armor_name = 'Silk Garb'
					armor_def = 3
					armor_mdef = 6
					gold -= 100
					bought(armor_name)
				elif option == '4' and gold >= 150:
					armor_name = 'Enigma'
					armor_def = 7
					armor_mdef = 7
					gold -= 150
					bought(armor_name)
				elif option == '5' and gold >= 200:
					armor_name = 'Kraken\'s Shell'
					armor_def = 12
					armor_mdef = 5
					gold -= 200
					bought(armor_name)
				elif option == '6' and gold >= 275:
					armor_name = 'Cloak of Shadows'
					armor_def = 10
					armor_mdef = 2
					gold -= 275
					bought(armor_name)
				elif option == '7' and gold >= 400:
					armor_name = 'Fire Vest'
					armor_def = 15
					armor_mdef = 10
					gold -= 400
					bought(armor_name)
				elif option == '8' and gold >= 1000:
					armor_name = 'Mirror Armor'
					armor_def = 20
					armor_mdef = 25
					gold -= 1000
					bought(armor_name)
				elif option == '9' and gold >= 2250:
					armor_name = 'The Forsaken'
					armor_def = -10
					armor_mdef = -10
					gold -= 2250
					bought(armor_name)
				else:
					noGold()
					
			if shop == '4':
				print "\t\t\t(1) Potion 	|  10G | Heals A Little HP"
				print "\t\t\t(2) Hi-Potion 	|  50G | Heals Some HP"
				print "\t\t\t(3) X-Potion 	| 100G | Heals A Lot of HP"
				print "\t\t\t(4) Ether 	|  10G | Heals A Little MP"
				print "\t\t\t(5) Max Ether 	|  50G | Heals All MP"
				print "\t\t\t(6) Elixir 	|  50G | Heals Some HP and MP"
				print "\t\t\t(7) Megalixir 	| 150G | Heals All HP and MP"
				print "\t\t\t(8) Bomb 	|  50G | Deals Damage"
				print "\t\t\t(9) Smokescreen |  50G | Makes it Rough to See"
				option = raw_input(prompt)
				if option == '1' and gold >= 10:
					potion += 1
					gold -= 10
					bought('Potion')
				elif option == '2' and gold >= 50:
					hipotion += 1
					gold -= 50
					bought('Hi-Potion')
				elif option == '3' and gold >= 100:
					xpotion += 1
					gold -= 100
					bought('X-Potion')
				elif option == '4' and gold >= 10:
					ether += 1
					gold -= 10
					bought('Ether')
				elif option == '5' and gold >= 50:
					maxether += 1
					gold -= 50
					bought('Max Ether')
				elif option == '6' and gold >= 70:
					elixir += 1
					gold -= 70
					bought('Elixir')
				elif option == '7' and gold >= 150:
					megalixir += 1
					gold -= 150
					bought('Megalixir')
				elif option == '8' and gold >= 50:
					bomb += 1
					gold -= 50
					bought('Bomb')
				elif option == '9' and gold >= 50:
					smoke += 1
					gold -= 50
					bought('Smokescreen')
				else:
					noGold()
					
		elif action == '2': #Visit Eliwood Inn
			print "\t\t\tYou have", gold, "gold."
			print "\t\t\tSleep at inn for 10 gold? (y/n)"
			action = raw_input(prompt)
			if (action == 'y' or action == '1') and gold >= 10:
				print "\t\t\tThank you for staying at the Eliwood Inn."
				gold -= 10
				hp += 10 + int(round(mhp * 0.25))
				if hp >= mhp:
					hp = mhp
				mp = mmp
				print "\t\t\tYou now have", hp, "/", mhp, "hp and", mp, "/", mmp, "mp.\n"
			elif gold < 10:
				noGold()
		elif action == '5': #View Equipment
			equip()
		elif action == '6': #View Items
			items()
		elif action == '7': #Save current game to character file name
			print "\t\t\tSaving game..."
			filename = name + '.txt'
			target = open(filename, 'w')
			save = "CLA:" + cclass + "\n"
			save += "LVL:" + str(lvl) + "\n"
			save += "EXP:" + str(exp) + "\n"
			save += "GOL:" + str(gold) + "\n"
			save += "CHP:" + str(hp) + "\n"
			save += "MHP:" + str(mhp) + "\n"
			save += "CMP:" + str(mp) + "\n"
			save += "MMP:" + str(mmp) + "\n"
			save += "ATK:" + str(attack) + "\n"
			save += "MGC:" + str(magic) + "\n"
			save += "ARM:" + str(armor) + "\n"
			save += "MDF:" + str(mdef) + "\n"
			save += "SPD:" + str(speed) + "\n"
			save += "CRT:" + str(crit) + "\n"
			save += "ULT:" + str(gauge) + "\n"
			save += weapon_name + "\n"
			save += "WPN:" + str(weapon_atk) + "\n"
			save += "WMG:" + str(weapon_mgc) + "\n"
			save += armor_name + "\n"
			save += "ADF:" + str(armor_def) + "\n"
			save += "AMD:" + str(armor_mdef) + "\n"
			save += str(potion) + "\n"
			save += str(hipotion) + "\n"
			save += str(xpotion) + "\n"
			save += str(ether) + "\n"
			save += str(maxether) + "\n"
			save += str(elixir) + "\n"
			save += str(megalixir) + "\n"
			save += str(bomb) + "\n"
			save += str(smoke) + "\n"
			target.write(save)
			target.close()
			print "\t\t\tGame saved!\n"
			
			#########SPAWNING ENEMIES#########
		elif action == '1': #normal enemy
			enemy_roll = random.randrange(0, 10)
			
			if enemy_roll < 3: #0, 1, 2
				enemy_name = 'Lasher'
				enemy_descrip = 'A ferocious clawing beast'
				ehp = 5 + 3 * random.randrange(1, lvl + 2)
				ehp += int(round(lvl/3)) * 5
				eatk = 3 + random.randrange(-1, lvl * 2 + 1)
				exp_drop = 10 + random.randrange(-3, 4)
				gold_drop = 10 + random.randrange(-3, 4)
				attack_type = 1 #Physical attack type
				
			elif enemy_roll >= 3 and enemy_roll < 6: #3, 4, 5
				enemy_name = 'Ahriman'
				enemy_descrip = 'Shoots magical waves of distortion'
				ehp = 2 + 3 * random.randrange(1, lvl + 2)
				ehp += int(round(lvl/3)) * 5
				eatk = 4 + random.randrange(1, lvl * 2 + 1)
				exp_drop = 10 + random.randrange(-3, 4)
				gold_drop = 10 + random.randrange(-3, 4)
				attack_type = 2 #Magical attack type
			
			elif enemy_roll >= 6 and enemy_roll < 8: #6, 7
				enemy_name = 'Bombe'
				enemy_descrip = 'Charges up for a mighty explosion'
				ehp = 5 + 3 * random.randrange(1, lvl + 2)
				ehp += int(round(lvl/3)) * 5
				eatk = 5 + random.randrange(3, lvl * 3 + 1) + 3 * lvl
				exp_drop = 12 + random.randrange(-5, 6)
				gold_drop = 12 + random.randrange(-5, 6)
				attack_type = 2 #Magical attack type
			
			elif enemy_roll >= 8 and enemy_roll < 10: #8, 9
				enemy_name = 'Sheldon'
				enemy_descrip = 'A slow but enduring shell'
				ehp = 5 + 6 * random.randrange(1, lvl + 2)
				ehp += int(round(lvl/3)) * 5
				eatk = 3 + random.randrange(-1, lvl * 2 + 1)
				exp_drop = 15 + random.randrange(-3, 4)
				gold_drop = 15 + random.randrange(-3, 4)
				attack_type = 1 #Physical attack type
			
			
			print "\t\t\tA", enemy_name, "appeared!"
			combatUI()
		
		elif action == 'bill': #billavuong
			print "\t\t\tA wild Billavuong appeared!"
			ehp = 100000 + 3 * random.randrange(-20, lvl * 3)
			eatk = 1000 + random.randrange(0, lvl * 2)
			combatUI()		
			
		elif action == 'peter': #phagg0t
			print "\t\t\tA flaming faggot has appeared!"
			ehp = 9999
			eatk = 9999
			combatUI()	
			
		elif action == 'b': #mini boss
			print "\t\t\tA hobgoblin mini boss has appeared!"
			ehp = 100 + 3 * random.randrange(-20, lvl * 3)
			eatk = 10 + random.randrange(0, lvl * 2)
			enemy_name = 'hobgoblin'
			combatUI()
		elif action == 'd': #final boss
			print "\t\t\tDemonlord Urza has appeared! Are you ready for the final challenge?"
			ehp = 300 + 25 * random.randrange(1, lvl + 1)
			eatk = armor * 2 + random.randrange(lvl, lvl * 3)
			enemy_name = 'Urza'
			combatUI()
		
		elif action == 'save.info': #print save info
			filename = name + '.txt'
			target = open(filename, 'r')
			print target.read()
			target.close()
			
		elif action == 'l': #Cheat - gain a level (100 exp)
			exp += 100
		elif action == 'c': #Cheat - fill combo gauge
			gauge = '---------------------'
		elif action == 'g': #Cheat - gain gold (1000g)
			gold += 1000
		elif action == '0': #Cheat - set hp to 1 hp
			hp = 1
		def calc_damage(raw_damage, focus): #Calculates attack damage done
			total = (raw_damage + weapon_atk)
			if focus == True:
				total = total * 1.75
				print "\t\t\tFocused attack!"
			total = int(round(total))
			print "\t\t\tYou hit the enemy for", total, "damage."
			return total
		def mag_damage(raw_damage):  #Calculates magic damage done
			total = raw_damage + weapon_mgc
			if total < 0:
				total = 0
			if weapon_name == 'Blood Funnel':
				total = int(round(total * 1.25))
			print "\t\t\tYou hit the enemy for", total, "damage."
			return total
		
		while hp > 0 and ehp > 0: #Combat initiates
			if cclass == 'fighter':
				print "\t\t\tActions: (1) Attack  (2) Skills"
				print "\t\t\tActions: (3) Item    (4) Escape"
			elif cclass == 'mage':
				print "\t\t\tActions: (1) Attack  (2) Magic"
				print "\t\t\tActions: (3) Item    (4) Escape"
			if len(gauge) == 21: #Ultimate option
				print "\t\t\t\t (5) *EPHEMERAL STYLE*"
			battle = raw_input(prompt)
			
			if weapon_name == 'Life Seeker':
				seek = int(round(ehp * 0.1))
			
			if weapon_name == 'Godblade':
				godchance = 2
			else:
				godchance = 0
			
			if battle == '1': #Regular attack
				attackAction = True
				damage = attack + random.randrange(-1, 2)
				if armor_name == 'The Forsaken':
					criticalhp = int(round(mhp * 0.1))
					if hp < criticalhp:
						damage *= 2
				if cclass == 'fighter':
					damage = int(round(damage * 1.25))
				if weapon_name == 'Muramasa':
					hpmiss = mhp - hp
					damage += int(round(hpmiss * 0.9))
					if hp == 1:
						damage = damage * 9999
						if mhp > 1:
							mhp -= 1 #Careful, you lose 1 max hp everytime you use this
						print "\t\t\t<<Death awaits you...>>"
				if random.randrange(0, 100) <= crit and weapon_name != 'Excalibur':
					print "\t\t\t>>>Critical!<<<"
					damage = damage * 3
				if weapon_name == 'Excalibur':
					totalcrits = ''
					count = 0
					critscount = 0
					while count < 5:
						count += 1
						if random.randrange(0, 2) == 0:
							damage = damage * 1.5
							totalcrits += "crits! "
							critscount += 1
					if critscount == 5:
						damage = (damage + 1000) * 2
						print "\t\t\t<<By the holy sword of light, excalibur! Erase the enemy!!>>"
					else:
						print "\t\t\t", totalcrits
				damage = calc_damage(damage, focus)
				focus = False
				ehp -= damage
				
				#Weapon attack bonuses
				if weapon_name == 'Quoral Rapier':
					leech = int(round(damage * 0.125))
					hp += leech
					if hp > mhp:
						hp = mhp
					print "\t\t\tLeeched", leech, "HP."
				if weapon_name == 'Firebrand' or weapon_name == 'Godblade':
					if random.randrange(0, 8) < 2 + godchance: #chance to burn enemy for three turns
						eBurn = 3
						print "\t\t\tEnemy was burned."
				if weapon_name == 'Skyward Blade' or weapon_name == 'Godblade':
					if random.randrange(0, 10) < 2 + godchance: #chance to stun enemy for one turn
						eStun = True
						print "\t\t\tEnemy has been stunned."
				if weapon_name == 'Serpentine' or weapon_name == 'Godblade':		
					if random.randrange(0, 8) < 2 + godchance: #chance to freeze slow enemy for two turns
						eFrozen = 2
						print "\t\t\tThe enemy got frostbite."
						
			if battle == '5' and len(gauge) == 21: #Ultimate attack
				print "\t\t\tUltimate...EPHEMERAL STYLE!!"
				if cclass == 'fighter':
					damage = attack + random.randrange(-1, lvl)
					if armor_name == 'The Forsaken':
						criticalhp = int(round(mhp * 0.1))
						if hp < criticalhp:
							damage *= 2
					if cclass == 'fighter':
						damage = int(round(damage * 2.75))
						if focus == True:
							damage = int(round(damage * 0.75))
					if random.randrange(0, 30) <= crit:
						print "\t\t\t>>>Critical!<<<"
						damage = damage * 3
					damage = calc_damage(damage, focus)
					ehp -= damage
				elif cclass == 'mage':
					count = 0
					while count < 3:
						damage = magic + random.randrange(-1, lvl)
						damage = mag_damage(damage)
						ehp -= damage
						count += 1
				focus = False
				gauge = ''
				
			elif battle == '2' and cclass == 'fighter': #Fighter skills
				print "\t\t\tSkills: (1) Scan - 1mp  (2) Focus - 3mp"
				print "\t\t\tSkills: (3) Defend - 2mp  (4) ????"
				skill = raw_input(prompt)
				if skill == '1' and mp >= 1: #scan shows enemy hit points left
					mp -= 1
					eLife(ehp)
					print "\t\t\t", enemy_descrip
					print "\t\t\tThe enemy's attack power is", eatk
				elif skill == '2' and mp >= 3: #focus energy to deal 1.75x
					attackAction = True
					mp -= 3
					focus = True
					print "\t\t\t", name, "has focused his energy."
				elif skill == '3' and mp >= 2: #defend need attack
					mp -= 2
					defend = 0.2
					print "\t\t\t", name, "got into a defensive position."
				elif skill == '4':
					print "\t\t\tYou feel life force gathering around you..."
				else:
					print "\t\t\tYou don't have enough mp."	
					
			elif battle == '2' and cclass == 'mage': #Mage spells
				manacost = 1 + int(round(lvl*0.5))
				print "\t\t\tSpells: (1) Scan - 1 mp  (2) Heal - 3 mp  (3) Fire -", manacost, "mp"
				print "\t\t\t        (4) Lightning -", manacost, "mp  (5) Blizzard -", manacost, "mp"
				if weapon_name == 'Harbinger':
					print "\t\t\t        (6) Ultima -", mp, "mp"
				spell = raw_input(prompt)
				if weapon_name == 'Blood Funnel':
					print "\t\t\tYou drain your own life source..."
					drain = int(round(hp * 0.1))
					hp -= drain
					if hp <= 0:
						hp = 1
				if spell == '1' and mp >= 1: #scan shows enemy hit points left
					mp -= 1
					eLife(ehp)
					print "\t\t\t", enemy_descrip
					print "\t\t\tThe enemy's attack power is", eatk
				elif spell == '2' and mp >= 3: #heals you for your magic power plus a bit more
					mp -= 3
					heal = magic + random.randrange(3, 7)
					hp += heal
					if hp > mhp:
						hp = mhp
					print "\t\t\tYou have healed for ", heal, "hp."
				elif spell == '3' and mp >= manacost: #fire hits regular high numbers, stable results
					mp -= manacost
					bottom = int(round(-magic/4))
					damage = magic + random.randrange(bottom, magic + 1)
					damage = mag_damage(damage)
					ehp -= damage
					if weapon_name == 'Oathkeeper' and random.randrange(0, 2) == 1:
						print "\t\t\tDoublecast!!"
						bottom = int(round(-magic/4))
						damage = magic + random.randrange(bottom, magic + 1)
						damage = mag_damage(damage)
						ehp -= damage
					if random.randrange(0, 10) < 2: #chance to burn enemy for three turns
						eBurn = 3
						print "\t\t\tEnemy was burned."
					attackAction = True
				elif spell == '4' and mp >= manacost: #lightning most volatile, can hit highest but can also miss
					mp -= manacost
					bottom = -magic/2
					top = int(round(magic * 1.75))
					damage = random.randrange(bottom, top)
					damage = mag_damage(damage)
					ehp -= damage
					if weapon_name == 'Oathkeeper' and random.randrange(0, 2) == 1:
						print "\t\t\tDoublecast!!"
						bottom = -magic/2
						top = int(round(magic * 1.75))
						damage = random.randrange(bottom, top)
						damage = mag_damage(damage)
						ehp -= damage
					if random.randrange(0, 10) < 2: #chance to stun enemy for one turn
						eStun = True
						print "\t\t\tEnemy has been stunned."
					attackAction = True
				elif spell == '5' and mp >= manacost: #blizzard most consistant, hits normal with chance for 1.5x
					mp -= manacost
					check = random.randrange(0, 2)
					damage = magic
					if check == 0:
						damage = int(round(1.5*damage))
					damage = mag_damage(damage)
					ehp -= damage
					if weapon_name == 'Oathkeeper' and random.randrange(0, 2) == 1:
						print "\t\t\tDoublecast!!"
						check = random.randrange(0, 2)
						damage = magic
						if check == 0:
							damage = int(round(1.5*damage))
						damage = mag_damage(damage)
						ehp -= damage
					if random.randrange(0, 10) < 2: #chance to freeze slow enemy for two turns
						eFrozen = 2
						print "\t\t\tThe enemy got frostbite."
					attackAction = True
				elif spell == '6' and weapon_name == 'Harbinger': #Ultima spell
					print "\t\t\tUltima!!"
					range = random.randrange(3, 6)
					tenth = mp / 10
					manaburn = int(round(tenth * range))
					mp = 0
					damage = magic * manaburn
					damage = mag_damage(damage)
					attackAction = True
					ehp -= damage
				else:
					print "\t\t\tYou don't have enough mp."
			
			elif battle == '3':
				print "\t\t\tUse which item?"
				print "\t\t\t(1) Potion 	| ", potion, "x | Heals A Little HP"
				print "\t\t\t(2) Hi-Potion 	| ", hipotion, "x | Heals Some HP"
				print "\t\t\t(3) X-Potion 	| ", xpotion, "x | Heals A Lot of HP"
				print "\t\t\t(4) Ether 	| ", ether, "x | Heals A Little MP"
				print "\t\t\t(5) Max Ether 	| ", maxether, "x | Heals All MP"
				print "\t\t\t(6) Elixir 	| ", elixir, "x | Heals Some HP and MP"
				print "\t\t\t(7) Megalixir 	| ", megalixir, "x | Heals All HP and MP"
				print "\t\t\t(8) Bomb	| ", bomb, "x | Deals Damage"
				print "\t\t\t(9) Smokescreen | ", smoke, "x | Makes it Rough to See"
				option = raw_input(prompt)
				if option == '1' and potion > 0:
					potion -= 1
					heal_amount = 10
					hp += heal_amount
					if hp >= mhp:
						hp = mhp
					print "\t\t\t", name, "healed for", heal_amount, "HP."
				elif option == '2' and hipotion > 0:
					hipotion -= 1
					heal_amount = 20 + int(round(mhp * 0.1))
					hp += heal_amount
					if hp >= mhp:
						hp = mhp
					print "\t\t\t", name, "healed for", heal_amount, "HP."
				elif option == '3' and xpotion > 0:
					xpotion -= 1
					heal_amount = 30 + int(round(mhp * 0.7))
					hp += heal_amount
					if hp >= mhp:
						hp = mhp
					print "\t\t\t", name, "healed for", heal_amount, "HP."
				elif option == '4' and ether > 0:
					ether -= 1
					heal_amount = 15
					mp += heal_amount
					if mp >= mmp:
						mp = mmp
					print "\t\t\t", name, "healed for", heal_amount, "MP."
				elif option == '5' and maxether > 0:
					maxether -= 1
					mp = mmp
					print "\t\t\t", name, "healed to full MP."
				elif option == '6' and elixir > 0:
					elixir -= 1
					heal_amount = 30 + int(round(mhp * 0.4))
					hp += heal_amount
					if hp >= mhp:
						hp = mhp
					print "\t\t\t", name, "healed for", heal_amount, "HP."
					heal_amount = 20 + int(round(mmp * 0.4))
					mp += heal_amount
					if mp >= mmp:
						mp = mmp
					print "\t\t\t", name, "healed for", heal_amount, "MP."
				elif option == '7' and megalixir > 0:
					megalixir -= 1
					hp = mhp
					mp = mmp
					print "\t\t\t", name, "healed to full HP and MP."
				elif option == '8' and bomb > 0:
					bomb -= 1
					damage = random.randrange(1, 4)
					damage = int(round(ehp * damage / 4))
					ehp -= damage
					print "\t\t\tYou threw a bomb which dealt", damage, "damage."
				elif option == '9' and smoke > 0:
					smoke -= 1
					smoked = 3
					print "\t\t\tYou threw a smokescreen which makes it hard for the enemy to see."
				else:
					print "\t\t\tYou do not have that item."
			
			elif battle == '4':
				esc = speed - int(round(lvl/2))
				if weapon_name == 'Blackbriar':
					esc += 5
				if random.randrange(0, 10) < esc:
					escape = True
					ehp = 0
					print "\t\t\tRan away swiftly."
				elif random.randrange(0, 3) == 0:
					escape = True
					ehp = 0	
					print "\t\t\tRan away safely."
				else:
					print "\t\t\tFailed to escape."
			
			burn_damage = checkBurn(eBurn)
			if burn_damage > 0:
				ehp -= burn_damage
				eBurn -= 1
			
			if attackAction == True:
				gauge += '-'
			
			if weapon_name == 'Life Seeker' and attackAction == True:
				if seek > 20 + lvl * 3:
					seek = 20 + lvl * 3
				print "\t\t\tYou drained", seek, "HP"
				ehp -= seek
				hp += seek
				if hp > mhp:
					hp = mhp
				seek = 0
					
			if ehp > 0 and escape == False: #Enemy attack
				if eStun == False:
					if enemy_name == 'Bombe' and echarge == False:
						echarge = True
						print "\t\t\tThe", enemy_name, "charges its attack.."
					elif armor_name == 'Cloak of Shadows' and random.randrange(0, 10) < 2:
						print "\t\t\tThe enemy missed its attack due to your shadowy movement!"
					else:
						if smoked > 0 and random.randrange(0, 4) < 3:
							print "\t\t\tThe smoke causes the enemy to miss its attack."
						else:
							if attack_type == 1: #physical damage type
								damage_reduce = 1 - (armor + armor_def)/100
								if damage_reduce < 0.2:
									damage_reduce = 0.2
							elif attack_type == 2: #magical damage type
								damage_reduce = 1 - (mdef + armor_mdef)/100
								if damage_reduce < 0.2:
									damage_reduce = 0.2
							#print "\t\t\tReduce", damage_reduce
							edamage = int(round(eatk * damage_reduce))
							#print "\t\t\tdmg", edamage
							variable = random.randrange(-2, 3) + 10
							variable = variable / 10.0
							edamage = int(round(edamage * variable))
							#print "\t\t\tdmg2", edamage
							if eFrozen > 0:
								edamage = int(round(edamage * 0.25))
								eFrozen -= 1
								print "\t\t\tThe enemy has frostbite and did reduced damage."
							if armor_name == 'Kraken\'s Shell':
								edamage = int(round(edamage * 0.8))
							edamage = int(round(edamage * defend))
							if edamage <= 0:
								edamage = 0
							print "\t\t\tThe enemy hit you for", edamage, "damage."
							hp -= edamage
							if armor_name == 'Barbed Armor' and edamage >= 3:
								reflect = 2 + int(round(edamage * 0.1))
								ehp -= reflect
								print "\t\t\tThe enemy took", reflect, "reflected damage."
							elif armor_name == 'Fire Vest':
								if random.randrange(0, 8) < 2: #chance to burn enemy for three turns
									eBurn = 3
									print "\t\t\tEnemy was burned."
							elif armor_name == 'Mirror Armor' and edamage >= 5:
								reflect = 4 + int(round(edamage * 0.5))
								ehp -= reflect
								print "\t\t\tThe enemy took", reflect, "reflected damage."
							echarge = False
				elif eStun == True:
					print "\t\t\tThe enemy was stunned and could not act."
					eStun = False
				if smoked > 0:
					smoked -= 1
					if smoked == 0:
						print "\t\t\tThe smoke fades away."
			
			if armor_name == 'Enigma' and hp > 0: #Enigma's hp regen
				regen = 5 + int(round(mhp * 0.05))
				hp += regen
				if hp > mhp:
					hp = mhp
				print "\t\t\tEnigma's mystic healing healed you for", regen, "HP"
				
			if weapon_name == 'Vorpal Wand' and hp > 0: #Vorpal Wand's mana regen
				mregen = 3 + int(round(mmp * 0.1))
				mp += mregen
				if mp > mmp:
					mp = mmp
				print "\t\t\tVorpal Wand recovered", mregen, "MP"
			
			if weapon_name == 'Sieglinde': #Sieglinde's extra ephemeral charge
				gauge += '-'
			if len(gauge) >= 21:
				gauge = '====================='
			combatUI()
			attackAction = False
			defend = 1
			if ehp <= 0 and hp > 0 and escape == False: #Enemy defeated
				if action == '1':
					print "\t\t\tCongratulations, you have defeated the enemy!"
					print "\t\t\tYou have gained", exp_drop, "exp and", gold_drop, "gold.\n"
					exp += exp_drop
					gold += gold_drop
				elif action == 'b':
					print "\t\t\tCongratulations, you have defeated the miniboss!"
					expdrop = 30 + random.randrange(-5, 6)
					golddrop = 25 + random.randrange(-5, 6)
					print "\t\t\tYou have gained", expdrop, "exp and", golddrop, "gold.\n"
					exp += expdrop
					gold += golddrop
				elif action == 'd':
					print "\t\t\tCongratulations, you have defeated the demonlord!"
				if exp >= 100: #Level up function
					exp -= 100
					lvl += 1;
					if cclass == 'fighter': #Fighter lvl up
						mhp += random.randrange(3, 6)
						mmp += random.randrange(1, 3)
						attack += random.randrange(1, 4)
						magic += random.randrange(0, 2)
						armor += random.randrange(1, 3)
						mdef += random.randrange(0, 2)
						speed += random.randrange(0, 2)
						crit += random.randrange(0, 3)
					elif cclass == 'mage': #Mage lvl up
						mhp += random.randrange(2, 6)
						mmp += random.randrange(3, 6)
						attack += random.randrange(0, 2)
						magic += random.randrange(1, 4)
						armor += random.randrange(0, 2)
						mdef += random.randrange(1, 4)
						speed += random.randrange(0, 2)
						crit += random.randrange(0, 2)
					hp = mhp
					mp = mmp
					print "\t\t\tCongratulations, you have leveled up!"
					print "\t\t\tYou now have", hp, "/", mhp, "hp and", mp, "/", mmp, "mp."
					print "\t\t\tStats: ATK", attack, "MGC", magic, "ARM", armor, "MDF", mdef, "SPD", speed, "CRT", crit
					print "\n"
				focus = False
				eBurn = 0
				eStun = False
				eFrozen = 0
				smoked = 0
				echarge = False
			elif ehp <=0 and escape == True:
				escape = False
			elif hp <= 0: #Game over, you lost all your HP
				print "\t\t\t\t\t\tGame over, you have died."
				if action == 'peter':
					print "\t\t\t\t\t\tPeter says, 'Haha! You're a faggot!'"
				start_game()
start_game()