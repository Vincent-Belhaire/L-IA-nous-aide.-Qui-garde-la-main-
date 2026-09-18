# L’IA : qui garde la main ? — édition 5

## La bonne ouverture pour les vidéos

**Sur un hébergement web (conseillé pour une classe)** : placer `index.html` et le dossier `assets` côte à côte. Ouvrir l’adresse HTTPS du parcours. Les lecteurs YouTube reçoivent alors une origine web réelle. Vérifier les droits avant de republier les copies vidéo contenues dans l’archive.

**Sur ton ordinateur** : extraire tout le ZIP, puis ouvrir `Lancer_le_site.cmd` sous Windows, ou lancer `python3 serveur_local.py` sous Linux. Python 3 doit être présent. Le navigateur s’ouvre sur une adresse `http://127.0.0.1:…/index.html`. Garder la fenêtre du lanceur ouverte ; Ctrl+C arrête le serveur. Celui-ci écoute seulement sur ce poste, pas sur le réseau de la classe. Il n’installe aucun module et n’envoie aucune réponse d’élève.

**Par double-clic sur index.html ou sur le HTML autonome** : exercices, bilan et trois vidéos incluses sont utilisables. Les vidéos YouTube ne sont pas lancées depuis une origine `file:` : l’interface prévient au lieu d’afficher volontairement un lecteur en erreur 153. Cette limite n’est pas levée en ajoutant simplement un paramètre à l’URL. Aucun réglage de sécurité de Firefox ne doit être désactivé.

Internet est nécessaire pour les lecteurs YouTube. Une origine HTTP/HTTPS correcte ne garantit pas la lecture si le réseau du collège filtre YouTube, si des protections suppriment le référent ou si le diffuseur refuse l’intégration.

## Contenu

Huit dossiers, 24 activités d’entraînement, huit situations de transfert et un avis argumenté non noté automatiquement. Les questions, leurs réponses attendues et les données fictives sont conservées. Le document d’explication « De l’entraînement à l’utilisation » a été retiré ; les autres pièces nécessaires pour répondre restent consultables au-dessus des questions.

La barre Mode accompagné/zoom a été supprimée. Le zoom habituel du navigateur et les indices restent disponibles. Aucun accès « Repères enseignant » n’est présent dans le site. Les sources sont accessibles discrètement en pied de page.

## Médias : ce qui a réellement changé

Les pages complètes de Lumni ne sont plus insérées dans des iframes. Les sources originales restent accessibles dans Sources et crédits ; il n’est pas prétendu qu’un lecteur Lumni a été réparé ou trouvé.

- Comprendre : remplacement des deux pages Lumni par « L’IA est-elle vraiment intelligente ? », publication TFO de la série Ma vie avec l’IA, lecteur YouTube `Q4y5mxy5HWQ`.
- Usurpation : TF1 INFO, « Vidéo truquée : Florent Pagny alerte ses fans », vidéo fournie `M696918yAUA`.
- Vie privée : copie « Germain » de l’archive d’origine.
- Environnement : réintégration du reportage « Découverte — L’impact écologique de l’intelligence artificielle » depuis l’archive d’origine. Date exacte non établie. Les prévisions et chiffres ne sont pas présentés comme des données actuelles universelles.
- Création : réintégration de la vidéo Lumni / France Télévisions « Création de contenus : faut-il avoir peur de l’intelligence artificielle ? », document du parcours d’origine avec contexte de 2023. Ce n’est pas une présentation du droit actuel.
- Fiabilité : publication TFO « Peut-on faire confiance à l’IA ? », lecteur YouTube `5UvLW5AaTS0`.

L’émission France Inter du 3 septembre 2026 et les autres pages Lumni sont conservées dans les ressources complémentaires, **pas intégrées dans des cadres supposés fonctionner**. Le contenu de l’émission radio et un lecteur autorisé n’ont pas pu être confirmés.

Les trois copies vidéo incluses restent la propriété de leurs titulaires. Leur présence dans une archive fournie ne vaut pas autorisation de republication sur un hébergement public. Vérifier le cadre de diffusion retenu. Aucune vidéo YouTube n’a été téléchargée ou recopiée.

## Bilan et données

La session reste en mémoire dans l’onglet, sans export JSON, sans stockage persistant et sans transfert automatique vers un tableau de bord professeur. Actualiser ou fermer peut effacer les réponses. Imprimer le bilan avant de quitter.

Le bilan conserve les résultats, badges, point fort et prochain objectif. « Acquis ici » signifie que les trois activités au dernier essai et la situation de transfert sont réussies ; ce n’est pas une certification de maîtrise durable. Le détail conserve les premières réponses et les indices. L’avis argumenté dispose d’une impression distincte.

Les lecteurs YouTube ne sont chargés qu’au clic, jamais à l’ouverture de l’accueil. Ils utilisent les services du diffuseur. Le site ne transmet ni nom, ni réponse, ni avis à ces lecteurs. L’hébergeur du parcours peut enregistrer les connexions.

## Vérifications

Lire `VERIFICATIONS.txt` pour les tests réellement réalisés. Les métadonnées des publications YouTube et les adresses des lecteurs ont été contrôlées ; cela ne vaut pas vérification du flux sur le réseau du collège. Faire un essai réel avant une séance.

## Sources techniques

YouTube, API iframe et erreur 153 : https://developers.google.com/youtube/iframe_api_reference
YouTube, identification par le référent : https://developers.google.com/youtube/terms/required-minimum-functionality
MDN, X-Frame-Options : https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options

Les illustrations sont des SVG originaux créés pour le parcours. `index.html` contient le programme et les styles ; les copies `assets/app-source.js` et `assets/styles-source.css` facilitent leur lecture mais ne sont pas chargées par la page. Aucun dépôt GitHub n’a été modifié.
